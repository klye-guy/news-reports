---
title: "Daily IT and Cybersecurity Intelligence Summary — 2026-11-10"
type: it-daily
date: 2026-11-10
dtg: "100800 CST NOV 26"
period: "2026-11-09 ~0740 CST to 2026-11-10 ~0800 CST"
classification: "UNCLASSIFIED // FOR INFORMATIONAL USE"
tags: [it-daily, cybersecurity, sysadmin, N-able, N-central, Able2Shell, RMM, MSP, CISA-KEV, BOD-26-04, OpenSSH, SSHole, CVE-2026-123158, Alpine, musl, GPUStack, CVE-2026-102895, FreeSWITCH, SignalWire, CVE-2026-116779, IBM, Aspera-Faspex, CVE-2026-123218, SonicWall, CVE-2026-19868, WordPress, WP-Duplicate, CVE-2026-123751, Microsoft, Patch-Tuesday, MSRC, Entra, CVE-2026-109469, .NET-8, .NET-9, Windows-11-23H2, Azure, SAP, ICM2SHELL, PROXYGATE, CVE-2026-76964, CVE-2026-89126, CVE-2026-89103, CVE-2026-120017, Google, Chrome, CVE-2026-125350, Mozilla, Firefox-160, MFSA-2026-125, Ubuntu, CVE-2026-98432, APT, CVE-2026-109518, Nvidia, Jensen-Huang, MegaSpeed, FBI, Anthropic, Claude-Fable-5.2, Claude-Mythos-5.2, TPU-8tx, IRGC, Shahid-Kaveh, CyberAv3ngers, ANSSI, Vanderbilt, BYOD-ransomware, Mittwald, MCP, SEGA, ARARA, NoName057(16), Football-Manager-27, Denuvo, ARTIFACT, Destruction-AllStars, delisting, Growtopia, Nintendo, DMCA, Citron-NEO, Eden, Switch-2, Dolphin, PCSX2, Xenia, shadPS4]
---

UNCLASSIFIED // FOR INFORMATIONAL USE  

DAILY IT AND CYBERSECURITY INTELLIGENCE SUMMARY  
DTG: 100800 CST NOV 26 (America/Chicago)  
PERIOD COVERED: ~0740 hours CST 09 NOV 26 through ~0800 hours CST 10 NOV 26 (CT)  
PREPARED FOR: Kyle Sibley  
CLASSIFICATION: UNCLASSIFIED // FOR INFORMATIONAL USE  

## EXECUTIVE SUMMARY

The biggest new admin problem is N-able N-central. A researcher published 33 alleged zero-days with working exploit code ("Able2Shell") late on 08 NOV. N-able took hosted N-central offline worldwide on 09 NOV and told on-premises customers to shut their servers down. There is no fix yet; N-able's hotfix ETA is midday Eastern today (about 1100 CST). watchTowr, Lupovis and Previdian have already seen exploit attempts against honeypots. CISA added four exploited bugs to KEV on 09 NOV with an unusually short 12 NOV federal deadline: OpenSSH "SSHole" (CVE-2026-123158, now confirmed exploited, with attackers stealing keys and planting persistence), GPUStack, FreeSWITCH and IBM Aspera Faspex. Google patched a Chrome zero-day (CVE-2026-125350) in 157.0.8103.50/.51. SAP shipped four CVSS 10.0 fixes this morning. Microsoft Patch Tuesday is not out yet; it is due at 1200 CST, and .NET 8 and .NET 9 reach end of support today. In big tech, Trump said the FBI is looking into Jensen Huang's relationship with an alleged Chinese agent, a shareholder sued Nvidia, and the stock closed down more than 4% on Monday. Anthropic released Claude Fable 5.2 and Mythos 5.2. France blamed Iran's IRGC for refrigeration sabotage at about 700 stores; Vanderbilt is dealing with a BYOD ransomware attack; SEGA leaked 2.2 million newsletter email addresses through a vendor. On the gaming side, Football Manager 27 launches today with a Denuvo bypass already out, and Nintendo's DMCA notice removed the Citron NEO Switch emulator and 70 forks from GitHub. Eden and the Switch 2 forks were not named.

## BIG TECH

## ITEM 1: Nvidia — Trump Says FBI Is Looking at Huang Affair; Shareholder Class Action Filed; Shares Closed Down More Than 4%

- WHAT / WHERE / WHEN: At a White House briefing Monday, 09 NOV, Trump said of CEO Jensen Huang's affair with Alice Huang, a former executive at Singapore-based Megaspeed who US intelligence reportedly says works for China's Ministry of State Security: "I know the FBI is looking into it in terms of something else, and I think that he'll be in good shape." Trump said Huang told him, "I had no idea that she was a spy." Nvidia shares closed down more than 4% Monday (Reuters). Shareholder Mark Kistenmacher filed a proposed class action in federal court in San Jose against Nvidia and Huang, alleging investors were misled about the relationship and about Nvidia's ties to Megaspeed (AP, Reuters, Courthouse News, Politico, 09 NOV). Nvidia's board says it has "no reason to believe that either national security or NVIDIA secrets were compromised"; a spokesperson told NBC that Huang will lead "without interruption." China's Foreign Ministry called the allegation "a smear." Reuters reported lawmakers now see tighter AI-chip export legislation as more likely.
- IMPACT ASSESSMENT: The story is now a legal and policy matter, not just a board review: a federal inquiry, securities litigation, and possible new chip-export rules. There is still no product, driver or supply impact. Q3 earnings are scheduled for 17 NOV, per earlier CNBC reporting.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: Al Jazeera and AP (10 NOV, read directly); Reuters via Hindustan Times; NBC News (updated 09 NOV); lawsuit details from AP, Reuters/Investing.com, Courthouse News and Law360 search excerpts. The complaint itself was not read.
- FRAMING (TRADE/MAINSTREAM): AP framed it as having "rocked the political class and America's tech sector"; Reuters focused on Huang's future and export-control fallout.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Hacker News stories on the lawsuit, a short seller who flagged the Megaspeed ties six months ago, and Trump–Huang ties each drew single-digit points and few comments. Reddit was not checked.
- CONFIDENCE: HIGH on Trump's remarks, the share move and the lawsuit filing. LOW on the espionage allegation (anonymous intelligence sourcing; China denies; Alice Huang has not commented).

## ITEM 2: Anthropic — Claude Fable 5.2 and Mythos 5.2 Released; Mythos Limited to Vetted Organizations

- WHAT / WHERE / WHEN: Anthropic announced Claude Fable 5.2 and Claude Mythos 5.2 on 09 NOV (about 1300 CST). Anthropic says they are the same underlying model: Fable has cybersecurity and biology safeguards and is available to all users, while Mythos is open only to vetted organizations through Anthropic's Cyber and Life Sciences Verification Programs. Pricing is $8 per million input tokens and $40 per million output tokens, with an optional fast mode at $16/$80. Fable 5.2 is available on the Claude Platform (`claude-fable-5-2`), Amazon Web Services, Google Cloud and Microsoft Azure; Microsoft announced it in Foundry the same day. Anthropic says Mythos 5.2 found 10.2% more vulnerabilities than Opus 5.5 on its internal CVE Rediscovery evaluation, that Fable 5.2 produced about 55% fewer unnecessary safety blocks than Fable 5.1, and that Fable falls back to Opus 4.8 on blocked cybersecurity queries.
- IMPACT ASSESSMENT: For admins, the practical change is that AI-driven bug finding keeps speeding up. That is the same dynamic OpenSSH's Damien Miller cited when he rushed the SSHole release, and it means shorter windows between disclosure and exploitation. Enterprise tenants may see the new model appear in Azure Foundry, Bedrock and Vertex model catalogs.
- ACTION FOR ADMINS: If you govern AI model access in Azure, AWS or GCP, review allow-lists for the new model IDs. No security action is needed.
- SOURCE SYNOPSIS: Anthropic announcement (09 NOV, read directly); The Verge (09 NOV, read directly); Microsoft Tech Community Foundry post (search title).
- FRAMING (TRADE/MAINSTREAM): The Verge led with the claims that the models solved open physics problems and formalized Fermat's Last Theorem.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): The main HN thread had about 700 points and 864 comments. Top comments mocked the naming (5.2 above Opus 5.5), complained about cost ("Too expensive for me"), and accused Anthropic of degrading Opus 5.5 ("lobotomized"). One noted the model appeared immediately in Claude Code.
- CONFIDENCE: HIGH on the release, pricing and availability. Benchmark and capability claims are vendor-reported.

## ITEM 3: Big Tech Briefs — Google Adds Two TPU 8 Variants; Microsoft Launches "Frontier Accelerate" Bundle

- WHAT / WHERE / WHEN: Google announced two more eighth-generation TPUs on 09 NOV: TPU 8tx for confidential computing for government and regulated businesses, and 8i Max for AI applications with large context windows. That makes four new TPUs this year, after the 8t and 8i in April (The Verge, 09 NOV). Microsoft announced "Frontier Accelerate," a cross-service package of expertise, savings, investments and training across Azure, databases, Copilot, security and Marketplace (Microsoft Cloud Blog, 09 NOV).
- IMPACT ASSESSMENT: Low operational impact. Confidential-compute TPUs matter mainly to government and regulated GCP tenants.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: The Verge (09 NOV, read directly); Microsoft Cloud Blog (search title and excerpt).
- FRAMING (TRADE/MAINSTREAM): Routine product coverage.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH (Google); MODERATE (Microsoft; read from a search excerpt only).

## SYSADMIN

## ITEM 4: Microsoft Patch Tuesday Not Yet Released (Due 1200 CST); .NET 8 and .NET 9 End of Support Today

- WHAT / WHERE / WHEN: As of about 0740 CST on 10 NOV, Microsoft's November security release had not been published. The MSRC November update guide (first posted 04 NOV, last updated 10 NOV at 0101 UTC) had 108 entries. All were early-posted entries for cloud services, Chromium/Edge, Linux kernel and open-source components (including OpenSSH CVE-2026-123158). None yet covered Windows or Office. One is rated Critical: Entra Device Registration elevation of privilege CVE-2026-109469 (CVSS 10.0, authorization bypass through a user-controlled key). MSRC says Microsoft has "already fully mitigated" it and that no customer action is required. The scheduled release time is 10:00 a.m. Pacific (1200 CST). Also today: .NET 8 and .NET 9 reach end of support (Microsoft .NET support policy), so .NET 10 LTS (supported to November 2028) is the upgrade target. A Danish admin blog notes that today is also the final security update for Windows 11 23H2 Enterprise and Education, and that the November CU will include October's out-of-band fixes, the removal of seven compromised root certificates (26 OCT), and gradual default enablement of Memory Integrity (HVCI) on eligible PCs.
- IMPACT ASSESSMENT: Any zero-days will be known only after 1200 CST. HVCI defaulting on can break old drivers and slow some systems, which matters for older hardware and gaming rigs. Unsupported .NET 8/9 runtimes on servers will stop getting security fixes after today's patches.
- ACTION FOR ADMINS: Hold the maintenance window for 10–12 NOV and check MSRC and CISA KEV after 1200 CST for exploited CVEs. Inventory .NET 8/9 runtimes (`dotnet --list-runtimes`) and plan .NET 10 migrations. Move Windows 11 23H2 Enterprise/Education PCs to 25H2 or 26H2. Test HVCI with legacy drivers on a pilot ring.
- SOURCE SYNOPSIS: MSRC CVRF API (read directly at ~0738 CST); Microsoft .NET support policy (search excerpt); J-Cave.dk admin blog (search excerpt); Help Net Security forecast (06 NOV). An AI-generated "predicted" article claiming an exploited Windows zero-day was found and discarded as fabricated.
- FRAMING (TRADE/MAINSTREAM): Help Net Security expected another very large CVE count after October's record 1,407 unique CVEs.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): The r/sysadmin megathread opens with the release and was not checked.
- CONFIDENCE: HIGH that the release is pending and on .NET end of support. MODERATE on the 23H2 and HVCI details (secondary blog).

## ITEM 5: SAP November Patch Day — Four CVSS 10.0 Flaws, Including Pre-Auth RCE in ICM and Web Dispatcher ("ICM2SHELL")

- WHAT / WHERE / WHEN: SAP's 10 NOV Security Patch Day fixed four unauthenticated CVSS 10.0 flaws. CVE-2026-76964 (ICM, Note 3778530) and CVE-2026-89126 (Web Dispatcher, Note 3778556) share one WebSocket reassembly bug that Onapsis calls ICM2SHELL; it allows pre-authentication memory corruption and code execution as `<sid>adm`. CVE-2026-89103 (SAP Gateway, Note 3798345, "PROXYGATE") lets an outsider impersonate an internal application server. CVE-2026-120017 (SAML2 service provider, Note 3849308) skipped signature checks on assertions in some configurations, allowing login as any user. The researchers say none has been seen exploited. Out-of-maintenance kernels are also affected and may not get fixes. On 7.93, patch level 419 is still vulnerable; you need the updated 401 stack kernel, 402, or 420 or later. For PROXYGATE, the kernel patch alone is not enough: you also need a restrictive `prxyinfo` or `gw/acl_mode_proxy = 1`.
- IMPACT ASSESSMENT: Critical for any shop running SAP, especially an internet-facing Web Dispatcher, and Fiori or Web GUI behind SAML SSO. Exploits were demonstrated privately to SAP, so expect public exploit work soon.
- ACTION FOR ADMINS: Patch the kernel and every Web Dispatcher in one rollout. Until then, disable WebSocket support as a stopgap (it breaks ABAP Push Channels and some Fiori features), lock down `prxyinfo`, set `gw/acl_mode_proxy = 1`, restrict gateway ports 33NN/48NN, and review SAML2 trusted IdPs and privileged SAML logons.
- SOURCE SYNOPSIS: The Hacker News (10 NOV, read directly, citing SAP's bulletin, Onapsis and RedRays); SAP Patch Day page, Onapsis advisories and BleepingComputer (search titles and excerpts; SAP notes require login).
- FRAMING (TRADE/MAINSTREAM): BleepingComputer headline: "SAP patches ICM2SHELL and PROXYGATE maximum severity flaws."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH.

## ITEM 6: Browsers — Chrome Zero-Day CVE-2026-125350 Fixed in 157.0.8103.50/.51; Firefox 160 and ESR 153.7/115.45 Fix 99 CVEs

- WHAT / WHERE / WHEN: Google's 09 NOV Stable update to 157.0.8103.50/.51 (Windows/Mac) and 157.0.8103.50 (Linux) has nine security fixes, including High-severity CVE-2026-125350, a use-after-free in XML reported anonymously on 06 NOV. Google says it "is aware that an exploit for CVE-2026-125350 exists in the wild." Extended Stable 156.0.8078.96 carries the same fix. Chrome 157 for Android (157.0.8103.50) shipped the same day. Mozilla released Firefox 160 (MFSA 2026-125, announced 10 NOV) with 99 CVE IDs: 58 high, 24 moderate and 18 low, none marked exploited. It also released Firefox ESR 153.7 (MFSA 2026-127) and ESR 115.45 (MFSA 2026-126). Several Firefox bugs are sandbox escapes; one was reported by OpenAI researcher Amy Burnett.
- IMPACT ASSESSMENT: The Chrome zero-day affects every Chromium-based browser until vendors ship the fix. Edge and the other Chromium browsers will follow. As of the 09 NOV KEV update, CISA had not added it.
- ACTION FOR ADMINS: Force a Chrome relaunch to 157.0.8103.50 or later through policy, and watch for Edge, Brave and Opera builds that include CVE-2026-125350. Deploy Firefox 160 or ESR 153.7.
- SOURCE SYNOPSIS: Chrome Releases blog (read directly); Mozilla security advisories index and MFSA 2026-125 (read directly).
- FRAMING (TRADE/MAINSTREAM): Not yet widely covered at cutoff.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH.

## ITEM 7: Linux and Cloud — Ubuntu LTS Kernels Still Unfixed for CVE-2026-98432; Azure North Europe Power Loss on 09 NOV

- WHAT / WHERE / WHEN: Ubuntu's tracker for CVE-2026-98432, a use-after-free in IPv4 TCP SYN-recv option handling that Ubuntu says "can lead to remote code execution," still lists 26.04, 24.04, 22.04 and 20.04 LTS (and older ESM releases) as "Vulnerable, work in progress." Only 26.10 is fixed (7.3.0-10.10). The APT fix for CVE-2026-109518 from 04 NOV stands; Ubuntu's tracker confirms the trigger needs a non-zero `Acquire::Retries`, which defaults to 3 from Debian 12 and Ubuntu 22.04. Separately, CloudAMQP relayed an Azure service issue: starting at 0917 UTC (0317 CST) on 09 NOV, multiple network devices in Azure North Europe lost power, leaving some servers unreachable. CloudAMQP marked it resolved at 1256 UTC (0656 CST).
- IMPACT ASSESSMENT: The kernel bug remains the larger open exposure for Ubuntu servers. The Azure event is mostly outside the window but matters for anyone running single-zone workloads in North Europe.
- ACTION FOR ADMINS: Keep vendor mitigations for CVE-2026-98432 in place and watch for Ubuntu USNs. If you ran workloads in Azure North Europe, check Service Health for the Azure post-incident review.
- SOURCE SYNOPSIS: Ubuntu CVE tracker pages for CVE-2026-98432 and CVE-2026-109518 (read directly 10 NOV); CloudAMQP status via OutageDB (read directly). The Azure status page itself was not read.
- FRAMING (TRADE/MAINSTREAM): No trade coverage found for either.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH (Ubuntu); MODERATE (Azure, relayed through a third-party status page).

## CYBERSECURITY

## ITEM 8: N-able N-central "Able2Shell" — 33 Alleged Zero-Days Dropped with Exploit Code; Hosted N-central Offline, On-Prem Told to Shut Down; Honeypot Attacks Begun

- WHAT / WHERE / WHEN: Researcher Sean Bales published 33 alleged N-central vulnerabilities late Sunday, 08 NOV, as four exploit chains with proof-of-concept code in a GitHub repository called Able2Shell. He tested them on N-central Appliance 2026.4.0.31 and believes earlier versions are also affected. The most serious chain abuses an unauthenticated XXE in service import to steal a trusted local session, reset a password and run commands as the `nable` user; it can also create an enabled "Default Administrator" account. Other chains include stored XSS to root and local privilege escalation to root. Bales told BleepingComputer he skipped vendor notice because N-able allegedly failed to fix bugs he had reported earlier in another product. N-able opened an incident at 1515 UTC (0915 CST) on 09 NOV, took Hosted N-central offline in the Americas, Europe and APAC, and "strongly advises" on-prem customers to take servers offline "until further notice." Ecoverse services under N-able Login stay up. N-able has said it has seen no exploitation or unauthorized data access. Its 0500 UTC 10 NOV update (2300 CST 09 NOV) put the hotfix ETA at "mid-day" Eastern today. watchTowr said on X that it saw exploitation attempts against N-central honeypots overnight. Lupovis and Previdian reported PoC-aligned SOAP probes against the XXE surface starting around 2200 UTC (1600 CST) on 09 NOV. No CVE IDs have been assigned. Huntress notes that N-able hotfixes that need no reboot may not change the version string.
- IMPACT ASSESSMENT: This is the top priority for any MSP, and for any business whose MSP uses N-central. A compromised RMM server can push commands to every managed endpoint, a pattern ransomware crews have used before. Hosted customers have lost their RMM console for more than a day.
- ACTION FOR ADMINS: Keep on-prem N-central offline, or at minimum block it from the internet, until N-able publishes the hotfix and restore guidance. Review N-central login and audit logs from 08 NOV onward for new admin accounts (especially "Default Administrator"), password resets and unexpected scripts pushed to endpoints. If your MSP uses N-central, ask them now about exposure and their plan. Verify the hotfix by N-able's guidance, not the version number.
- SOURCE SYNOPSIS: BleepingComputer and The Hacker News (09–10 NOV, search excerpts with N-able statements); Beazley Security advisory BSL-A1242 (updated 10 NOV); Rescana and Brandefense summaries citing the N-able status page and Huntress; X posts by watchTowr (via THN), Lupovis and Previdian (read directly). The N-able status page was not read directly (fetch failed).
- FRAMING (TRADE/MAINSTREAM): BleepingComputer noted that N-able "confirmed it is developing a hotfix," which lends credence to the claims. N-able calls the release "non-responsible communication."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): X security accounts are pushing honeypot and probe sightings and hunt guidance (new admin accounts, unexpected endpoint scripts), while some note the 33 flaws "have not all been independently verified." An HN thread linking Huntress drew little discussion. Reddit r/msp and r/sysadmin were not checked.
- CONFIDENCE: HIGH on the outage and vendor guidance. MODERATE on exploitation (honeypot attempts only; no confirmed victims). The researcher's full count of 33 is not independently verified.

## ITEM 9: CISA KEV Adds Four with a 12 NOV Deadline — OpenSSH SSHole (Now Confirmed Breaching Systems), GPUStack, FreeSWITCH, IBM Aspera Faspex

- WHAT / WHERE / WHEN: On 09 NOV (catalog version 2026.11.09, released 1954 UTC / 1354 CST), CISA added CVE-2026-123158 (OpenBSD OpenSSH on Linux, auth bypass, "SSHole"), CVE-2026-102895 (GPUStack improper authentication, giving unauthenticated admin access, secret disclosure and code execution via `POST /v2/inference-backends/from-yaml`), CVE-2026-116779 (SignalWire FreeSWITCH code injection allowing credential disclosure, call control and command execution) and CVE-2026-123218 (IBM Aspera Faspex incorrect authorization leading to privilege escalation). All four are due 12 NOV, three days instead of the usual three weeks. Each carries a BOD 26-04 "Forensics Triage" requirement, and ransomware use is listed as "Unknown." heise lists the fixes as GPUStack 2.2.0, FreeSWITCH 1.11.3 and Aspera Faspex 5.0.19 PL1, with CVSS 9.8 for those three. BleepingComputer reported 09 NOV that SSHole attempts began 05 NOV, the day a proof of concept appeared, and that successful exploitation was recorded the next day. It says post-access activity includes reconnaissance, theft of credentials and SSH keys, and persistence through `authorized_keys` edits or startup services. Microsoft's update guide also lists CVE-2026-123158, rated Important.
- IMPACT ASSESSMENT: SSHole is now confirmed as a breach vector, not just scanning, for Alpine/musl hosts without PAM. GPUStack matters for homelab and enterprise AI-GPU clusters; its flaw exposes cloud-provider secrets. FreeSWITCH underpins many VoIP and PBX stacks.
- ACTION FOR ADMINS: Patch by 12 NOV. For SSHole: upgrade to OpenSSH 10.6p2 or later and restart sshd, or set `PasswordAuthentication no`. On any exposed Alpine host, assume compromise and check `authorized_keys`, new services and `Accepted password` log lines for key-only accounts. Upgrade GPUStack to 2.2.0 and rotate the cloud and worker secrets it held. Upgrade FreeSWITCH to 1.11.3 or later and Aspera Faspex to 5.0.19 PL1 or later.
- SOURCE SYNOPSIS: CISA KEV JSON feed and CISA alert (read directly); heise (10 NOV, read directly); BleepingComputer (09 NOV, search excerpts; direct fetch blocked); eSecurity Planet and The Hacker News (search excerpts); MSRC CVRF.
- FRAMING (TRADE/MAINSTREAM): heise: "assume that systems accessible from the internet have been compromised," because CISA released no indicators of compromise.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): On X, admins urged starting with SSHole first among the four. One researcher posted a cyber-range detonation with PCAPs and Zeek logs. A Shodan-watcher noted SSHole and SonicWall CVE-2026-19868 are not yet tagged in Shodan, so exposure counts are unknown. The HN repost of BleepingComputer got little traction; the earlier "*sshole, or when are we going to get rid of C?" thread (06 NOV) is still the main discussion.
- CONFIDENCE: HIGH.

## ITEM 10: Carried Threats — SonicWall CVE-2026-19868 (KEV Due 20 NOV) and WP Duplicate CVE-2026-123751 (Still No Patch)

- WHAT / WHERE / WHEN: The SonicWall SonicOS SSL-VPN SAML/MFA bypass (CVE-2026-19868) is still in KEV with a 20 NOV due date; no new SonicWall advisory or indicators of compromise were found this run. The WP Duplicate (formerly LocalSync) plugin, through 1.1.11, still has no official fix for CVE-2026-123751, an unauthenticated arbitrary file upload exploited in the wild. Patchstack, GitHub Advisory GHSA-v9cp-82qp-rrj6 and SecurityOnline all still say no patch. It is not in KEV.
- IMPACT ASSESSMENT: No change from 09 NOV. Both remain open perimeter risks.
- ACTION FOR ADMINS: Upgrade SonicOS and audit SSL-VPN logins that skipped SAML. Delete WP Duplicate (deactivating it is not enough) and look for stray PHP files.
- SOURCE SYNOPSIS: CISA KEV JSON (read directly); Patchstack, GitHub Advisory Database, SecurityOnline (search excerpts).
- FRAMING (TRADE/MAINSTREAM): Unchanged.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH.

## ITEM 11: France Attributes Refrigeration Sabotage at ~700 Stores to IRGC's Shahid Kaveh (CyberAv3ngers); Names Commanders

- WHAT / WHERE / WHEN: France's Cyber Crisis Coordination Centre (ANSSI, military cyber command, DGSE and DGSI) published a five-page report on Monday, 09 NOV. It attributes the October sabotage of industrial refrigeration controllers at about 700 French grocery sites, which caused extensive food losses and at least 15 fires, to Shahid Kaveh, an IRGC unit. The US government has previously identified Shahid Kaveh as CyberAv3ngers, the group behind attacks on US water-utility controllers. The annex names Hamid Reza Lashgarian, Mahdi Lashgarian and Reza Salarvand. ANSSI also found the group targeting Schneider Electric equipment at small hydroelectric sites. France summoned Iran's ambassador and will seek EU sanctions, and Paris prosecutors requested international arrest warrants. A second wave in early November hit at least 11 European countries and is not covered by the report (The Record, 09 NOV).
- IMPACT ASSESSMENT: The same actor has hit US OT before, so internet-exposed refrigeration, building-management and PLC interfaces in US retail and food supply are plausible targets, particularly given US–Iran hostilities.
- ACTION FOR ADMINS: Remove internet exposure of OT, HMI and refrigeration-controller interfaces, change default credentials, and check them against the CISA and FBI CyberAv3ngers advisories.
- SOURCE SYNOPSIS: The Record (09 NOV, read directly); BleepingComputer (09 NOV, search excerpt).
- FRAMING (TRADE/MAINSTREAM): French Foreign Minister Barrot called the sabotage unprecedented in scale and aggressiveness.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH on the attribution as stated by France. Iran had not responded.

## ITEM 12: Incidents — Vanderbilt BYOD Ransomware Attack; Mittwald Hosting Breach via MCP Server; SEGA Newsletter Vendor Leaks 2.2 Million Emails

- WHAT / WHERE / WHEN: Vanderbilt University confirmed an "active cybersecurity incident" on Monday, 09 NOV. It told students and staff to shut down university devices and disconnect from campus Wi-Fi. The BYOD ransomware gang listed Vanderbilt on its leak site, and BleepingComputer confirmed that the ransom note's link leads to BYOD's site. Vanderbilt has not confirmed encryption or data theft. Ransomware researcher Allan Liska told The Record BYOD's first victim appeared on 29 SEP; the group is also linked to attacks on Michigan State and the University of New Mexico. German host Mittwald CM Service said attackers went undetected for eight days and compromised 56 customer projects through a flaw in the MCP server that lets customers connect AI assistants to its mStudio platform. It said log timing suggests AI-assisted speed but offered no other evidence (The Record, 09 NOV). SEGA disclosed on 09 NOV that a breach at newsletter provider ARARA exposed 2,196,044 email addresses, including 92,273 records with extra delivery information, from 11 newsletters sent between July and October 2026. SEGA says names, addresses, phone numbers, card data and passwords were not exposed, and SEGA Account emails were not affected.
- IMPACT ASSESSMENT: Mittwald is another case of AI-integration endpoints (MCP servers) becoming an attack surface. SEGA newsletter subscribers should expect targeted phishing.
- ACTION FOR ADMINS: Inventory and authenticate any MCP or AI-assistant endpoints exposed to customers or the internet. As a gamer, watch for SEGA-themed phishing.
- SOURCE SYNOPSIS: The Record (09 NOV, Vanderbilt and Mittwald, read directly); BleepingComputer (09 NOV, search excerpts); SEGA press release (search title) and CyberInsider (search excerpt).
- FRAMING (TRADE/MAINSTREAM): The Record tied BYOD's rise to reports of AI-fueled ransomware growth; Halcyon counted a 40% rise from July to September.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): HN posts on Vanderbilt drew under 10 points; one repeated BYOD's claim of "over 1M" records (see Quarantined).
- CONFIDENCE: HIGH on company statements. LOW on BYOD's data claims and on Mittwald's AI attribution.

## GAME PRESERVATION AND PIRACY

## ITEM 13: Football Manager 27 Launches Today with a Denuvo Bypass Already Out

- WHAT / WHERE / WHEN: Sports Interactive's Football Manager 27 launches 10 NOV. The ARTIFACT group's hypervisor-based Denuvo bypass, released around 04 NOV during the pre-launch window, means the full game is effectively pirated on day one; CrackWatcher lists FM27 as cracked by hypervisor bypass. CrackWatcher also lists recent bypasses for Phantom Blade Zero, Star Wars: Galactic Racer and Final Fantasy Resonance. No statement from Sports Interactive or Sega on the bypass was found.
- IMPACT ASSESSMENT: Denuvo's launch-window protection failed for a major release. Hypervisor bypasses need the system's protections lowered below the operating system, so they are a high-risk install on any PC you care about.
- ACTION FOR ADMINS: None (consumer). On managed endpoints, block unsigned drivers and keep HVCI on.
- SOURCE SYNOPSIS: Football Manager official site and Steam store (search titles); VGTimes and games-man.ru (04 NOV); CrackWatcher (search summary). r/CrackWatch was not checked.
- FRAMING (TRADE/MAINSTREAM): VGTimes headline: "cracked ahead of launch."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Tracker sites only; Reddit not checked.
- CONFIDENCE: MODERATE (enthusiast trackers; no publisher confirmation).

## ITEM 14: Shutdowns and Delistings — Destruction AllStars Offline 25 NOV at 0900 CST; Growtopia PC Delisting 01 DEC; Several Steam Removals

- WHAT / WHERE / WHEN: Destruction AllStars' remaining server support ends 25 NOV at 1500 UTC (0900 CST). Multiplayer is already gone; arcade challenges may stay playable, but Sony says functionality could be affected (PlayStation server-support page via search; Polygon, VGC). PlayStation LifeStyle (09 NOV) reconfirmed that Hotel Transylvania 3: Monsters Overboard and Avatar: The Last Airbender – Quest for Balance leave the PS Store at the end of December because licenses are expiring. Delisted Games logged new removals: TrollMaker shuts down 16 NOV, less than eight months after launch; Ubisoft's Growtopia leaves PC storefronts 01 DEC; Asterism: Apex of War is leaving Steam because HorseFeathers is closing; Whale Captain is leaving temporarily; and two free games, Battle Sweeper and Sadball, are leaving Steam.
- IMPACT ASSESSMENT: More online-dependent games are becoming unplayable. Single-player delistings keep existing purchases; server shutdowns do not.
- ACTION FOR ADMINS: None. Claim the free titles before removal if you want them; buy the licensed titles before 31 DEC.
- SOURCE SYNOPSIS: Delisted Games (09–10 NOV, read directly); PlayStation LifeStyle (09 NOV, read directly); PlayStation, Polygon, VGC, Game Developer (search excerpts).
- FRAMING (TRADE/MAINSTREAM): Delisted Games' tagline: "Even in the age of digital, nothing lasts forever."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked this run.
- CONFIDENCE: HIGH.

## EMULATION

## ITEM 15: Nintendo DMCA Takes Down Citron NEO and 70 Forks on GitHub; Eden and Switch 2 Forks Not Named

- WHAT / WHERE / WHEN: GitHub published two Nintendo DMCA notices dated 06 NOV on 09 NOV. The first, committed at 1728 UTC (1128 CST), names `citron-neo/emulator`. Because the repo was actively being forked, GitHub processed it "against the entire network of 71 repositories." The second, at 1759 UTC, targets a single Yuzu copy (`IpwnedU/yuzu-mainline-master`). Both use Nintendo's standard 17 U.S.C. 1201 argument (emulators use unauthorized copies of prod.keys) and cite the Tropic Haze (Yuzu) judgment and a 2025 Colorado case. As of 10 NOV, `github.com/citron-neo/emulator` returns 404. LoveGame reports that the listed forks return 451, that the separate `citron-neo/CI` build repo is up but its last nightly is from 06 NOV, and that an unconfirmed copy appeared on a self-hosted Forgejo server. Citron NEO has not commented. Eden, which hosts its own source, and Switch 2 forks such as Eglantine and Lichii do not appear in any published notice.
- IMPACT ASSESSMENT: This is Nintendo's first GitHub action since the Switch 2 fork surge, but it hit a Switch 1 emulator. Installed copies still work. Fake download sites usually follow takedowns.
- ACTION FOR ADMINS: None. Download builds only from a project's verified home; treat "Citron NEO mirror" sites as malware risks.
- SOURCE SYNOPSIS: GitHub DMCA repository notices 2026-11-06-nintendo-3 and -4 (read directly, with commit timestamps); direct HTTP check of the repo (404); LoveGame (10 NOV, read directly; enthusiast site).
- FRAMING (TRADE/MAINSTREAM): LoveGame: "The August sweep skipped Citron NEO. This time it was the main target."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Little reaction found on X in the sample searched; r/emulation and r/yuzu were not checked.
- CONFIDENCE: HIGH on the notice and takedown. MODERATE on fork and CI status details (single enthusiast source).

## ITEM 16: Emulator Releases — PCSX2, Xenia and shadPS4 Nightlies; Dolphin 2609b Still Current

- WHAT / WHERE / WHEN: On 09 NOV, PCSX2 posted pre-release builds v2.9.166 through v2.9.168, with x64 profiler and graphics fixes. Xenia updated to v1.0.2844, Xenia Edge had a 09 NOV Git build, and shadPS4 posted two pre-release builds. Dolphin's latest is still 2609b (08 NOV, with savestate and FIFO hardening). RPCS3's last tagged build is v0.0.43 Alpha (30 SEP).
- IMPACT ASSESSMENT: Routine. Updating to Dolphin 2609b is still the security-relevant step from 09 NOV.
- ACTION FOR ADMINS: None beyond keeping Dolphin on 2609b or later.
- SOURCE SYNOPSIS: PCSX2 and RPCS3 GitHub releases, Emu-France "Mini sac de GIT" (09 NOV) and whatsnew.fyi (search excerpts only).
- FRAMING (TRADE/MAINSTREAM): Routine.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: MODERATE (search summaries; release pages not opened).

## PATCH AND KEV WATCH

- NEW KEV, added 09 NOV, federal due 12 NOV (forensic triage required): CVE-2026-123158 OpenSSH "SSHole" (fix 10.6p2); CVE-2026-102895 GPUStack (fix 2.2.0); CVE-2026-116779 SignalWire FreeSWITCH (fix 1.11.3); CVE-2026-123218 IBM Aspera Faspex (fix 5.0.19 PL1).
- KEV due this week (verified against the CISA feed): Adobe Commerce/Magento CVE-2026-48356 and Google Brotli CVE-2026-111497, due 10 NOV (today); VMware ESX CVE-2026-41709, due 11 NOV; Ivanti Connect Secure CVE-2026-118527, due 13 NOV.
- KEV due next week: Apple CVE-2024-27834, due 18 NOV; SonicWall CVE-2026-19868, due 20 NOV.
- Past due: WordPress Core CVE-2026-119977 (06 NOV); Ivanti CVE-2026-111357 (02 NOV); Cisco ASA/FTD CVE-2026-76418 and GitLab CVE-2026-97229 (01 NOV); Linux kernel CVE-2026-46300 (31 OCT).
- Exploited, not in KEV: Chrome CVE-2026-125350 (fix 157.0.8103.50/.51); WP Duplicate CVE-2026-123751 (no patch, remove it); N-able N-central Able2Shell (no CVEs, no patch; honeypot attempts).
- Critical patches today: SAP CVE-2026-76964, CVE-2026-89126, CVE-2026-89103 and CVE-2026-120017 (all CVSS 10.0); Firefox 160 / ESR 153.7 / ESR 115.45. Microsoft Patch Tuesday is pending at 1200 CST; Adobe's November bulletins were not checked this run.
- Pending fixes: Ubuntu LTS kernels for CVE-2026-98432 (work in progress); N-able hotfix (ETA midday ET 10 NOV).
- End of support today: .NET 8, .NET 9; Windows 11 23H2 Enterprise/Education final update (per secondary source).

## OPEN THREADS CARRIED FORWARD

- OpenSSH SSHole CVE-2026-123158: moved into KEV 09 NOV (due 12 NOV); confirmed breaches with credential theft and persistence. Track exposure counts once Shodan tags it.
- SonicWall CVE-2026-19868: KEV due 20 NOV; no new vendor details or indicators.
- WP Duplicate CVE-2026-123751: still unpatched; not in KEV.
- Microsoft Patch Tuesday 10 NOV: pending at 1200 CST. Cover zero-days, KEV additions and r/sysadmin breakage reports in the 11 NOV IT daily.
- APT CVE-2026-109518: fixed since 04 NOV; no exploitation reported. Ubuntu kernel CVE-2026-98432 is still unfixed on LTS.
- Nvidia / Jensen Huang: escalated to FBI interest per Trump and a securities class action; earnings 17 NOV.
- NoName057(16) doxxing of 18 European officials: no new developments found this run.
- Football Manager 27 Denuvo bypass: game launches today, bypass already out.
- Destruction AllStars: full shutdown 25 NOV at 0900 CST.
- Switch 2 Eden forks: still not named in any public Nintendo DMCA notice; the Citron NEO takedown shows Nintendo is active on GitHub again.
- New: N-able Able2Shell hotfix and restore guidance; whether CVEs and a KEV entry follow; any confirmed MSP compromises.
- New: Chrome CVE-2026-125350 KEV status and Edge patch.

## UNCONFIRMED / QUARANTINED

- BYOD ransomware claims about Vanderbilt: "Over 1 Million SSNs," full domain-controller takeover, and encrypted databases. These come from the leak site and ransom note and are not confirmed by the university.
- The full count of 33 Able2Shell vulnerabilities is the researcher's claim; not all have been independently verified. N-able has confirmed only that it is building a hotfix.
- Mittwald's suggestion that the attacker used AI rests only on log timing.
- Espionage allegations against Alice Huang rest on anonymous US intelligence sourcing; China denies them.
- An AI-generated "predicted" news page (next-edition.com) claimed Microsoft patched an exploited Windows zero-day today. It is fabricated and was excluded.
- Self-hosted Forgejo copy of Citron NEO: its existence is reported by LoveGame; the team has not confirmed it.

## GAPS AND NOTES

- Microsoft Patch Tuesday was not released by cutoff. Note for the record: the release time is 10:00 a.m. PT, which is 1200 CST, not 1000 CST. Adobe's Patch Tuesday bulletins were not checked.
- BleepingComputer article pages returned 403 to the fetch tool; details come from search excerpts. The N-able status page (uptime.n-able.com) could not be read directly.
- Reddit (r/sysadmin, r/msp, r/netsec, r/emulation, r/Piracy, r/CrackWatch), Slashdot and lobste.rs were not searched; the Reddit JSON endpoint returned an HTML block page. Community framing comes from Hacker News (Algolia) and targeted X searches.
- Correction to the 09 NOV IT daily: the "older KEV items" it marked as unverified (Adobe Commerce, Brotli, VMware ESX, Ivanti) are now verified against the CISA feed with the due dates listed above.
- OpenAI items (a "Control Room" product page and ChatGPT Enterprise on AWS Marketplace) appeared in search, but the OpenAI page returned 404, so they are excluded. Apple, Amazon, Meta, xAI, Intel, AMD, Cisco, Broadcom, Oracle, Valve and Sony had no verified major items in the window.
- Football Manager 27 crack status comes only from tracker sites; neither r/CrackWatch nor the publisher was checked.

UNCLASSIFIED // FOR INFORMATIONAL USE  
