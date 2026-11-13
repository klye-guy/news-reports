---
title: "Daily IT and Cybersecurity Intelligence Summary — 2026-11-13"
type: it-daily
date: 2026-11-13
dtg: "130800 CST NOV 26"
period: "2026-11-12 ~0745 CST to 2026-11-13 ~0800 CST"
classification: "UNCLASSIFIED // FOR INFORMATIONAL USE"
tags: [it-daily, cybersecurity, sysadmin, Microsoft, Microsoft-365, Exchange-Online, EX1550543, MO1550821, outage, Intune, KB5132061, KB5126646, SQL-Server, SLMGR, KMS, 0x80041008, printing, Exchange-Server-2016, Exchange-Server-2019, Exchange-SE, CVE-2026-118207, N-able, N-central, 4EverAble2Shell, Agent2Shell, CVE-2026-90436, Apache-Axis, Sean-Bales, Huntback, Previdian, XMRig, Check-Point, Gaia, DynamicCLI, CVE-2026-123039, PHP2Shell, CVE-2026-109618, CVE-2026-109619, TSGA, ESXi, wiper, ConnectWise, ScreenConnect, RMM-Plus, CVE-2026-127063, SCKit, RelayTrap, CVE-2026-84869, Blackpoint, Huntress, MSP, Vates, Xen-Orchestra, XCP-ng, VSA-2026-062, VSA-2026-063, SignDrop, CLFS, Nightmare-Eclipse, Windows-zero-day, Citrix, NetScaler, CVE-2026-120869, Red-Hat-Quay, CVE-2026-123710, CVE-2026-110697, AMD, Turin, CVE-2026-0004, Google-Cloud, Operation-Endgame, Gootloader, CastleRAT, StealC, Operation-TorNado, Binance, TraderTraitor, FaceStealer, GitHub, wfx-loot, Aikido, Apify, TSMC, CISA-KEV, Barracuda, Ivanti, Nvidia, Jensen-Huang, Colette-Kress, Harvey-Jones, Megaspeed, Singapore, OpenAI, Daybreak, Google, Gemini-4-Hydrogen, Anthropic, Claude-outage, Valve, Steam, Humble-Bundle, 2FA, DODI, ESA, Notorious-Markets, delistings, Nintendo, DMCA, Citron-Neo, Eden, Dolphin, Xenia, RPCS3]
---

UNCLASSIFIED // FOR INFORMATIONAL USE  

DAILY IT AND CYBERSECURITY INTELLIGENCE SUMMARY  
DTG: 130800 CST NOV 26 (America/Chicago)  
PERIOD COVERED: ~0745 hours CST 12 NOV 26 through ~0800 hours CST 13 NOV 26 (CT)  
PREPARED FOR: Kyle Sibley  
CLASSIFICATION: UNCLASSIFIED // FOR INFORMATIONAL USE  

## EXECUTIVE SUMMARY

The biggest admin story is Microsoft 365. Exchange Online began failing around midday Thursday, 12 NOV, and took down Outlook, Teams calendar features, Copilot, Defender portal pages, Intune and the admin centers that depend on it. Microsoft's repeated fixes failed overnight; at 0658 CST Friday it reported "broader improvements now observed in North America," with email backlogs still draining and no root cause published. Microsoft says it has no evidence of malicious activity and promises a post-incident report. Microsoft also confirmed three more November update problems: printing failures for documents with zero-size images, KMS/SLMGR activation errors (0x80041008), and SQL Server linked-server connection leaks dating to October. Exchange 2016 and 2019 are now officially "permanently vulnerable." Two more MSP tools are under active attack. A researcher dumped a new N-able N-central exploit chain, 4EverAble2Shell, and attackers had rooted at least 21 servers within hours, 19 of them already on this week's Hotfix 2. Check Point disclosed an exploited Gaia root-escalation zero-day (CVE-2026-123039) that attackers chained with PHP2Shell to backdoor gateways and wipe an ESXi host. On ScreenConnect, ConnectWise assigned CVE-2026-127063 (CVSS 9.3) to the RMM+ extension; the worm feature in SCKit failed against patched clients. Xen Orchestra's VM-import flaw is still unfixed. A public Windows CLFS zero-day called SignDrop gives SYSTEM, though no exploitation is reported. CISA added nothing to KEV on 12 NOV; Barracuda and Ivanti deadlines are today. Police took down Gootloader, CastleRAT and StealC infrastructure and arrested 354 dark-web suspects, and DOJ moved to seize $1.2 billion of the Binance theft. In big tech, Nvidia is run by interim CEO Colette Kress after Jensen Huang resigned; Reuters reports a third relationship and Wired says employees are petitioning for his return. For gamers, repacker DODI retired and handed his site to a new team, and Humble Bundle has still not explained the missing 2FA.

## BIG TECH

## ITEM 1: Nvidia — Huang Out, Kress Interim CEO and Jones Chair; Reuters Reports a Third Relationship; Employees Petition for His Return; Singapore Says US Gave "Limited" Help

- WHAT / WHERE / WHEN: Nvidia announced on Thursday, 12 NOV, that Jensen Huang resigned as president, CEO and director, effective immediately; its 8-K says the board accepted the resignation on 11 NOV. CFO Colette Kress is interim CEO while staying CFO, and director Harvey Jones, a former Synopsys CEO, is the company's first board chair (Nvidia release and 8-K, per the 13 NOV world-events daily; Ars Technica; The Register). Later Thursday, Reuters reported, citing two people familiar with the matter, that Huang had an intimate relationship with a second Nvidia employee, whom it did not name, in addition to Alice Huang and VP Kimberly Powell; Nvidia declined to comment (Reuters via CNA and The Hindu). Wired reported that an internal suggestion-box post asking the board to weigh employee sentiment has drawn more than 1,600 comments, mostly favoring bringing Huang back, and that one employee sent a companywide email saying "I stand by Jensen." Singapore's Ministry of Home Affairs said late Thursday that police investigated Megaspeed from February 2025 over possible false declarations on server purchases, that Alice Huang "was not investigated for espionage," that Supermicro gave "limited cooperation," and that repeated requests to the DOJ and FBI since September 2025 got "limited information or assistance" (The Register). Nvidia closed down 4.3% at $166.19 on 12 NOV and was up about 2.6% premarket Friday (Reuters, per the world-events daily). Earnings are still set for 17 NOV and an employee meeting for 18 NOV.
- IMPACT ASSESSMENT: No product, driver or supply change. The open questions for buyers are export-control fallout from the Megaspeed probe and whether a permanent CEO changes roadmap or pricing. For Kyle as a gamer, GeForce plans are unaffected for now.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: Ars Technica and The Register (12 NOV, headlines; The Register's Singapore story read directly, 13 NOV); Reuters via CNA and The Hindu (search excerpts with full text); Wired (12 NOV, read directly); The Verge and TechCrunch (search excerpts); the 13 NOV world-events daily for the 8-K and market figures.
- FRAMING (TRADE/MAINSTREAM): The Register called it Nvidia's "midlife crisis": "The competition is circling like vultures"; The Verge collected tech leaders calling the ouster "a mistake."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): "Jensen Huang resigns" was the top Hacker News story of the period (3,702 points, 3,230 comments). The Wired petition story drew 688 points and 532 comments, the Reuters third-relationship story 330 and 367, and the NYT's Singapore story 176 and 60.
- CONFIDENCE: HIGH on the resignation, appointments and Singapore statement. MODERATE on the third relationship (two anonymous sources; not confirmed by Nvidia).

## ITEM 2: Big Tech Briefs — OpenAI Launches Daybreak Security Agents; Gemini 4 Hydrogen Replaces Flash; Claude Has Two Outages

- WHAT / WHERE / WHEN: OpenAI announced two Daybreak security products at its 12 NOV "Cyber at the Frontier" event: Daybreak Red Team, which uses multiple AI agents to pentest web apps and validate findings (early-access requests), and Daybreak Defense Factory, which traces findings through code and drafts patches as GitHub pull requests for human review, importing from Wiz, Snyk and Endor Labs (SecurityWeek). The Register's headline said OpenAI "tells orgs they're doomed if they don't use them." Google released Gemini 4 Hydrogen on 12 NOV, replacing Gemini 3.8 Flash across its products and in Search AI Mode; API pricing stays at $1.50 per million input and $7.50 per million output tokens, while Carbon and Argon rise from $2/$10 to $4/$20 next month (Ars Technica). Google also launched Gemini smart glasses starting at $395 (Ars headline). Anthropic's status page logged a Claude authentication outage from 0358 to 0558 CST Friday and a new incident for "elevated errors" on claude.ai, the API and Claude Code at 0709 CST, still under investigation at report time. Its Microsoft 365 connector also failed Thursday because of the Microsoft outage.
- IMPACT ASSESSMENT: Gemini API users get a faster model at the same price, but the planned doubling of Carbon/Argon prices matters for budgets. The Claude incidents and Microsoft outage on the same morning are a reminder that AI tools inherit their providers' downtime.
- ACTION FOR ADMINS: Teams on Gemini Carbon or Argon should re-budget before the December price change. Check status.claude.com before troubleshooting Claude errors locally.
- SOURCE SYNOPSIS: SecurityWeek (13 NOV, read directly); The Register (headline); Ars Technica (12 NOV, read directly); Anthropic status RSS (read directly).
- FRAMING (TRADE/MAINSTREAM): Ars noted Hydrogen "isn't getting a slow, security-conscious release like Carbon and Argon."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): On HN, Gemini 4 Hydrogen drew 543 points and 339 comments, and Claude's 12–13 NOV errors 299 points and 243 comments. An X news summary put Claude outage reports above 3,800.
- CONFIDENCE: HIGH.

## SYSADMIN

## ITEM 3: Microsoft 365 Outage — Exchange Online Failure Cascades Across Teams, Copilot, Defender and Intune for More Than 18 Hours; Recovery Under Way, No Root Cause Yet

- WHAT / WHERE / WHEN: Exchange Online mailboxes began failing on Thursday, 12 NOV. The Register puts the start at about 1200 CST (1800 UTC); an incident timeline compiled by Xurrent from Microsoft's updates puts first impact at 1017 CST (1617 UTC). Microsoft opened EX1550543 for Exchange Online and MO1550821 for dependent services. Outlook (web, desktop MAPI, ActiveSync and REST), mail delivery, Teams calendar and meeting features, Copilot, Defender XDR and Defender for Office 365 portal pages, Microsoft 365 admin center pages, Intune, Universal Print, To Do and Windows 365 Cloud PCs using Customer Key were affected; services that do not depend on Exchange Online kept working (Microsoft status feed; The Register). Microsoft first blamed servers failing automated health checks, then said a process "responsible for establishing secure connections" was overwhelmed. It reverted a network change that coincided with the start of impact, tried an alternate health check, restricted traffic and scaled up VMs, some of which got "stuck in a bad state" (CIO; The Register). Overnight it said a patch to "an upstream authentication/routing configuration component" was improving stability (The Guardian). In its 0658 CST Friday update, Microsoft reported "broader improvements now observed in North America" and "sustained improvements across much of Europe," with some users still seeing intermittent access or delayed mail. It says "we have no evidence of malicious activity" and will publish a post-incident report with root cause; its next update was due at 0800 CST. Microsoft shares were down about 2% premarket (Reuters, per the world-events daily).
- IMPACT ASSESSMENT: This was a full workday without email for many US organizations, and admins lost the tools they would normally use to respond (Intune, admin centers, parts of Defender). Mail queued during the outage should deliver as backlogs clear, but expect late delivery, duplicate sends and confused users today.
- ACTION FOR ADMINS: Monitor EX1550543 and MO1550821 in the admin center or status.cloud.microsoft. Tell users to expect delayed mail and not to resend. Review security alerts and DLP actions that Defender may have delayed. Afterward, decide whether you need an out-of-band contact method (SMS, Signal, a secondary mail domain) and document what broke. Save the post-incident report for any SLA credit claim.
- SOURCE SYNOPSIS: Microsoft admin center status RSS (0658 CST 13 NOV, read directly); The Register (12 and 13 NOV, read directly); CIO, The Guardian live blog, iTnews, Moneycontrol and Xurrent (search excerpts).
- FRAMING (TRADE/MAINSTREAM): The Register: Microsoft's "fixes keep failing"; in Australia it was called the "Microsoft long weekend."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): HN posts on the status page drew 1,018 points and 859 comments, plus 397 points for "Outlook/365 still down after 12 hours." X summaries cite up to 140,000 Downdetector reports for Outlook and recirculated an old Hegseth video on Microsoft's China-based engineers. Cyberattack theories circulated but are contradicted by Microsoft (see Quarantined).
- CONFIDENCE: HIGH on impact and Microsoft's statements. MODERATE on the exact start time (sources differ). Root cause UNKNOWN.

## ITEM 4: More November Windows Update Fallout — Printing Failures, KMS/SLMGR Activation Errors, SQL Server Connection Leaks; Exchange 2016/2019 Declared "Permanently Vulnerable"

- WHAT / WHERE / WHEN: Microsoft confirmed that November security updates can make printing fail for documents containing images with zero height or width at the print resolution, often invisible watermark or layout objects inserted by document-generation tools. It was seen with Word printing through GDI, but other apps may be affected. It hits Windows 10 and later and Windows Server 2016 and later (WI1549472); the issue is still under investigation. Separately, `slmgr.vbs /skms-domain` and `slmgr.vbs /ipk` can fail with error 0x80041008 on Windows 10 21H2/22H2, Windows 11 23H2 and Server 2019/2022/2025 (WI1549486). Already-activated devices stay activated, a fix is due "over the coming days," and interim help requires Microsoft Support for Business. Microsoft also said that since the October update KB5126646, SQL Server linked-server queries using OLE DB providers (PostgreSQL and Oracle cited) can leave connections open until the server degrades. It affects Windows Server 2012 through 2025 and Windows 10 1809 onward, but not Windows 11 26H2. An out-of-band fix is expected within days; until then, close idle connections or restart the SQL service. The KB5132061 install-failure repair reported yesterday has had no new update. Microsoft's November Exchange SE release notes say Exchange 2016 and 2019 "are no longer tested for vulnerabilities" and should be considered "permanently vulnerable." The paid ESU ended with the 13 OCT updates. November fixed nine Exchange SE bugs, including critical RCE CVE-2026-118207.
- IMPACT ASSESSMENT: The SQL Server leak is the most dangerous for production because it degrades slowly. The activation bug hits imaging and deployment scripts. The printing bug will generate help-desk tickets that look like printer faults. Any remaining on-prem Exchange 2016/2019 now carries November's Exchange flaws with no fix.
- ACTION FOR ADMINS: Watch SQL Servers that use linked servers for growing connection counts, and plan restarts until the out-of-band fix arrives. Pause SLMGR-based KMS setup in task sequences or bake the KMS client key into images. Expect "blank page" print complaints from Word templates with hidden images. Move Exchange 2016/2019 to SE or Exchange Online now, and keep OWA/ECP off the internet in the meantime.
- SOURCE SYNOPSIS: BleepingComputer (13 NOV, read directly, twice); The Register (12 NOV, read directly, three stories).
- FRAMING (TRADE/MAINSTREAM): The Register: "Microsoft has an image problem with November's Windows security update."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): No notable HN traction; r/sysadmin could not be checked (Reddit blocked automated reads).
- CONFIDENCE: HIGH (Microsoft service alerts as reported by two outlets).

## ITEM 5: Patch Roundup — Citrix Fixes 10 Critical NetScaler Bugs; Red Hat Quay Registry Takeover Flaws (CVSS 9.8/9.9); Google Cloud Warns on AMD Turin TSA Flaws; No Apache httpd Exploitation Reported

- WHAT / WHERE / WHEN: Citrix released patches on 12 NOV for 28 NetScaler ADC and Gateway bugs, nine critical memory-overflow issues leading to unpredictable behavior or DoS (CVE-2026-120868, CVE-2026-107407 through CVE-2026-107410, CVE-2026-107412, CVE-2026-107415, CVE-2026-111334, CVE-2026-120864). Fixed builds: 14.1-73.57+, 13.1-64.39+, and the FIPS/NDcPP equivalents. Citrix also fixed NetScaler Console auth bypass CVE-2026-120869 (CVSS 9.4) in 14.1-74.34. No exploitation was mentioned (SecurityWeek). Red Hat disclosed two critical Quay registry flaws. CVE-2026-123710 (CVSS 9.8) lets anyone who can reach Quay plant a trusted signing key, even anonymously since anonymous access is on by default, and then read, push or overwrite any image. CVE-2026-110697 (CVSS 9.9) leaks other tenants' robot tokens through an unescaped SQL LIKE pattern. Fixes are out for eight Quay 3 branches; Red Hat says turning off anonymous access "doesn't protect you" (The Hacker News). Google Cloud says C4D, N4D, H4D, Z4D and G4 VMs on AMD Turin (Zen 5) need a guest OS patch and then a full stop and start, not a reboot, for TSA side-channel flaws CVE-2024-36350, CVE-2024-36357 and new CVE-2026-0004. AMD previously said Zen 5 was not affected by the first two. Debian has fixed it only in unstable so far (The Hacker News). No exploitation of Apache httpd CVE-2026-119618 was found in sources reviewed.
- IMPACT ASSESSMENT: NetScaler bugs are historically weaponized fast even when they start as DoS-only. The Quay flaw is a supply-chain risk for any OpenShift shop: a planted key survives restarts and password resets. The Turin issue matters mainly for multi-tenant and cloud workloads.
- ACTION FOR ADMINS: Patch NetScaler ADC/Gateway and Console this week. On Quay, block `/keys` at the proxy for untrusted clients, search audit logs for `service_key_rotate`/`service_key_delete` events with null expiration, remove unknown keys, then upgrade. Google Cloud Turin users: patch the guest kernel, then stop and start the VM. Keep Apache httpd 2.4.71 rollouts moving.
- SOURCE SYNOPSIS: SecurityWeek (13 NOV, read directly); The Hacker News (12 NOV, read directly, two stories).
- FRAMING (TRADE/MAINSTREAM): SecurityWeek noted NetScaler "vulnerabilities ... are a frequent target for threat actors."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): No notable HN traction.
- CONFIDENCE: HIGH on Citrix and Quay. MODERATE on Turin details (one secondary source).

## CYBERSECURITY

## ITEM 6: New N-able N-central Zero-Day "4EverAble2Shell" Exploited Within Hours; 21 Servers Rooted, 19 Already on Hotfix 2

- WHAT / WHERE / WHEN: On 12 NOV, researcher Sean Bales published proof-of-concept code for two new N-central exploit chains. 4EverAble2Shell chains Apache Axis CVE-2026-90436 (CVSS 9.8) with an N-central privilege escalation (the `setLDFileOwner` helper plus a symlink) to give an unauthenticated attacker root on appliances that have Legacy API enabled. Agent2Shell is claimed to give SYSTEM on managed Windows agents. Bales says both work on 2026.4 HF2 (build 2026.4.1.26), the 10 NOV fix for the earlier Able2Shell bugs. Previdian saw probing from 157.20.241[.]16 at about 0230 CST (0830 UTC) 12 NOV. Huntback saw full exploit attempts from 0316 CST and, by 0650 CST, found 21 compromised servers mining Monero with XMRig: 19 on HF2, 9 of them in the US (Lupovis). N-able disabled the Intune integration, restricted Legacy API and other features on hosted instances, and told on-prem customers to make sure Legacy API is disabled (the default). On 13 NOV it said it had found additional indicators of compromise and is working with specific customers. No CVE exists for the N-central escalation bug; Previdian tracks it as VULN-2026-0009. Bales says two RCE bugs he reported to N-able in July in another product remain unpatched.
- IMPACT ASSESSMENT: This is the second N-central wave in a week, and patching to HF2 did not protect servers with Legacy API on. So far the payload is a miner, but root on an RMM server is a path to every managed endpoint. Together with ScreenConnect, two major MSP platforms are under active attack.
- ACTION FOR ADMINS: On N-central, confirm Legacy API is disabled now. Check logs for requests to `/dms/services/ServerUI` referencing `jline.internal.TerminalLineSettings`, an unexpected `xvd.service`, and files under `/tmp/.xvd` or `/var/tmp/.xvd`. Treat any hit as full compromise: rebuild, and rotate every credential the server held. Keep upgrading agents and probes per HF2 guidance. If your MSP uses N-central, ask today whether Legacy API was enabled.
- SOURCE SYNOPSIS: BleepingComputer (12 NOV, read directly); SecurityWeek (13 NOV, read directly); The Hacker News (13 NOV, headline); N-able advisories (quoted via those outlets).
- FRAMING (TRADE/MAINSTREAM): Huntback, quoted by SecurityWeek: "Treat a hit as a full compromise, not a cleanup job. Applying Hotfix 2 is not enough on its own."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Bales told BleepingComputer it is "much much easier for me to just release the research I have." No major HN thread; r/msp could not be checked.
- CONFIDENCE: HIGH on exploitation and the victim count (two independent researchers). LOW on Agent2Shell's real-world impact (no exploitation reported).

## ITEM 7: Check Point Gaia Zero-Day CVE-2026-123039 Exploited Since Late October, Chained With PHP2Shell; Attackers Wiped an ESXi Host

- WHAT / WHERE / WHEN: Check Point released emergency hotfixes on Thursday, 12 NOV, for CVE-2026-123039, a local privilege escalation. The root-level Gaia DynamicCLI daemon listens on world-writable `/tmp/dynamic_socket` without authenticating callers, so any local user can run commands as root. Affected: Firewall, Multi-Domain Security Management, Scalable Platforms, Security Gateway and Security Management Server. Check Point says it saw exploitation "against a couple of dozen customers." Attackers got in through PHP2Shell (CVE-2026-109618/CVE-2026-109619, in KEV since 26 OCT) on Mobile Access portals, escalated to root, planted PHP webshells in the login-page directory, and installed TSGA and TSProxy, PhiliKit variants previously seen in China-linked UNC5221 attacks on Ivanti. In the first wave, from 30 OCT against Israeli organizations, they moved to a VMware ESXi host and ran a wiper, leaving a note mentioning Dream Security. A second, non-destructive wave began 2 NOV against gateways in several countries. Check Point says attribution can't be made with high confidence and lists false flag and access brokering as possibilities. CVE-2026-123039 is not yet in KEV.
- IMPACT ASSESSMENT: Firewalls are again the way in, and this chain ended in destruction of virtualization hosts. Any Check Point gateway with Mobile Access exposed and unpatched for PHP2Shell since October should be treated as suspect.
- ACTION FOR ADMINS: Apply the CVE-2026-123039 hotfix. If you can't, stop the `dynamic_server` process and keep it from restarting. Confirm the PHP2Shell fixes are in. Hunt with Check Point's IOCs, especially commands not run through the default Clish wrapper and use of the `system()` sink. Check for webshells in the Mobile Access portal directory. Isolate ESXi management from gateway networks.
- SOURCE SYNOPSIS: BleepingComputer (13 NOV, read directly); SecurityWeek (13 NOV, read directly); The Hacker News (headline); Check Point advisory and report (quoted via those outlets).
- FRAMING (TRADE/MAINSTREAM): SecurityWeek: "PHP2Shell Exploited in Destructive Check Point Gateway Attacks."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked beyond HN, where it got no traction.
- CONFIDENCE: HIGH on the flaw and exploitation. LOW on attribution (Check Point's own caveat).

## ITEM 8: ScreenConnect RMM+ Campaign Update — CVE-2026-127063 (CVSS 9.3) Assigned; SCKit's Technician-Infection Worm Failed Against Patched Clients

- WHAT / WHERE / WHEN: ConnectWise published CVE-2026-127063 on 12 NOV for the third-party DataComm RMM+ extension. Its description: the extension "uses a static API secret by default," and environments that keep the default can accept unauthorized requests, including commands to managed agents (CVSS 4.0 9.3, CWE-1392). No fixed RMM+ version exists. ConnectWise removed the extension from cloud instances and tells on-prem partners to disable it and not reinstall it. Huntress, which earlier described the issue as a blank access key in RMM+ 1.0.31 and 1.0.32, still counts 288 endpoints across 48 organizations, about a third hit in the first 10 minutes. BleepingComputer, Huntress and Blackpoint Cyber detailed SCKit's spreading mechanism. A component called RelayTrap, compiled on the victim from C# source that appears LLM-written, replaces the ScreenConnect Guest process and tries to push a file back to the connecting technician by exploiting CVE-2026-84869, a client file-transfer flaw patched in 26.6.5 and in KEV since September. Other components then steal technicians' ScreenConnect cookies and use the Shared Toolbox to spread to other customers. Blackpoint reproduced the exploit against a current client and found the fix blocks it; Huntress says the console takeover failed in every recovered host log.
- IMPACT ASSESSMENT: The worst case, a worm hopping between MSP customers, did not happen, but only because clients were patched. Anyone running ScreenConnect clients older than 26.6.5 is exposed to the technician-side attack.
- ACTION FOR ADMINS: Keep RMM+ and related extensions disabled. Update all ScreenConnect clients and technician installs to 26.6.5 or later. Review Run Command and Shared Toolbox history, and hunt for rogue ScreenConnect Access clients and `RelayTrap.cs` or compiled RelayTrap binaries. Keep investigating suspect hosts with separate tools, not interactive sessions.
- SOURCE SYNOPSIS: ConnectWise disclosure for CVE-2026-127063 on GitHub (read directly); BleepingComputer (12 NOV, read directly); The Hacker News (12 NOV, headline); Huntress blog and The Record (search titles).
- FRAMING (TRADE/MAINSTREAM): BleepingComputer: "New worm-like 'SCKit' malware targets MSPs in ScreenConnect attacks."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): An X news summary repeats that Sophos is tracking the spread (still unconfirmed elsewhere). No HN thread.
- CONFIDENCE: HIGH. Note the difference in root-cause wording: ConnectWise says static default secret, Huntress says blank key.

## ITEM 9: Xen Orchestra VM-Import Flaw (VSA-2026-063) Still Unfixed; Lower-Privilege Users Can Also Abuse It

- WHAT / WHERE / WHEN: As of 13 NOV, Vates has not shipped a fix for VSA-2026-063 (status "In progress"). Xen Orchestra passes imported XVA files to XAPI as the fully privileged pool-admin without reading `ova.xml`, so crafted keys such as `VM.platform:hvm_serial`, `VM.other-config:is_system_domain` and `VBD.other_config:backend-local` can compromise an XCP-ng host. Vates says the attacker used it with admin rights gained from the VSA-2026-062 authentication bypass, but any user with `vm.import`, `sr/import:vm`, `network/action:create` or `network/action:update` can abuse it. It affects Xen Orchestra 6.10.1 and earlier and the appliance, so installs patched for VSA-062 remain exposed. There is no CVE or CVSS score yet. Known indicators include a VM named `pivot2`, `hvm_serial: file`, and `/etc/cron.d/zz-ustar*` or `/.ustar*` files.
- IMPACT ASSESSMENT: Homelab and SMB XCP-ng users who delegate import rights are exposed even after patching the bypass.
- ACTION FOR ADMINS: Stay on 6.9.2 or 6.10.1 for the bypass. Restrict VM import to Admin and disable any user holding the four privileges above. Keep XO off the internet. Check every host for the indicators; if any are found, rotate secrets and reinstall.
- SOURCE SYNOPSIS: Vates advisory VSA-2026-063 (search excerpt with full text); The Hacker News update, IT-Connect, Magica, Thank You for Patching (search excerpts).
- FRAMING (TRADE/MAINSTREAM): The Hacker News added the second flaw as an update to its bypass story.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not found on HN; XCP-ng forums not checked.
- CONFIDENCE: HIGH (vendor advisory).

## ITEM 10: Public Windows Zero-Day "SignDrop" Gives SYSTEM via CLFS and Defender; No Patch, No Exploitation Reported

- WHAT / WHERE / WHEN: Researcher Abdelhamid Naceri ("Nightmare Eclipse") released SignDrop this week, a local privilege escalation that abuses how clfs.sys creates CLFS log authentication (`.cnpf`) files. A standard user creates a log file pointing at a chosen container path, then triggers Windows Defender's signature-update RPC so Defender opens it and writes a signature file as SYSTEM in an attacker-controlled location. Overwriting that file yields a SYSTEM shell. Naceri says he tested it on Windows 11 26H2 and Server 2025 Experimental builds, claims it works on 80% of Windows installs, and says "You're generally vulnerable if your Windows installation is older than 90 days." Cyderes compiled and ran the PoC and reports no in-the-wild exploitation. Microsoft had not commented to SecurityWeek. No CVE yet.
- IMPACT ASSESSMENT: Local-only, but public PoCs from this researcher have been picked up by ransomware operators before. It turns any foothold, such as a phished user, into SYSTEM on unpatched machines.
- ACTION FOR ADMINS: No patch yet. Watch for a Microsoft advisory or out-of-band fix. In the meantime, alert on unusual CLFS log or `.cnpf` file creation in user-writable paths and on unexpected SYSTEM shells spawned near Defender activity. Keep endpoint detection rules current.
- SOURCE SYNOPSIS: SecurityWeek (13 NOV, read directly); BleepingComputer and The Hacker News (headlines).
- FRAMING (TRADE/MAINSTREAM): BleepingComputer: "New Windows SignDrop zero-day gives hackers SYSTEM privileges."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): No notable HN traction.
- CONFIDENCE: HIGH that the PoC is public and works per Cyderes. LOW on the "80%" and "90 days" claims (researcher's own statements).

## ITEM 11: Law Enforcement — Operation Endgame Hits Gootloader, CastleRAT and StealC; Operation TorNado Arrests 354; DOJ Moves on $1.2B of Binance Theft and Disrupts FaceStealer

- WHAT / WHERE / WHEN: Police in the US, Europe, Australia and Canada seized 235 servers and 257 domains used by Gootloader, CastleRAT and StealC under Operation Endgame. Europol says 6.4 million stolen credentials were recovered and shared with Have I Been Pwned, Shadowserver and others; HIBP reports 180,000 email addresses and 893,000 unique passwords from CastleRAT. DOJ says Gootloader infected more than 25,000 computers and caused about $28.8 million in US damages (SecurityWeek). Europol and DOJ announced Operation TorNado: 354 arrests of vendors and buyers on Archetyp, Nemesis, Tor2Door, Bohemia and Kingdom, with more than €60 million and 57 firearms seized in Europe and more than €150 million, 4.8 tonnes of drugs and 152 firearms in the US (BleepingComputer). DOJ obtained authority to seize or restrain more than $1.2 billion from last month's $6.3 billion Binance theft, which Binance and the FBI attribute to North Korea's TraderTraitor. The FBI also disrupted infrastructure for "FaceStealer," a North Korean scheme that lures victims into fake Zoom or Teams calls, fakes an audio error, and has them install a "fix." The FBI says it stole more than $400 million in 18 months and has targeted npm and Rust crate maintainers (The Record).
- IMPACT ASSESSMENT: The credential haul means more users will get HIBP breach notices. FaceStealer targets developers and IT staff directly through compromised contacts' accounts.
- ACTION FOR ADMINS: Check your domains in HIBP's domain search. Brief developers and admins: never install a "fix" offered during a video call; leave and rejoin from a known client.
- SOURCE SYNOPSIS: SecurityWeek (13 NOV, read directly); BleepingComputer (13 NOV, read directly); The Record (12 NOV, read directly).
- FRAMING (TRADE/MAINSTREAM): FBI's Patrick Grandy, quoted by The Record: "If you can't imagine a scenario where you might fall prey to it, you are not thinking creatively enough."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH.

## ITEM 12: Incidents — "wfx-loot" Uses 4,837 Hijacked GitHub Accounts to Steal CI Secrets; Apify Confirms Customer Data Accessed; TSMC Says Employee Data Leaked via a Cloud Provider

- WHAT / WHERE / WHEN: Aikido says that starting about 0645 CST on 10 NOV, an attacker used 4,837 compromised GitHub accounts to probe 61,764 repositories for write access with pull requests titled "docs: dependency audit notes." It then injected a 1,500-line stealer into Actions workflows (or npm install hooks) to take GitHub, cloud (AWS/Azure/GCP via OIDC), npm, PyPI, Vault, Terraform and AI-service secrets, and deleted the runs in under a minute. Secrets were stolen from at least 1,835 targets (BleepingComputer; The Hacker News says 1,806+). Affected accounts include Fortune 100 companies, US GSA, the French government, Nextcloud and WebdriverIO, and about 50 have package-publishing rights. Automated publishing pushed the payload into Packagist `digitalelvis/neuronai-studio` 3.14.3 and Go module `github.com/onuragtas/docker-env` v1.0.278 and v1.0.280. Apify, a scraping platform with 91,000 customers, says an attacker used a compromised credential on 9–10 NOV to reach internal systems and customer accounts. A customer-posted notice lists salted password hashes, 2FA recovery codes, and Google/GitHub sign-in tokens among exposed data. Apify revoked OAuth connections including GitHub (SecurityWeek). TSMC said in a 12 NOV SEC 6-K that current and former employee data appeared on an external website, matches data held by a cloud service provider, and that it has "found no evidence that TSMC's systems have been compromised."
- IMPACT ASSESSMENT: wfx-loot is a broad CI supply-chain theft. Any org whose developers' GitHub accounts were compromised may have leaked cloud credentials, and 92% of the probe PRs are still open, meaning owners haven't noticed.
- ACTION FOR ADMINS: Search your repos for a `wfx-docs` branch, PRs titled "docs: dependency audit notes," and gaps in workflow run numbers. If the payload ran, rotate every secret and cloud role the workflow could reach. Pin Actions permissions to least privilege and require approval for workflows from outside contributors. Apify users: reset passwords and 2FA, and reconnect GitHub integrations.
- SOURCE SYNOPSIS: BleepingComputer (12 NOV, read directly); The Hacker News (headline); SecurityWeek (13 NOV, read directly); TSMC Form 6-K on SEC EDGAR (read directly).
- FRAMING (TRADE/MAINSTREAM): BleepingComputer: "Hackers compromise 4,800 GitHub accounts to steal cloud credentials."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): A "TSMC Hacked" HN post linking the 6-K drew 108 points, though the filing says TSMC's own systems were not shown to be compromised.
- CONFIDENCE: HIGH on company statements and Aikido's findings. Victim counts vary slightly between outlets.

## ITEM 13: KEV Status — No Additions on 12 NOV; Barracuda and Ivanti Due Today

- WHAT / WHERE / WHEN: The CISA KEV catalog was still at version 2026.11.10 (1,779 entries) at 0729 CST today. Nothing was added on 11 or 12 NOV. Due today, 13 NOV: Barracuda CVE-2026-116606 (ESG auth bypass) and CVE-2026-111560 (multi-product OS command injection), and Ivanti Connect Secure CVE-2026-118527. Newly reported exploited bugs not yet in KEV: Check Point CVE-2026-123039, N-central 4EverAble2Shell (Apache Axis CVE-2026-90436 plus an escalation bug without a CVE), ScreenConnect RMM+ CVE-2026-127063, and the Xen Orchestra flaws.
- IMPACT ASSESSMENT: KEV lags several confirmed exploited bugs this week; don't wait for it.
- ACTION FOR ADMINS: Close out Barracuda and Ivanti today. Treat the not-yet-listed items above as KEV-equivalent.
- SOURCE SYNOPSIS: CISA KEV JSON (read directly twice, last-modified 1303 CST 10 NOV).
- FRAMING (TRADE/MAINSTREAM): No new coverage.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH.

## GAME PRESERVATION AND PIRACY

## ITEM 14: Game Repacker DODI Retires, Hands Site to a New Team; ESA Wants It on USTR's Notorious Markets List

- WHAT / WHERE / WHEN: DODI, one of the best-known game repackers after FitGirl, announced on 12 NOV that he is retiring before his 24 NOV wedding and move to France: "No way to own or operate a pirated content site in France." He says domains, hosting and accounts were already transferred to a new "Dodi Repack Team," which made most recent releases. In its 2026 Notorious Markets filing, the ESA reported 7.14 million visits to the site in August, links to more than 2,000 games, and only 22% of reported links removed. It also flagged crypto payments from DODI-linked wallets to KYC exchanges including Binance as "an attribution and enforcement path." TorrentFreak notes that FMHY and r/Piracy previously stopped linking DODI's site over malware concerns, pointing users to his 1337x profile instead; Cyderes listed the domain in a February RenEngine malware report without implicating the operator.
- IMPACT ASSESSMENT: Unknown new operators running a site already flagged for malware raise the risk for anyone downloading from it.
- ACTION FOR ADMINS: None. For anyone on Kyle's networks: treat repack sites under new management as untrusted executables.
- SOURCE SYNOPSIS: TorrentFreak (13 NOV, read directly).
- FRAMING (TRADE/MAINSTREAM): TorrentFreak framed it as a planned exit amid "continued pressure from the game industry."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): r/Piracy and r/CrackWatch could not be checked (Reddit blocked).
- CONFIDENCE: HIGH on the announcement and ESA filing contents.

## ITEM 15: Gaming Briefs — Humble Bundle Still Silent on 2FA; Steam Review Backlog Up to 12 Business Days; Year-End Delistings

- WHAT / WHERE / WHEN: The Verge's Jay Peters found that Humble Bundle's redesigned settings page offers no way to add or change two-factor methods. At login he was sent an emailed access code, but he was never asked for the TOTP code he had set up, and he could change his password without entering the old one. Owner Ziff Davis/IGN had not commented. Valve says Steam build reviews, normally three to five business days, are "taking up to 12 business days" because of a "significant increase in submissions," and several indie developers have delayed launches (GamesIndustry.biz, citing Eurogamer). Delistings and shutdowns: TrollMaker servers end 16 NOV; Rough Draft leaves Steam 25 NOV; Destruction AllStars goes offline 25 NOV; Growtopia leaves PC storefronts 01 DEC; and the PS5/PS4 delistings on 31 DEC are unchanged (Delisted Games; Push Square).
- IMPACT ASSESSMENT: Humble accounts appear to have at least email-code login, which slightly corrects the "no 2FA at all" picture, but authenticator-app protection and password-change checks are still missing.
- ACTION FOR ADMINS: For Kyle personally: the earlier advice stands. Use a unique Humble password, redeem outstanding keys, and remove saved cards until Humble restores full 2FA.
- SOURCE SYNOPSIS: The Verge (12 NOV, read directly); GamesIndustry.biz (13 NOV, read directly); Delisted Games and Push Square (search excerpts).
- FRAMING (TRADE/MAINSTREAM): Rami Ismail, via GamesIndustry.biz: Valve avoiding a position on AI "is forcing them into choices that will inevitably be worse for developers."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): An X news summary says longtime Humble customers are removing saved payment details.
- CONFIDENCE: HIGH.

## EMULATION

## ITEM 16: No New Nintendo Takedowns Since the 06 NOV Notices; Coverage Spreads; Dolphin Adds CRT Shaders; Routine Xenia and RPCS3 Builds

- WHAT / WHERE / WHEN: GitHub's public DMCA repository shows no Nintendo notices beyond the four dated 06 NOV (three Yuzu-related, including the Citron NEO network, and one for Picofly); its 12 NOV commits were unrelated. Coverage widened: XDA totals about 217 Switch-related repos removed across the four notices and notes that the Switch 2 emulators Eglantine and Lichii share Yuzu code through Eden and "could be next." IGN's write-up reached the HN front page. Eden hosts its source on its own server and was unaffected. Dolphin dev build 2609-206 adds crt-pi and crt-lottes-fast CRT shaders (PR #12014, merged 1408 CST 11 NOV), and hotfix 2609b adds official Linux x64 and arm64 AppImages. Xenia v1.0.2844, Xenia Edge and an RPCS3 alpha build dated 12 NOV were posted, with no notable changes reported.
- IMPACT ASSESSMENT: Quiet day for enforcement. The risk to Switch 2 emulators is speculation at this point.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: GitHub `github/dmca` repository (read via API); XDA (12 NOV, search excerpt); LoveGame (search excerpt); VetTV/Dolphin download page (search excerpt); Emu-France build list (search excerpt).
- FRAMING (TRADE/MAINSTREAM): XDA: "Switch 2 emulators are safe for now."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): IGN's "Nintendo Takes Down Emulators and Firmware in Massive GitHub DMCA Sweep" drew 313 points and 246 comments on HN. r/emulation and GBAtemp were not checked.
- CONFIDENCE: HIGH on the absence of new public notices (as of the DMCA repo's latest commits). MODERATE on build details (secondary listings).

## PATCH AND KEV WATCH

- NEW KEV: none on 11 or 12 NOV (catalog 2026.11.10, 1,779 entries, at 0729 CST 13 NOV).
- KEV due today, 13 NOV: Barracuda CVE-2026-116606 and CVE-2026-111560; Ivanti Connect Secure CVE-2026-118527.
- KEV due later: Apple CVE-2024-27834 (18 NOV); SonicWall CVE-2026-19868 (20 NOV); Microsoft Outlook CVE-2026-124194, Chromium CVE-2026-125350, Cisco BroadWorks CVE-2026-20320, Openwave CVE-2026-111793 (24 NOV).
- Exploited, not in KEV: Check Point CVE-2026-123039 (hotfix out); N-central 4EverAble2Shell via Apache Axis CVE-2026-90436 plus an escalation bug without a CVE (disable Legacy API; HF2 alone is not enough); ScreenConnect RMM+ CVE-2026-127063 (no fix; disable); Xen Orchestra VSA-2026-062 (6.9.2/6.10.1) and VSA-2026-063 (no fix); WP Duplicate CVE-2026-123751 (not rechecked).
- Public PoC, no exploitation reported: Windows SignDrop (no patch); N-able Agent2Shell.
- Critical patches: Citrix NetScaler ADC/Gateway (nine critical) and Console CVE-2026-120869; Red Hat Quay CVE-2026-123710 and CVE-2026-110697; Exchange SE CVE-2026-118207; Apache httpd 2.4.71 (CVE-2026-119618); AMD Turin TSA CVE-2026-0004 (guest kernel plus stop/start on Google Cloud).
- Microsoft known issues: KB5132061 install failures (repair rolling out); printing with zero-size images (WI1549472, investigating); SLMGR/KMS 0x80041008 (WI1549486, fix in days); SQL Server linked-server leak since KB5126646 (out-of-band fix in days).
- EOL: Exchange Server 2016/2019, no updates and "permanently vulnerable."

## OPEN THREADS CARRIED FORWARD

- Microsoft 365 outage (new): full mitigation, post-incident report and root cause; SLA credits.
- N-central 4EverAble2Shell (new): N-able fix, CVE for the escalation bug, victims beyond 21, whether payloads go beyond mining.
- Check Point CVE-2026-123039 (new): KEV addition; attribution.
- ScreenConnect/SCKit: RMM+ fixed version; final victim count; Sophos involvement unconfirmed.
- Xen Orchestra VSA-2026-063: fix and CVE.
- Windows SignDrop (new): Microsoft response and CVE.
- Microsoft November known issues: activation and SQL Server out-of-band fixes; printing fix; KB5132061 repair completion.
- Nvidia: permanent CEO search; 17 NOV earnings; 18 NOV employee meeting; congressional testimony; Singapore/Malaysia probes.
- wfx-loot: more affected packages; GitHub response.
- Humble Bundle 2FA: company response.
- Apache httpd CVE-2026-119618: exploitation watch (none found).
- Barracuda ESG and Ivanti: KEV deadlines today.
- Anthropic IPO: pricing expected next week (not rechecked).
- Not rechecked this run: Turla Cereal, Cisco BroadWorks "Operation Snowball," Vanderbilt/BYOD, Maersk/WhiteArmor, iOS worse_query, eMudhra, Ubuntu CVE-2026-98432, NoName057(16).
- Destruction AllStars shutdown 25 NOV; Nintendo GitHub campaign (no new notices).

## UNCONFIRMED / QUARANTINED

- Cyberattack theories about the Microsoft 365 outage: speculation; Microsoft says it has "no evidence of malicious activity."
- Huang's relationship with a third woman, an Nvidia employee: two anonymous Reuters sources; not confirmed by Nvidia or Huang.
- Sophos tracking the ScreenConnect campaign: still only in X summaries.
- SignDrop working on "80%" of Windows installs and installs "older than 90 days" being vulnerable: researcher's claims, not independently measured.
- Agent2Shell's SYSTEM-on-agents claim: researcher's PoC; no exploitation reported.
- Check Point campaign attribution (China-linked tooling vs. false flag): Check Point itself declines to assess with high confidence.
- Switch 2 emulators being "next" for Nintendo: press speculation.
- Carry-forward: WhiteArmor's Maersk claims and BYOD's Vanderbilt/HHSC claims remain unverified; reported iPhone wallet losses tied to worse_query remain unsourced.

## GAPS AND NOTES

- Corrections and updates to the 12 NOV IT daily: (1) It said no CVE had been assigned to the ScreenConnect RMM+ issue; ConnectWise published CVE-2026-127063 on 12 NOV. Its wording (static default API secret) differs from Huntress's blank-key description used yesterday. (2) It said no Nvidia board decision had been announced; the 8-K shows the board accepted Huang's resignation on 11 NOV, before that report, and it was announced 12 NOV. (3) It said N-able had "no new developments"; the 4EverAble2Shell PoC and the first exploitation (from about 0230 CST 12 NOV) came before that report's cutoff but had not been published yet.
- Reddit returned HTTP 403 for automated reads again, so r/sysadmin, r/msp, r/netsec, r/cybersecurity, r/emulation, r/Piracy and r/CrackWatch were not checked. The Slashdot RSS returned empty and the lobste.rs feed did not parse. Community framing comes from Hacker News (Algolia) and X news summaries, which are AI-generated summaries of posts.
- Read directly: CISA KEV JSON, Microsoft status RSS, Anthropic status RSS, TSMC 6-K, ConnectWise CVE disclosure, GitHub DMCA repo, and articles from BleepingComputer, SecurityWeek, The Register, The Record, The Hacker News (Quay, Turin), Wired, The Verge, Ars Technica, TorrentFreak and GamesIndustry.biz. The Vates advisory, Reuters (third relationship), XDA, CIO, The Guardian and emulator build listings came through search excerpts. The WSJ, NYT and Bloomberg were not read (paywalled).
- Microsoft 365 start time differs by source (1017 CST per Xurrent's timeline of Microsoft updates, about 1200 CST per The Register). The outage was still being mitigated at report time; check Microsoft's 0800 CST update.
- Intel, Cisco (beyond KEV), Broadcom/VMware, Oracle, Sony, Meta, Apple, Amazon and xAI had no verified major items in the window.

UNCLASSIFIED // FOR INFORMATIONAL USE  
