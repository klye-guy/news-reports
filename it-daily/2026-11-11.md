---
title: "Daily IT and Cybersecurity Intelligence Summary — 2026-11-11"
type: it-daily
date: 2026-11-11
dtg: "110745 CST NOV 26"
period: "2026-11-10 ~0800 CST to 2026-11-11 ~0745 CST"
classification: "UNCLASSIFIED // FOR INFORMATIONAL USE"
tags: [it-daily, cybersecurity, sysadmin, Microsoft, Patch-Tuesday, MSRC, Outlook, CVE-2026-124194, NTLM, Windows-Search, CVE-2026-116928, LDAP, CVE-2026-119958, Schannel, CVE-2026-119952, Exchange, CVE-2026-118207, Xbox-Live, CVE-2026-112967, KB5132061, Windows-11-26H2, Windows-11-23H2, Edge, Adobe, Adobe-Connect, APSB26-191, Adobe-Experience-Manager, APSB26-189, CISA-KEV, BOD-26-04, Barracuda, ESG, CVE-2026-116606, CVE-2026-111560, Mandiant, Cisco, BroadWorks, CVE-2026-20320, Operation-Snowball, DeepSeek, Openwave, CVE-2026-111793, Google, Chrome, CVE-2026-125350, N-able, N-central, Able2Shell, CVE-2026-125883, CVE-2026-125881, CVE-2026-125878, CVE-2026-125879, CVE-2026-125882, CVE-2026-125880, CVE-2026-91000, OpenSSH, SSHole, CVE-2026-123158, SonicWall, CVE-2026-19868, WP-Duplicate, CVE-2026-123751, Nvidia, Jensen-Huang, Wachtell, OpenAI, Businesses-in-ChatGPT, Meta, Muse, Amazon, Ring, Turla, Cereal, ESET, Fireworks-AI, Notion, LLMJacking, Vanderbilt, BYOD-ransomware, Texas-HHS, Nintendo, DMCA, Picofly, HWFLY, SX-Core, Citron-NEO, yuzu, WeLib, Denuvo, ARTIFACT, Football-Manager-27, Destruction-AllStars, Eden, Eglantine, Lichii, RPCS3]
---

UNCLASSIFIED // FOR INFORMATIONAL USE  

DAILY IT AND CYBERSECURITY INTELLIGENCE SUMMARY  
DTG: 110745 CST NOV 26 (America/Chicago)  
PERIOD COVERED: ~0800 hours CST 10 NOV 26 through ~0745 hours CST 11 NOV 26 (CT)  
PREPARED FOR: Kyle Sibley  
CLASSIFICATION: UNCLASSIFIED // FOR INFORMATIONAL USE  

## EXECUTIVE SUMMARY

Microsoft's November Patch Tuesday landed at 1200 CST with roughly 1,090 to 1,260 CVEs, depending on who is counting, and one exploited zero-day: an Outlook flaw (CVE-2026-124194) that leaks NTLMv2 hashes when a user opens a crafted message file. It is fixed through Office updates, not Windows Update, and CISA put it in KEV with a 24 NOV deadline. The admin priorities beyond that are a zero-click Windows Search bug reachable through Exchange (CVE-2026-116928, CVSS 9.8), Windows LDAP RCE (CVE-2026-119958, 9.8) and Schannel RCE (CVE-2026-119952). CISA added six entries to KEV on 10 NOV: the Outlook bug, Chrome CVE-2026-125350, a Barracuda ESG chain that can reach root (due 13 NOV, exploitation confirmed by Barracuda), Cisco BroadWorks CVE-2026-20320 (used in an AI-driven intrusion on a European telecom), and Openwave Webtop. N-able shipped N-central 2026.4 Hotfix 2 (build 2026.4.1.26) with seven CVEs, hosted servers are back up, and on-prem servers should stay offline until upgraded. Agents and probes must also be upgraded, agents first. Adobe fixed 110 CVEs, including six CVSS 10.0 bugs in Adobe Connect. In big tech, Nvidia's board hired Wachtell to investigate Jensen Huang; the stock fell 5.47% Tuesday and was up about 5% premarket today. ESET exposed a Turla toolkit hiding inside Exchange servers. On the gaming side, Nintendo's DMCA notices widened to Switch modchip firmware: GitHub disabled a network of 144 Picofly repositories, a first for Nintendo.

## BIG TECH

## ITEM 1: Nvidia — Board Hires Wachtell to Investigate Huang; Shares Fell 5.47% Tuesday, Rebounding Premarket; Congressional Briefing Request

- WHAT / WHERE / WHEN: On Tuesday, 10 NOV, Nvidia said it had hired Wachtell, Lipton, Rosen & Katz, with partner and former acting SDNY US attorney Joon Kim leading, for a "thorough and independent" investigation into whether company secrets or national security were compromised through CEO Jensen Huang's relationship with Alice Huang, an alleged Chinese intelligence asset and Nvidia customer. Nvidia gave no timeframe and says Huang will lead "without interruption"; CNBC reports he was in the office Monday and Tuesday. Shares closed down 5.47% Tuesday after a 4.3% drop Monday, and were up 5.3% premarket at 0447 CST Wednesday (CNBC). The Guardian says the scandal has erased about $430 billion of market value. Morgan Stanley removed Nvidia from its top-pick list today. Tom's Hardware reports House members asked for a joint closed-door briefing on Nvidia's anti-espionage security protocols and could subpoena Huang if he does not respond by today. Earnings are 17 NOV.
- IMPACT ASSESSMENT: Still no product, driver or supply impact. The risk to watch is policy: lawmakers tying this to tighter AI-chip export rules, which could affect GPU pricing and availability over time.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: The Guardian (11 NOV, read directly); CNBC (11 NOV, read directly); Tom's Hardware (headline and search summary only; the subpoena deadline is not independently confirmed).
- FRAMING (TRADE/MAINSTREAM): CNBC framed it as investors weighing "spillover effects" before earnings; analyst Dan Ives put Huang's odds of removal at about 15%, while Yale's Jeffrey Sonnenfeld called it "about 50-50."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Hacker News posts on the board statement and on a report that Alice Huang helped secure over $7.5 billion of Nvidia imports drew about 8 to 10 points and almost no comments. Reddit was not checked.
- CONFIDENCE: HIGH on the law-firm hire and share moves. MODERATE on the congressional deadline (single outlet). LOW on the underlying espionage allegation (anonymous sourcing; China denies).

## ITEM 2: Big Tech Briefs — OpenAI "Businesses in ChatGPT," Meta Muse on Watches, Amazon Ring Security Robots

- WHAT / WHERE / WHEN: On 10 NOV, OpenAI announced "Businesses in ChatGPT," which lets companies claim profiles and run customer-facing agents inside ChatGPT. Meta brought its Muse AI agent to Apple Watch and Wear OS (TechCrunch). Amazon's Ring announced "Ring Robotics," including an indoor drone camera and a patrol robot for businesses (About Amazon).
- IMPACT ASSESSMENT: Low operational impact. Ring's autonomous cameras and drones raise the usual privacy and network-segmentation questions for anyone putting them on a home or office network.
- ACTION FOR ADMINS: None. Treat new camera robots as IoT and keep them on an isolated VLAN.
- SOURCE SYNOPSIS: OpenAI, TechCrunch and About Amazon pages (search titles and summaries only; not opened).
- FRAMING (TRADE/MAINSTREAM): Routine product coverage.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): The HN thread on Businesses in ChatGPT had 37 points and 10 comments.
- CONFIDENCE: MODERATE (search summaries only).

## SYSADMIN

## ITEM 3: Microsoft November Patch Tuesday — About 1,090+ CVEs, One Exploited Outlook Zero-Day; Zero-Click Windows Search via Exchange, LDAP and Schannel RCEs Lead the List

- WHAT / WHERE / WHEN: Microsoft released its November updates on 10 NOV at 1200 CST. Counts differ by method: ZDI says about 1,090 new CVEs, SecurityWeek 1,094, BleepingComputer 1,235 and The Hacker News 1,259; the MSRC CVRF feed shows 1,096 entries first published 10 NOV. That is the second straight month above 1,000, after October's record. BleepingComputer counts 66 Critical and CSO Online 63. The only exploited bug is CVE-2026-124194, an Outlook spoofing flaw (Moderate, CVSS 6.5). Opening a crafted message file makes Outlook contact an attacker-controlled location without the external-content warning, which discloses the user's NTLMv2 hash. The Preview Pane is not an attack vector. Affected products are Microsoft 365 Apps for Enterprise and Office LTSC 2021 and 2024; tbreak lists fixed builds 16.0.17932.21140 (LTSC 2024) and 16.0.14334.21048 (LTSC 2021). Microsoft credits "nono" and Benoît Sevens, whose credit mentions Anthropic's Claude. Other priorities, per ZDI and MSRC: CVE-2026-116928, Windows Search RCE (CVSS 9.8), which ZDI says is reachable through Exchange when the server automatically indexes a malicious attachment, so nobody has to open anything; CVE-2026-119958, Windows LDAP RCE (9.8, unauthenticated, serious on domain controllers); CVE-2026-119952, Windows Schannel RCE (8.1, "Exploitation More Likely"); CVE-2026-118207, Exchange RCE (8.8, authenticated); and CVE-2026-118146, AD DS RCE (8.8). ZDI counts 30 CVEs it considers wormable, including five in Message Queuing, four in DNS, two in DHCP Server, and two in Xbox, among them CVE-2026-112967, a CVSS 9.8 Xbox Live Networking Service RCE. The Windows 11 cumulative update is KB5132061 (builds 26300.9974, 26200.9974 and 26100.9974). This is the final monthly update for Windows 11 23H2 Enterprise and Education.
- IMPACT ASSESSMENT: The Outlook zero-day is a classic phishing credential-theft vector, and any environment that still allows outbound NTLM to the internet is exposed. The Windows Search/Exchange and LDAP bugs are the most dangerous unexploited items, because the network attack paths need no user action. Microsoft says publicly disclosed: none.
- ACTION FOR ADMINS: Push the Office/Microsoft 365 Apps update now; it comes through Office Click-to-Run channels or WSUS/Intune Office policies, not the Windows CU. Block outbound SMB (TCP 445) and NTLM to the internet and consider adding high-value users to Protected Users. Patch Exchange servers and domain controllers first (Windows Search, LDAP, Schannel, AD DS), then DNS, DHCP and MSMQ hosts. Move any remaining Windows 11 23H2 Enterprise/Education PCs to a supported release.
- SOURCE SYNOPSIS: MSRC CVRF API (read directly, ~0730 CST 11 NOV); ZDI November review (read directly); SecurityWeek, BleepingComputer, The Hacker News, tbreak, Five Nines and JPCERT (search excerpts); Microsoft KB5132061 page (search title).
- FRAMING (TRADE/MAINSTREAM): ZDI's Dustin Childs: "At this point, does the exact number actually matter?" He argued that fewer zero-days does not mean less exploitation, because AI is better at reversing patches than finding bugs in closed-source code. ZDI and BleepingComputer both warned not to let the 6.5 score downplay the Outlook bug.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): An HN post titled "Microsoft's Patch Tuesday surpasses 1k bugs for second month in a row" got almost no traction. The r/sysadmin megathread was not read (see Gaps).
- CONFIDENCE: HIGH on the zero-day, the CVE details and the KB numbers. Total counts vary by method, as noted.

## ITEM 4: Patch Fallout — KB5132061 Install Failures Reported; Edge 157 Picks Up the Chrome Zero-Day Fix

- WHAT / WHERE / WHEN: Neowin reports users seeing KB5132061 install failures with errors 0x800f0993 and 0x800f0989, and one user found that turning off the Windows Sandbox feature, restarting and retrying let it install. Microsoft lists no known issues for the update. Its KB page says KB5124010 or later and servicing stack 26100.9539 or later must be installed first. Microsoft Edge 157.0.4341.46, released 10 NOV, carries the fix for Chrome zero-day CVE-2026-125350.
- IMPACT ASSESSMENT: Expect a small number of failed installs on machines with Windows Sandbox enabled, which is common on admin and developer workstations. With Edge patched, every major Chromium browser now has a fix.
- ACTION FOR ADMINS: Watch WSUS/Intune compliance for 0x800f0993 and 0x800f0989. Test the Sandbox workaround on a pilot machine before using it broadly. Confirm Edge is at 157.0.4341.46 or later and Chrome is at 157.0.8103.50 or later.
- SOURCE SYNOPSIS: Neowin and Microsoft KB page (search excerpts); Edge version from a 2-Spyware summary and Microsoft Learn's Edge security release notes listing (search only; the Microsoft page was not opened).
- FRAMING (TRADE/MAINSTREAM): Neowin: "a Microsoft feature may be culprit."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: MODERATE (user reports; Edge build number from a secondary source).

## ITEM 5: Adobe November Patch Day — 110 CVEs; Six CVSS 10.0 Flaws in Adobe Connect, Four 9.9s in Experience Manager

- WHAT / WHERE / WHEN: Adobe released nine bulletins on 10 NOV fixing 110 CVEs. The Priority 2 bulletins are APSB26-191 for Adobe Connect (24 CVEs, 18 Critical, top CVSS 10.0; Connect 12.12 and earlier on Windows; fixed in 12.12.a, 12.11.i, 12.10.f, 12.9.a and 12.8.a) and APSB26-189 for Experience Manager (14 CVEs, including four CVSS 9.9 code-execution bugs, such as CVE-2026-114371; fixed in AEM Cloud Service 2026.10.29251 and the GRANITE-75052 cumulative hotfix for 6.5 and 6.5 LTS). ZDI says each Connect 10.0 bug is reachable over the network with no authentication or user interaction. After Effects, Audition, Dimension, Photoshop, Premiere, Media Encoder and the Content Credentials SDK got Priority 3 fixes. Adobe says none is exploited.
- IMPACT ASSESSMENT: Connect is the urgent one for anyone self-hosting it. Creative Cloud desktop apps are routine updates.
- ACTION FOR ADMINS: Patch on-prem Adobe Connect and AEM 6.5 servers this week. Let Creative Cloud update desktop apps.
- SOURCE SYNOPSIS: ZDI review (read directly); Adobe APSB26-191 and APSB26-189 bulletins, SecurityWeek and OpenAdvisories (search excerpts).
- FRAMING (TRADE/MAINSTREAM): SecurityWeek: "Adobe Patches 110 Vulnerabilities Across 9 Products."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH.

## CYBERSECURITY

## ITEM 6: N-able Ships N-central 2026.4 Hotfix 2 (Seven CVEs); Hosted Back Online; On-Prem Should Stay Offline Until Upgraded; Agents and Probes Must Also Update

- WHAT / WHERE / WHEN: On 10 NOV, N-able released N-central 2026.4 Hotfix 2 (build 2026.4.1.26), which addresses "the most critical" of the Able2Shell flaws disclosed 08 NOV. N-able published seven CVEs: CVE-2026-125883 (multiple XXE, CVSSv4 9.3), CVE-2026-125881 (SSRF in service-import schema validation, 9.3), CVE-2026-125878 (OGNL injection, 8.7), CVE-2026-125879 (root escalation through a syslog-ng config the `nable` user can write, 8.6), CVE-2026-125882 (RCE through file-repository upload path traversal, 8.6, credited to Nate Fair of Sprocket Security), CVE-2026-91000 (insecure IPC escalation, 8.4, reserved 14 SEP, before the public dump) and CVE-2026-125880 (stored XSS through MMS3 patch metadata, 8.3). Rapid7 says N-able confirmed on 11 NOV that hosted servers in every region were upgraded. The hotfix removes legacy MDM and temporarily disables built-in remote control; Take Control still works. Hosted and on-prem customers must upgrade agents first and probes second, because an upgraded probe cannot talk to old agents. A follow-up hotfix is planned for the remaining issues. N-able reported scanning tied to the public PoC but says it has no evidence of successful exploitation in customer environments; Huntress has seen none among its partners.
- IMPACT ASSESSMENT: The emergency outage is ending, but only seven CVEs cover what the researcher called 33 issues, so expect a second hotfix. The agent-first order matters: if you get it wrong, you lose visibility of endpoints.
- ACTION FOR ADMINS: Upgrade on-prem N-central to 2026.4.1.26 before reconnecting it to the internet. Then upgrade agents, then probes. Before restoring access, review logs from 08 NOV onward for new admin accounts, password resets and scripts pushed to endpoints. If an MSP manages you, ask them to confirm the upgrade and the log review.
- SOURCE SYNOPSIS: Tenable FAQ, Rapid7 ETR (with 11 NOV update), Huntress blog, BleepingComputer, and the N-able status page excerpt (search excerpts; none opened directly).
- FRAMING (TRADE/MAINSTREAM): Rapid7 urged an emergency upgrade "outside of normal patching cycles."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): No HN stories on the hotfix in the window. r/msp was not checked.
- CONFIDENCE: HIGH.

## ITEM 7: CISA KEV Adds Six on 10 NOV — Outlook, Chrome, Barracuda ESG Chain (Due 13 NOV), Cisco BroadWorks, Openwave

- WHAT / WHERE / WHEN: CISA catalog version 2026.11.10 (released 1303 CST) added CVE-2026-124194 (Microsoft Outlook, due 24 NOV), CVE-2026-125350 (Chromium XML use-after-free, due 24 NOV), CVE-2026-116606 and CVE-2026-111560 (Barracuda, due 13 NOV), CVE-2026-20320 (Cisco BroadWorks XXE, due 24 NOV) and CVE-2026-111793 (Openwave Webtop Media Transcoder, due 24 NOV). All carry BOD 26-04 forensic-triage requirements. Barracuda: CVE-2026-116606 (CVSS 9.3) lets an unauthenticated attacker who can reach the ESG admin UI restore a crafted backup and change global config; CVE-2026-111560 (8.6) is an admin command injection through the timezone field that gives root on ESG, ADC, WAF, WSG, BMA and WCC. Chained, they give root. Mandiant found both; Barracuda patched them 02 NOV (ESG 9.4.0.030 or later) and late on 09 NOV said it had seen exploitation "affecting a small number of organizations." Previdian logged 17 attempts against CVE-2026-116606 from 15 IPs between 09 and 11 NOV (SecurityWeek). Cisco BroadWorks CVE-2026-20320 was patched in August (RI.2026.07). Malbear Labs says a Chinese-speaking actor used an autonomous framework built on a jailbroken DeepSeek model ("Operation Snowball") to exploit it against a European telecom's BroadWorks XSP on port 2208, stealing private keys and SSL credentials and, over two weeks, thousands of subscriber billing and device records affecting 13 hosted organizations. Cisco's advisory still said PSIRT was not aware of malicious use.
- IMPACT ASSESSMENT: Barracuda ESG is a repeat target for Chinese state actors (2023 campaign), and the three-day deadline signals CISA sees urgent risk. BroadWorks matters mainly to telecoms and hosted-voice providers; for most US businesses it is a supplier question.
- ACTION FOR ADMINS: Patch Barracuda ESG to 9.4.0.030 or later and the other appliances to their listed fixes by 13 NOV, take admin UIs off the internet, and review config-import and timezone-change events. Ask any hosted-voice/UCaaS provider whether BroadWorks is on RI.2026.07 or later. Openwave affects only Webtop operators.
- SOURCE SYNOPSIS: CISA KEV JSON (read directly); Barracuda advisory and Mandiant MNDT-2026-0041/0042 (search excerpts); The Register, SecurityWeek, BleepingComputer, The Hacker News (search excerpts); Cisco advisory (search excerpt).
- FRAMING (TRADE/MAINSTREAM): The Register quoted Purplecop's Tausif Ahmed: "If your Email Security Gateway's admin UI is open to the internet, that's the first thing I'd close today." The Hacker News stressed the AI-agent angle of the BroadWorks attacks.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): No HN traction in the window. X and Reddit were not checked.
- CONFIDENCE: HIGH on KEV entries and vendor statements. MODERATE on Malbear's AI-campaign details (single research firm).

## ITEM 8: Turla's "Cereal" Toolkit Hid Inside Exchange to Steal NATO and EU Mail from Romanian and Kazakh Government Servers

- WHAT / WHERE / WHEN: ESET published research on 10 NOV attributing a campaign against government Exchange servers in Romania and Kazakhstan to Turla (FSB-linked; also called Secret Blizzard and Venomous Bear). A previously unknown toolkit, Cereal, includes CerealBox, which is embedded in an Exchange mail-processing service to capture selected messages in transit. In Romania it targeted mail exchanged with NATO and EU institutions. The attackers used the victims' own Exchange servers as command hubs instead of external C2. ESET first found it in November 2025 and could not determine initial access.
- IMPACT ASSESSMENT: The victims were not in the US, but the technique (persistence inside Exchange transport with no external C2) defeats network-based detection and applies to any on-prem Exchange. Combined with this month's Exchange CVEs, it strengthens the case for moving off or hardening on-prem Exchange.
- ACTION FOR ADMINS: On on-prem Exchange, inventory transport agents and loaded modules against a known baseline, and check ESET's published indicators.
- SOURCE SYNOPSIS: The Record (10 NOV, read directly), citing ESET; ESET's own report was not opened.
- FRAMING (TRADE/MAINSTREAM): ESET called abusing Exchange as a central hub "a rare technique, used by only a handful of APT groups."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): HN post "Exchange for breakfast: Turla's Cereal tricks are not for kids" (ESET's title) had 1 point.
- CONFIDENCE: HIGH (vendor attribution).

## ITEM 9: Incidents — Fireworks AI Breaches Hit Notion Customers; Vanderbilt Still Restricted; BYOD Also Claims Texas HHS

- WHAT / WHERE / WHEN: AI inference provider Fireworks updated its notice on 09 NOV: a "well-known, financially motivated" group stole account and billing data and secrets in a breach found 06 OCT, and a second intrusion on 23–24 OCT through a third-party cloud provider hosting its R&D machines exposed invoices, payment history and AI datasets. Unit 42 is investigating. Notion said some of its customers were affected through its use of Fireworks for its Insights feature and for open-weight model inference. Notion has disabled Insights and stopped serving open-weight models through Fireworks. The Record ties this to the "LLMJacking" trend Google and Mandiant described last week, with fraudulent cloud charges over $100,000 in a day at some victims. Vanderbilt restored campus Wi-Fi Monday evening, but most systems remain restricted; classes resumed Tuesday, and athletics ticketing is down (The Register, 10 NOV). BYOD also claimed an attack on Texas Health and Human Services, which has not confirmed an incident.
- IMPACT ASSESSMENT: Third-party AI inference providers are now part of the supply-chain attack surface: data sent to them for "features" can be stolen. Stolen API keys turn quickly into large cloud bills.
- ACTION FOR ADMINS: Inventory which SaaS tools send your data to third-party AI providers. Rotate LLM and cloud API keys, set spend alerts and quotas on AI services, and check Notion admin notices if your organization uses Notion.
- SOURCE SYNOPSIS: The Record (10 NOV, read directly); The Register (10 NOV, read directly).
- FRAMING (TRADE/MAINSTREAM): The Register led with the audio ransom message played on Vanderbilt computers.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): The Fireworks incident post on HN had 2 points.
- CONFIDENCE: HIGH on company statements. LOW on BYOD's claims (see Quarantined).

## ITEM 10: Carried Threats — OpenSSH SSHole and Three Others Due 12 NOV; SonicWall Due 20 NOV; WP Duplicate Still Unpatched

- WHAT / WHERE / WHEN: The four KEV entries from 09 NOV are due tomorrow, 12 NOV: OpenSSH "SSHole" CVE-2026-123158, GPUStack CVE-2026-102895, FreeSWITCH CVE-2026-116779 and IBM Aspera Faspex CVE-2026-123218. VMware ESX CVE-2026-41709 is due today, and Ivanti Connect Secure CVE-2026-118527 is due 13 NOV. No new developments were found this run for SonicWall CVE-2026-19868 (due 20 NOV) or WP Duplicate CVE-2026-123751 (still no fix, not in KEV).
- IMPACT ASSESSMENT: No change in risk; the deadlines are the news.
- ACTION FOR ADMINS: Finish the SSHole upgrade (OpenSSH 10.6p2 or later) and the other 12 NOV items today. Delete WP Duplicate.
- SOURCE SYNOPSIS: CISA KEV JSON (read directly); prior IT daily.
- FRAMING (TRADE/MAINSTREAM): No new coverage.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH.

## GAME PRESERVATION AND PIRACY

## ITEM 11: Piracy and DRM — WeLib Hit with $19.5M Default Judgment; ARTIFACT Updates Denuvo Hypervisor Bypasses; Destruction AllStars Reconfirmed for 25 NOV

- WHAT / WHERE / WHEN: TorrentFreak and Publishers Weekly report that the shadow library WeLib was hit with a $19.5 million default judgment on 10 NOV and ordered off its domains, with registrars and hosts told to disable them. Russian gaming sites (Playground.ru and others) report that the ARTIFACT group updated its hypervisor Denuvo bypasses for Stellar Blade, Planet Zoo 2, Football Manager 27 and Crimson Desert. SavePoint (10 NOV) reconfirmed that Destruction AllStars servers shut down 25 NOV, leaving only Arcade Mode challenges.
- IMPACT ASSESSMENT: Hypervisor bypasses keep requiring users to disable core OS protections, which is a malware risk. Destruction AllStars joins the list of purchased games losing their online play.
- ACTION FOR ADMINS: None. Keep HVCI and Secure Boot on gaming PCs; do not run hypervisor bypasses on machines that matter.
- SOURCE SYNOPSIS: TorrentFreak archive headline and Publishers Weekly (search excerpt); Playground.ru and VASILISK (search titles; enthusiast); SavePoint (search excerpt).
- FRAMING (TRADE/MAINSTREAM): Routine.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): r/CrackWatch was not checked.
- CONFIDENCE: HIGH (WeLib, Destruction AllStars); MODERATE (ARTIFACT updates, enthusiast sources).

## EMULATION

## ITEM 12: Nintendo Expands GitHub DMCA Campaign to Switch Modchip Firmware — 144-Repo Picofly Network Disabled; Two More yuzu Copies Wiped

- WHAT / WHERE / WHEN: GitHub published a Nintendo of America DMCA notice dated 06 NOV on Tuesday, 10 NOV. It targets `Ansem-SoD/Picofly`, firmware for an RP2040-Zero-based Switch modchip, and also covers SX Core, SX Lite and HWFLY firmware. Because the network was over 100 repositories and Nintendo said all or most forks infringe, GitHub disabled all 144. Nintendo argues the firmware bypasses the Switch's boot sequence and cryptographic signatures (17 U.S.C. 1201) and cites the Team-Xecuter criminal case (No. 2:20-cr-00127-RSL), in which Gary Bowser pleaded guilty. TorrentFreak says none of Nintendo's 90 earlier GitHub notices mentioned modchips. Several other Picofly/HWFLY firmware repos, including what a GBAtemp user calls the original Picofly source, were still up when TorrentFreak checked Wednesday. The same day's notices also covered Citron NEO (71 repos, reported 10 NOV) and two yuzu copies (`IpwnedU/yuzu-mainline-master` and `IpwnedU/yuzu-android-master`), whose owner has since wiped the code and points to the Internet Archive. No counter-notice has been filed. Switch 2 forks such as Eden NX2, Eglantine and Lichii were still being updated several times a day (Emu-France, 10 NOV) and are not named in any notice.
- IMPACT ASSESSMENT: This is a new front: Nintendo is now going after hardware-mod firmware, not just emulators and key tools. Installed modchips keep working, but finding firmware and updates will get harder, and fake "mirror" downloads are likely.
- ACTION FOR ADMINS: None. Get firmware only from known project sources; treat re-uploads as untrusted.
- SOURCE SYNOPSIS: TorrentFreak (11 NOV, read directly, linking the GitHub notices); Emu-France Switch 2 roundup (read directly). The GitHub notice itself was not opened.
- FRAMING (TRADE/MAINSTREAM): TorrentFreak: "After taking down Switch emulators and hacking tools on GitHub for years, Nintendo is now going after modchip firmware."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): The HN repost had 4 points. GBAtemp and r/SwitchHacks were not checked.
- CONFIDENCE: HIGH.

## ITEM 13: Emulator Releases — RPCS3 Drakengard 3 Performance Jump; Dolphin 2609b Still Current

- WHAT / WHERE / WHEN: Notebookcheck reports a large RPCS3 performance gain in Drakengard 3, with 240 to 360 FPS on suitable hardware. Dolphin's latest release is still 2609b (with crash, GPU and security fixes). There were no new releases of note found for Xenia, shadPS4 or PCSX2 beyond routine nightlies.
- IMPACT ASSESSMENT: Routine.
- ACTION FOR ADMINS: None beyond keeping Dolphin on 2609b or later.
- SOURCE SYNOPSIS: Notebookcheck and TechSpot (search excerpts only).
- FRAMING (TRADE/MAINSTREAM): Routine.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: MODERATE (search summaries).

## PATCH AND KEV WATCH

- NEW KEV, added 10 NOV: CVE-2026-116606 and CVE-2026-111560 Barracuda (due 13 NOV; ESG 9.4.0.030+); CVE-2026-124194 Microsoft Outlook (due 24 NOV; Office update); CVE-2026-125350 Chromium (due 24 NOV; Chrome 157.0.8103.50+, Edge 157.0.4341.46+); CVE-2026-20320 Cisco BroadWorks (due 24 NOV; RI.2026.07); CVE-2026-111793 Openwave Webtop (due 24 NOV).
- KEV due today and this week (verified against the CISA feed): VMware ESX CVE-2026-41709 (11 NOV); OpenSSH CVE-2026-123158, GPUStack CVE-2026-102895, FreeSWITCH CVE-2026-116779, IBM Aspera Faspex CVE-2026-123218 (12 NOV); Ivanti Connect Secure CVE-2026-118527 and the two Barracuda CVEs (13 NOV).
- KEV due next week: Apple CVE-2024-27834 (18 NOV); SonicWall CVE-2026-19868 (20 NOV).
- Past due as of today: Adobe Commerce CVE-2026-48356 and Google Brotli CVE-2026-111497 (10 NOV), plus the older items listed in the 10 NOV IT daily.
- Exploited, not in KEV: WP Duplicate CVE-2026-123751 (no patch). N-able N-central Able2Shell: scanning only, now patched in 2026.4.1.26 (seven CVEs, not in KEV).
- Critical patches this cycle: Microsoft November (CVE-2026-116928 Windows Search, CVE-2026-119958 LDAP, CVE-2026-119952 Schannel, CVE-2026-118207 Exchange, CVE-2026-118146 AD DS); Adobe Connect APSB26-191 and AEM APSB26-189; SAP CVSS 10.0 fixes from 10 NOV (see prior daily); N-central 2026.4 HF2.
- Pending fixes: N-able follow-up hotfix; Ubuntu LTS kernels for CVE-2026-98432 (not rechecked this run).
- End of support: Windows 11 23H2 Enterprise/Education received its final update on 10 NOV; .NET 8 and .NET 9 ended support 10 NOV.

## OPEN THREADS CARRIED FORWARD

- Microsoft Patch Tuesday: released and covered here. Next, watch for exploitation of the Windows Search/Exchange and LDAP bugs and wider KB5132061 install problems.
- N-able Able2Shell: Hotfix 2 out with seven CVEs; follow-up hotfix pending; still no confirmed customer compromise.
- Chrome CVE-2026-125350: now in KEV (due 24 NOV), and Edge is patched. Closed apart from the deadline.
- OpenSSH SSHole and the three other 12 NOV KEV items: deadline tomorrow.
- SonicWall CVE-2026-19868 (due 20 NOV) and WP Duplicate CVE-2026-123751 (unpatched): no change.
- Ubuntu kernel CVE-2026-98432: not rechecked this run.
- Nvidia / Jensen Huang: Wachtell investigation, congressional briefing request, earnings 17 NOV.
- Vanderbilt BYOD ransomware: systems still restricted; data-theft claims unverified.
- Football Manager 27 / Denuvo: ARTIFACT updated the bypass after launch.
- Destruction AllStars: shutdown 25 NOV at 0900 CST.
- Nintendo GitHub campaign: now includes modchip firmware (Picofly). Switch 2 Eden forks are still not named in any notice.
- NoName057(16) doxxing: not rechecked this run.
- New: Barracuda ESG exploitation (who is behind it, scale); BroadWorks "Operation Snowball"; Turla Cereal indicators.

## UNCONFIRMED / QUARANTINED

- BYOD's claims against Vanderbilt ("over 1 million SSNs," full domain-controller takeover, locked databases) and its claimed attack on Texas HHS are leak-site claims only, not confirmed by either institution.
- Malbear Labs' account of an autonomous AI agent built on a jailbroken DeepSeek model comes from a single research firm, and Cisco PSIRT had not acknowledged malicious use as of its advisory text.
- The congressional subpoena threat against Jensen Huang comes from one outlet's headline (Tom's Hardware) and was not confirmed independently.
- The Alice Huang espionage allegation rests on anonymous intelligence sourcing; China denies it.
- The workaround for KB5132061 install failures (disabling Windows Sandbox) comes from one user report, not Microsoft.

## GAPS AND NOTES

- Reddit (r/sysadmin Patch Tuesday megathread, r/msp, r/netsec, r/emulation, r/Piracy, r/CrackWatch), Slashdot, lobste.rs and X were not searched this run. Community framing comes only from Hacker News (Algolia), where none of the security stories got real traction.
- BleepingComputer, SecurityWeek, The Hacker News, Tenable, Rapid7, Huntress and vendor pages were read through search excerpts, not opened directly. The Record, The Guardian, CNBC, The Register, TorrentFreak, ZDI and Emu-France were read directly. CISA KEV and MSRC data came straight from their feeds.
- Microsoft's CVE total is reported differently by each outlet (1,090 to 1,259); this report gives the range rather than a single number.
- Apple, Google (outside Chrome), Intel, AMD, Broadcom, Oracle, Valve, Sony and xAI had no verified major items in the window. Microsoft's CVRF lists two AMD Zen information-disclosure CVEs (CVE-2026-84004 and CVE-2026-84005) rated Important.
- No corrections to the 10 NOV IT daily. Its N-able ETA of midday Eastern 10 NOV held: the hotfix shipped that day.

UNCLASSIFIED // FOR INFORMATIONAL USE  
