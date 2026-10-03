// Headless Chrome print with CSS page size (letter) and backgrounds.
// No extra npm packages: a tiny DevTools websocket client.
import { spawn } from "node:child_process";
import crypto from "node:crypto";
import http from "node:http";
import net from "node:net";
import fs from "node:fs";

const htmlPath = process.argv[2];
const pdfPath = process.argv[3];
if (!htmlPath || !pdfPath) {
  console.error("Usage: node print-pdf.mjs INPUT.html OUTPUT.pdf");
  process.exit(2);
}

const port = 9400 + Math.floor(Math.random() * 500);
const userData = fs.mkdtempSync("/tmp/minder-chrome-");
const fileUrl = "file://" + htmlPath;

function getJSON(url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, (res) => {
      let d = "";
      res.on("data", (c) => (d += c));
      res.on("end", () => {
        try { resolve(JSON.parse(d)); }
        catch (e) { reject(e); }
      });
    });
    req.on("error", reject);
    req.setTimeout(1500, () => req.destroy(new Error("timeout")));
  });
}

function connectWS(wsUrl) {
  const u = new URL(wsUrl);
  return new Promise((resolve, reject) => {
    const key = crypto.randomBytes(16).toString("base64");
    const socket = net.connect(Number(u.port || 80), u.hostname);
    let buf = Buffer.alloc(0);
    let handshake = false;
    const queue = [];
    const waiters = [];
    let frag = [];
    let fragOp = 0;

    function pushText(text) {
      let msg;
      try { msg = JSON.parse(text); }
      catch (e) { return; }
      if (waiters.length) waiters.shift()(msg);
      else queue.push(msg);
    }

    function takeFrame(b0, payload) {
      const op = b0 & 0x0f;
      const fin = (b0 & 0x80) !== 0;
      if (op === 0) {
        frag.push(payload);
        if (fin) {
          const all = Buffer.concat(frag);
          frag = [];
          if (fragOp === 1) pushText(all.toString("utf8"));
        }
        return;
      }
      if (op === 1) {
        if (fin) pushText(payload.toString("utf8"));
        else { fragOp = 1; frag = [payload]; }
        return;
      }
      if (op === 8) socket.end();
      if (op === 9) {
        // masked pong, empty
        const mask = crypto.randomBytes(4);
        socket.write(Buffer.concat([Buffer.from([0x8a, 0x80]), mask]));
      }
    }

    function parse() {
      while (true) {
        if (buf.length < 2) return;
        const b0 = buf[0];
        const b1 = buf[1];
        let len = b1 & 0x7f;
        let off = 2;
        if (len === 126) {
          if (buf.length < 4) return;
          len = buf.readUInt16BE(2);
          off = 4;
        } else if (len === 127) {
          if (buf.length < 10) return;
          len = Number(buf.readBigUInt64BE(2));
          off = 10;
        }
        const masked = (b1 & 0x80) !== 0;
        const maskLen = masked ? 4 : 0;
        if (buf.length < off + maskLen + len) return;
        let payload = buf.subarray(off + maskLen, off + maskLen + len);
        if (masked) {
          const mask = buf.subarray(off, off + 4);
          const copy = Buffer.from(payload);
          for (let i = 0; i < copy.length; i++) copy[i] ^= mask[i % 4];
          payload = copy;
        }
        buf = buf.subarray(off + maskLen + len);
        takeFrame(b0, payload);
      }
    }

    const api = {
      send(obj) {
        const payload = Buffer.from(JSON.stringify(obj));
        const mask = crypto.randomBytes(4);
        const len = payload.length;
        let header;
        if (len < 126) header = Buffer.from([0x81, 0x80 | len]);
        else if (len < 65536) {
          header = Buffer.alloc(4);
          header[0] = 0x81;
          header[1] = 0x80 | 126;
          header.writeUInt16BE(len, 2);
        } else {
          header = Buffer.alloc(10);
          header[0] = 0x81;
          header[1] = 0x80 | 127;
          header.writeBigUInt64BE(BigInt(len), 2);
        }
        const masked = Buffer.alloc(len);
        for (let i = 0; i < len; i++) masked[i] = payload[i] ^ mask[i % 4];
        socket.write(Buffer.concat([header, mask, masked]));
      },
      next() {
        return new Promise((res) => {
          if (queue.length) res(queue.shift());
          else waiters.push(res);
        });
      },
      close() { socket.end(); },
    };

    socket.on("connect", () => {
      const path = u.pathname + u.search;
      socket.write(
        `GET ${path} HTTP/1.1\r\n` +
        `Host: ${u.host}\r\n` +
        `Upgrade: websocket\r\n` +
        `Connection: Upgrade\r\n` +
        `Sec-WebSocket-Key: ${key}\r\n` +
        `Sec-WebSocket-Version: 13\r\n\r\n`
      );
    });
    socket.on("data", (chunk) => {
      buf = Buffer.concat([buf, chunk]);
      if (!handshake) {
        const idx = buf.indexOf("\r\n\r\n");
        if (idx < 0) return;
        const head = buf.subarray(0, idx).toString("utf8");
        if (!head.includes(" 101 ")) {
          reject(new Error(head.split("\r\n")[0] || "websocket handshake failed"));
          socket.destroy();
          return;
        }
        handshake = true;
        buf = buf.subarray(idx + 4);
        parse();
        resolve(api);
        return;
      }
      parse();
    });
    socket.on("error", reject);
  });
}

const chromeBin = process.env.CHROME_BIN || "google-chrome";
const chrome = spawn(chromeBin, [
  "--headless=new",
  "--disable-gpu",
  "--no-sandbox",
  "--disable-dev-shm-usage",
  "--hide-scrollbars",
  "--no-first-run",
  "--no-default-browser-check",
  `--remote-debugging-port=${port}`,
  `--user-data-dir=${userData}`,
  "about:blank",
], { stdio: "ignore" });

let killed = false;
function cleanup() {
  if (killed) return;
  killed = true;
  try { chrome.kill("SIGKILL"); } catch {}
  try { fs.rmSync(userData, { recursive: true, force: true }); } catch {}
}
process.on("exit", cleanup);

async function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

try {
  let version = null;
  for (let i = 0; i < 60; i++) {
    try {
      version = await getJSON(`http://127.0.0.1:${port}/json/version`);
      break;
    } catch {
      await sleep(100);
    }
  }
  if (!version) throw new Error("Chrome DevTools did not start");

  let page = null;
  for (let i = 0; i < 30; i++) {
    const list = await getJSON(`http://127.0.0.1:${port}/json/list`);
    page = list.find((t) => t.type === "page" && t.webSocketDebuggerUrl);
    if (page) break;
    await sleep(100);
  }
  if (!page) throw new Error("No Chrome page target");

  const ws = await connectWS(page.webSocketDebuggerUrl);
  const pending = new Map();
  const listeners = {};
  let nextId = 0;
  (async () => {
    while (true) {
      const msg = await ws.next();
      if (msg.id && pending.has(msg.id)) {
        const p = pending.get(msg.id);
        pending.delete(msg.id);
        if (msg.error) p.reject(new Error(JSON.stringify(msg.error)));
        else p.resolve(msg.result || {});
      } else if (msg.method && listeners[msg.method]) {
        listeners[msg.method](msg.params || {});
      }
    }
  })();

  function call(method, params) {
    const id = ++nextId;
    return new Promise((resolve, reject) => {
      pending.set(id, { resolve, reject });
      ws.send({ id, method, params: params || {} });
    });
  }

  let loadResolve;
  const loaded = new Promise((r) => { loadResolve = r; });
  listeners["Page.loadEventFired"] = () => loadResolve();
  await call("Page.enable");
  await call("Emulation.setEmulatedMedia", { media: "print" });
  await call("Page.navigate", { url: fileUrl });
  await Promise.race([
    loaded,
    sleep(15000).then(() => { throw new Error("Timed out loading report HTML"); }),
  ]);
  await call("Runtime.evaluate", {
    expression: "document.fonts ? document.fonts.ready : true",
    awaitPromise: true,
  });

  const pdf = await call("Page.printToPDF", {
    printBackground: true,
    preferCSSPageSize: true,
    paperWidth: 8.5,
    paperHeight: 11,
    marginTop: 0,
    marginBottom: 0,
    marginLeft: 0,
    marginRight: 0,
    displayHeaderFooter: false,
    scale: 1,
  });
  if (!pdf.data) throw new Error("Chrome returned no PDF data");
  fs.writeFileSync(pdfPath, Buffer.from(pdf.data, "base64"));
  ws.close();
  cleanup();
} catch (err) {
  console.error(err && err.stack ? err.stack : err);
  cleanup();
  process.exit(1);
}
