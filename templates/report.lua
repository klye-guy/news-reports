-- Presentation-only filter for intel report PDFs.
-- Markdown stays the archive. No day-plan table rewrites.

local function slug(s)
  s = s:lower()
  s = s:gsub("[^%w]+", "-")
  s = s:gsub("^-+", ""):gsub("-+$", "")
  if s == "" then
    s = "section"
  end
  return s
end

local function meta_str(meta, key)
  if meta[key] == nil then
    return ""
  end
  return pandoc.utils.stringify(meta[key])
end

local function section_title(s)
  s = (s or ""):gsub("%s+$", "")
  if s == "EXECUTIVE SUMMARY" then return true end
  if s == "MN / US COST SNAPSHOT" then return true end
  if s == "UNCONFIRMED / MONITOR" then return true end
  if s == "SOURCE LIMITATIONS" then return true end
  if s:match("^GAPS / LIMITATIONS") then return true end
  if s:match("^ITEM%s+%d+") then return true end
  return false
end

function Meta(meta)
  local rt = meta_str(meta, "report_type")
  if rt == "" then
    rt = meta_str(meta, "type")
  end
  if rt == "" then
    rt = "report"
  end
  local labels = { daily = "DAILY", weekly = "WEEKLY" }
  meta.kind_label = pandoc.MetaString(labels[rt] or rt)
  meta.report_type = pandoc.MetaString(rt)
  local prepared = meta_str(meta, "prepared_for")
  if prepared == "" then
    prepared = meta_str(meta, "prepared-for")
  end
  if prepared ~= "" then
    meta.prepared_for = pandoc.MetaString(prepared)
  end
  local classification = meta_str(meta, "classification")
  if classification == "" then
    classification = "UNCLASSIFIED // FOR INFORMATIONAL USE"
  end
  meta.classification_line = pandoc.MetaString(classification)
  return meta
end

function Header(el)
  if el.level == 1 then
    return {}
  end
  local s = pandoc.utils.stringify(el)
  -- Normalize ITEM / standing section headings to level 2 so section-div
  -- ids and CSS hooks stay stable whether the Markdown used ## or ###.
  if el.level > 2 and (s:match("^ITEM%s+%d+") or section_title(s)) then
    el.level = 2
  end
  el.identifier = slug(s)
  return el
end

-- Plain section lines in the intel files are not ATX headings.
-- Promote those lines only, so CSS can target a slug. Words stay the same.

local function labelize(block)
  if block.t ~= "Para" and block.t ~= "Plain" then
    return block
  end
  local text = pandoc.utils.stringify(block):gsub("%s+", " ")
  local label, rest = text:match("^([^:\n]+):%s+(.+)$")
  if not label or not rest then
    return block
  end
  if #label < 2 or #label > 64 then
    return block
  end
  if label:find("%.", 1, true) or label:find(";", 1, true) then
    return block
  end
  local lbl = pandoc.Span({ pandoc.Str(label) }, pandoc.Attr("", { "lbl" }))
  local val = pandoc.Span({ pandoc.Str(rest) }, pandoc.Attr("", { "val" }))
  if block.t == "Para" then
    return pandoc.Para({ lbl, val })
  end
  return pandoc.Plain({ lbl, val })
end

function BulletList(el)
  for _, item in ipairs(el.content) do
    if item[1] then
      item[1] = labelize(item[1])
    end
  end
  return el
end

local function header_str(title)
  local h = pandoc.Header(2, { pandoc.Str(title) })
  h.identifier = slug(title)
  return h
end

local function collapse(s)
  return (s:gsub("%s+", " "):gsub("^%s+", ""):gsub("%s+$", ""))
end

-- Older archive files omitted the blank line Markdown needs before a list,
-- so pandoc glued "ITEM 1: …" and "- LABEL:" into one paragraph.
-- Split that presentation back apart when needed. Prefer real ATX headings
-- and a blank line before each item's bullet list in the Markdown source;
-- this filter still repairs glued paragraphs so PDFs stay correct.
local prose_titles = {
  "EXECUTIVE SUMMARY",
  "SOURCE LIMITATIONS",
  "GAPS / LIMITATIONS THIS RUN",
}

local function glued_blocks(text)
  for _, title in ipairs(prose_titles) do
    if text:sub(1, #title) == title then
      local rest = text:sub(#title + 1):gsub("^%s+", "")
      if rest ~= "" then
        return { header_str(title), pandoc.Para({ pandoc.Str(rest) }) }
      end
    end
  end
  local title, body = text:match("^(.-)%s+%-%s+(.*)$")
  if not title or not body then
    return nil
  end
  local known = title:match("^ITEM%s+%d+")
    or title == "MN / US COST SNAPSHOT"
    or title == "UNCONFIRMED / MONITOR"
    or title == "SOURCE LIMITATIONS"
    or (title:match("^GAPS / LIMITATIONS") and #title < 80)
  if not known then
    return nil
  end
  local parts = {}
  local buf = body
  while true do
    local a, b = buf:match("^(.-)%s+%-%s+(.*)$")
    if not a then
      parts[#parts + 1] = buf
      break
    end
    parts[#parts + 1] = a
    buf = b
  end
  local items = {}
  for _, part in ipairs(parts) do
    items[#items + 1] = { labelize(pandoc.Para({ pandoc.Str(part) })) }
  end
  return { header_str(title), pandoc.BulletList(items) }
end

function Para(el)
  local s = collapse(pandoc.utils.stringify(el))
  if section_title(s) and not s:find(" - ", 1, true) then
    local h = pandoc.Header(2, el.content)
    h.identifier = slug(s)
    return h
  end
  return glued_blocks(s)
end

function Table(tbl)
  local n = 0
  if tbl.head and tbl.head.rows and tbl.head.rows[1] then
    n = #tbl.head.rows[1].cells
  end
  if n >= 4 and tbl.attr and tbl.attr.classes then
    tbl.attr.classes:insert("wide")
    return tbl
  end
  return nil
end
