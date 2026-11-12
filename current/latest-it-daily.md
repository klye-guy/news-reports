---
title: "Daily IT and Cybersecurity Intelligence Summary — 2026-11-12"
type: it-daily
date: 2026-11-12
dtg: "120745 CST NOV 26"
period: "2026-11-11 ~0745 CST to 2026-11-12 ~0745 CST"
classification: "UNCLASSIFIED // FOR INFORMATIONAL USE"
tags: [it-daily, cybersecurity, sysadmin, ConnectWise, ScreenConnect, SCKit, RMM-Plus, Labtech-Plus, Huntress, MSP, Apache, httpd, mod_http2, CVE-2026-119618, mod_md, CVE-2026-106023, httpd-2.4.71, Vates, Xen-Orchestra, XCP-ng, Microsoft, KB5132061, KB5127936, Windows-11, Nvidia, Jensen-Huang, Kimberly-Powell, Colette-Kress, Megaspeed, Wachtell, Anthropic, IPO, Apple, Apple-Support-Community, iOS, worse_query, AWS, AWS-Emulator, Google, Gemini, CarPlay, Maersk, WhiteArmor, LF-Logistics, Notion, Fireworks-AI, Vanderbilt, BYOD-ransomware, Texas-HHSC, Poland, ePUAP, eMudhra, CISA-KEV, Barracuda, CVE-2026-116606, CVE-2026-111560, OpenSSH, SSHole, CVE-2026-123158, Outlook, CVE-2026-124194, Chrome, CVE-2026-125350, Cisco-BroadWorks, CVE-2026-20320, N-able, N-central, Humble-Bundle, 2FA, Ziff-Davis, TorrentFreak, Destruction-AllStars, PlayStation-delistings, Nintendo, DMCA, Picofly, Eden, Switch-2]
---

UNCLASSIFIED // FOR INFORMATIONAL USE  

DAILY IT AND CYBERSECURITY INTELLIGENCE SUMMARY  
DTG: 120745 CST NOV 26 (America/Chicago)  
PERIOD COVERED: ~0745 hours CST 11 NOV 26 through ~0745 hours CST 12 NOV 26 (CT)  
PREPARED FOR: Kyle Sibley  
CLASSIFICATION: UNCLASSIFIED // FOR INFORMATIONAL USE  

## EXECUTIVE SUMMARY

The top admin story is an active attack on MSPs through ScreenConnect. Starting at 1147 CST Wednesday, attackers used ScreenConnect's Run Command feature on cloud-hosted panels to push rogue ScreenConnect clients and a 16-file toolkit Huntress calls SCKit to at least 288 endpoints across 48 organizations in about 90 minutes. Huntress ties it to RMM+, a third-party extension whose versions 1.0.31 and 1.0.32 accept a blank access key when none was configured, which bypasses ScreenConnect logins and MFA. ConnectWise disabled five RMM+-family extensions in about 400 partner environments, says ScreenConnect itself is not vulnerable, and told partners not to open interactive sessions to suspect machines, because SCKit tries to infect the technician who connects. Apache shipped httpd 2.4.71 on 11 NOV fixing a critical mod_http2 remote code execution bug (CVE-2026-119618) in 2.4.55 through 2.4.70 when HTTP/2 is on; it was found by Anthropic's open-source scanner and by Google researchers. Vates warned that an unauthenticated Xen Orchestra authentication bypass and a second, still-unpatched zero-day are being exploited to take over XCP-ng hosts. Microsoft confirmed KB5132061 install failures on PCs that took the October preview update and is pushing an automatic repair. CISA added nothing to KEV on Veterans Day; the four 09 NOV entries, including OpenSSH SSHole, are due today, and Barracuda is due tomorrow. In big tech, Nvidia's board met Wednesday night on whether to remove Jensen Huang after a second reported affair, this one with an Nvidia vice president; shares fell more than 9% after hours and no decision had been announced early today. For gamers, Humble Bundle's redesigned site dropped two-factor login and password-change checks.

## BIG TECH

## ITEM 1: Nvidia — Board Meets on Ousting Jensen Huang After Second Reported Affair; Shares Down 9% After Hours; No Decision Announced

- WHAT / WHERE / WHEN: Late Wednesday, 11 NOV, The Wall Street Journal reported that Nvidia's board was preparing to oust CEO Jensen Huang, minutes after The New York Times reported he had a romantic relationship with Kimberly Powell, Nvidia's vice president of health care, who has led that group since 2017. CNBC confirmed the board was meeting and that the meeting stretched into the evening. Nvidia shares fell more than 9% in after-hours trading (CNBC) and were down about 6% premarket Thursday (Washington Post). Semafor and a Reuters report carried by Investing.com say some directors favored CFO Colette Kress as interim CEO. AP reports Megaspeed, the Singapore data-center company where Alice Huang (the alleged Chinese intelligence asset in the first affair) was an executive, pledged Thursday to cooperate with the US probe. As of early Thursday there was no announcement from Nvidia. Earnings remain scheduled for 17 NOV.
- IMPACT ASSESSMENT: Still no product, driver or supply effect. A forced CEO change at the company that supplies most AI accelerators would be the biggest leadership shock in the industry in years; for admins and gamers the near-term effect is market turbulence, not hardware.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: CNBC (11 NOV, updated 0011 CST 12 NOV, read directly); Washington Post and AP (12 NOV, search excerpts; AP page opened but body did not load); Semafor and Investing.com/Reuters (search excerpts). The WSJ and NYT stories were not read directly (paywalled).
- FRAMING (TRADE/MAINSTREAM): CNBC framed it as the board deciding "Huang's fate" and noted the stock was already on pace for a sixth straight weekly slide on AI-buildout worries.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): The WSJ story was the top Hacker News post of the day (1,128 points, 1,506 comments), and the NYT story drew 381 points and 479 comments. A Tom's Hardware post claiming Alice Huang helped move 240,000 banned chips into China got little traction (19 points).
- CONFIDENCE: HIGH that the board met and on the share moves. MODERATE on Kress as interim (anonymous sourcing). LOW on the espionage allegations themselves (anonymous intelligence sourcing; China denies).

## ITEM 2: Big Tech Briefs — Anthropic IPO Range Set; Apple Closing Its Support Community 20 NOV; AWS Ships a Local Emulator; Gemini on CarPlay

- WHAT / WHERE / WHEN: Anthropic's amended S-1 (filed 10 NOV) sets an IPO of 825 million Class A shares at $70 to $78, to trade on Nasdaq as ANT; TechCrunch puts the implied valuation at $1.404 trillion, and Anthropic says its roadshow has launched. Apple's Support Community forum, running for 28 years, is now read-only and closes permanently 20 NOV (The Verge, Ars Technica, TechRadar). AWS released AWS Emulator, a free tool for building and testing AWS applications locally without an account or deployment. Google brought Gemini to Apple CarPlay.
- IMPACT ASSESSMENT: The Apple forum closure removes a large archive of user-sourced troubleshooting for Macs and iPhones; admins who rely on it for obscure fixes lose that resource after 20 NOV unless it is archived elsewhere. AWS Emulator could cut test costs for teams working with AWS.
- ACTION FOR ADMINS: Save any Apple Support Community threads you rely on before 20 NOV.
- SOURCE SYNOPSIS: SEC EDGAR S-1/A, TechCrunch and Anthropic newsroom (search excerpts); The Verge, Ars Technica and TechRadar (search titles and summaries); AWS What's New and Google blog (search titles and summaries).
- FRAMING (TRADE/MAINSTREAM): TechRadar: Apple "pulls the plug" on a hub for iPhone and Mac advice.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): On HN, AWS Emulator drew 888 points and 247 comments, the Anthropic IPO page 157 points and 177 comments, and the Apple forum story 256 points.
- CONFIDENCE: HIGH (company filings and announcements), though read through excerpts.

## SYSADMIN

## ITEM 3: Apache httpd 2.4.71 Fixes Critical mod_http2 RCE (CVE-2026-119618), Found by Anthropic's Scanner and Google

- WHAT / WHERE / WHEN: The Apache HTTP Server project released 2.4.71 on 11 NOV with three fixes. The critical one, CVE-2026-119618, is a race condition in mod_http2's `assign_headers()` that corrupts shared heap memory and can lead to remote code execution. It affects httpd 2.4.55 through 2.4.70 and standalone mod_h2 2.0.8 through 2.0.42, and only matters when HTTP/2 (h2 or h2c) is enabled. Apache credits Anthropic's OSS Scanner (reported 26 OCT) and Anthony Weems and Simon Scannell of Google Cloud Vulnerability Research (reported 03 NOV). The release also fixes CVE-2026-106023 (important), a mod_md NULL pointer dereference that crashes a child process, affecting 2.4.30 through 2.4.70. The Hacker News and Red Hat describe it as unauthenticated. No exploitation was reported in the sources reviewed.
- IMPACT ASSESSMENT: Apache with HTTP/2 enabled is common on internet-facing web servers and reverse proxies, so this is a high-priority patch even without known exploitation. Distribution packages will lag the upstream release.
- ACTION FOR ADMINS: Upgrade to httpd 2.4.71 or your distribution's patched package. Until then, disable HTTP/2 by setting `Protocols http/1.1` on exposed virtual hosts. Check appliances and containers that bundle Apache.
- SOURCE SYNOPSIS: Apache httpd 2.4 vulnerabilities page (read directly); Red Hat CVE page and Bugzilla, GitHub Advisory Database and The Hacker News (search excerpts); Wiz blog (HN link, not opened).
- FRAMING (TRADE/MAINSTREAM): The Hacker News: "Critical Apache HTTP/2 Flaw Could Let Unauthenticated Attackers Execute Code Remotely."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): The Wiz write-up drew 260 points and 124 comments on HN.
- CONFIDENCE: HIGH.

## ITEM 4: Microsoft Confirms KB5132061 Install Failures on PCs That Took the October Preview; Automatic Repair Rolling Out

- WHAT / WHERE / WHEN: Microsoft acknowledged that November's Windows 11 update KB5132061 can fail with errors 0x80070306, 0x800f0989 or 0x800f0993, mainly on devices that installed October's optional preview update KB5127936. It is rolling out an automatic repair that should reach affected devices using Windows Update within 24 to 48 hours of 1200 CST 11 NOV, after which KB5132061 installs on its own. The community workaround of disabling Windows Sandbox, restarting and retrying still circulates (`Disable-WindowsOptionalFeature -Online -FeatureName Containers-DisposableClientVM`).
- IMPACT ASSESSMENT: This leaves a pocket of unpatched machines during a month with an exploited Outlook bug and several critical Windows bugs. Machines patched through WSUS or other tools may not get the repair the same way as consumer Windows Update.
- ACTION FOR ADMINS: Check compliance for these three error codes. Give Windows Update-managed devices until about 13 NOV to self-repair; for WSUS/ConfigMgr-managed devices, follow Microsoft's release-health guidance or test the Sandbox workaround on a pilot machine.
- SOURCE SYNOPSIS: BleepingComputer, Windows Latest, Windows Report and the Microsoft KB page (search excerpts; BleepingComputer returned 403); Neowin and Pureinfotech (search excerpts).
- FRAMING (TRADE/MAINSTREAM): BleepingComputer: "Microsoft confirms Windows security updates installation issues."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked (Reddit blocked automated reads this run).
- CONFIDENCE: HIGH that Microsoft confirmed the issue. MODERATE on the exact repair window wording (secondary sources).

## CYBERSECURITY

## ITEM 5: Active ScreenConnect Campaign Hits MSPs — Rogue Clients and SCKit on 288+ Endpoints via RMM+ Extension; ConnectWise Disables Five Extensions in ~400 Environments

- WHAT / WHERE / WHEN: At about 1147 CST (1747 UTC) on 11 NOV, attackers began using ScreenConnect's Run Command feature on cloud-hosted MSP panels to install attacker-controlled ScreenConnect clients and SCKit, a 16-file toolkit for persistent access, on managed endpoints. Huntress counts at least 288 endpoints across 48 organizations, all hit within 90 minutes; BleepingComputer's earlier count was six compromised MSPs. Affected ScreenConnect versions include the current 26.6.6.9747 and 26.7.6.9783. Huntress links the activity to RMM+, a third-party extension that lets other tools send commands through ScreenConnect: versions 1.0.31 and 1.0.32 accept a blank access key if the administrator never set one, and because RMM+ runs outside ScreenConnect's user accounts, commands arrived with no matching login, bypassing MFA. SCKit also tries to infect technicians who connect to an infected machine, stealing session cookies and pushing malware back to their workstation. Sequential victim tags suggest earlier, undetected victims; BleepingComputer found a rogue client ID referenced in a malicious script uploaded to VirusTotal on 25 JUL. ConnectWise's advisory (latest update 2045 CST 11 NOV) says it found no compromise of its infrastructure and no ScreenConnect vulnerability, and it disabled Labtech Plus, RMM Plus, RMM+, RMM Plus Password Link and RMM+ Password Link in about 400 partner environments where it could. On-prem partners must disable them themselves. Initial access and full scope remain under investigation; no CVE has been assigned.
- IMPACT ASSESSMENT: This is the most significant MSP supply-chain event since the N-central dump last weekend, and it is active. Any organization whose MSP uses ScreenConnect should assume exposure until told otherwise. Running the latest ScreenConnect does not protect you if the extension is installed.
- ACTION FOR ADMINS: If you run ScreenConnect, remove or disable all five RMM+-family extensions now and do not reinstall them. Review Run Command history back to at least July, even without alerts. Look for unknown ScreenConnect clients and installs on endpoints. Do not open interactive ScreenConnect sessions to suspect machines; investigate with separate tools. Revoke active sessions, reset credentials from a clean device and verify MFA. If an MSP manages you, ask today whether they use ScreenConnect with these extensions.
- SOURCE SYNOPSIS: The Register (12 NOV, full text in search result); ConnectWise Trust Center advisory and partner guidance blog (search excerpts); Huntress blog (search excerpt); BleepingComputer (search excerpt).
- FRAMING (TRADE/MAINSTREAM): The Register: "Hackers exploiting ScreenConnect plugin flaw to spread malware across hundreds of PCs." ConnectWise stresses that the 400 environments had the extension installed and are not necessarily compromised.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Huntress first raised the alarm in a Reddit post. An X trending summary notes Sophos is also tracking the spread (not confirmed elsewhere). No HN story in the window.
- CONFIDENCE: HIGH on the campaign and ConnectWise's actions. MODERATE on RMM+ as the root cause (Huntress's assessment; ConnectWise says it is still validating).

## ITEM 6: Xen Orchestra Authentication Bypass and a Second Zero-Day Exploited to Take Over XCP-ng Hosts; Fix for the Zero-Day Still Pending

- WHAT / WHERE / WHEN: Vates warned on 11 NOV that a threat actor is exploiting a critical authentication bypass in Xen Orchestra's REST authentication, in which a malformed token leads the server to return the first stored login token, giving an unauthenticated attacker administrator access and, from there, code execution on managed pools and root on XCP-ng nodes. It affects Xen Orchestra before 6.9.2 (stable) and 6.10.1 (latest) and the Xen Orchestra Appliance. The same actor is also using an unpatched zero-day that needs admin rights and abuses malicious VM imports to compromise hosts. The attacker operated from 91.211.251.112:8001 and through Tor. No CVEs are assigned, and Vates says unauthorized access is not logged.
- IMPACT ASSESSMENT: XCP-ng and Xen Orchestra are popular VMware alternatives in homelabs and small to mid-size shops after Broadcom's licensing changes. Compromise of the management plane means every VM in the pool is at risk, and the missing logs make detection hard.
- ACTION FOR ADMINS: Upgrade Xen Orchestra to 6.9.2 or 6.10.1 now. Keep it on a dedicated management network with no internet exposure, block the listed IP, add a WAF rule rejecting the empty token if you front it with one, and rotate credentials. Avoid importing VMs from untrusted sources until the zero-day is fixed. If compromised, Vates recommends a full reinstall.
- SOURCE SYNOPSIS: SecurityWeek (11 NOV, full text in search result), citing Vates's advisory, which was not opened.
- FRAMING (TRADE/MAINSTREAM): SecurityWeek: "Critical Xen Orchestra Flaws Exploited in Attacks."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): No HN traction found; other forums not checked.
- CONFIDENCE: HIGH (vendor advisory via SecurityWeek).

## ITEM 7: Incidents — Maersk Confirms Breach of Legacy LF Logistics System; Notion Says AI Chat Transcripts Exposed; Vanderbilt Expects Weeks to Restore; Poland Takes ePUAP Offline

- WHAT / WHERE / WHEN: Maersk confirmed on 11 NOV unauthorized access and data extraction from a local legacy system inherited from an acquisition, says no sensitive data appears to have been disclosed, and expects no operational disruption. WhiteArmor listed Maersk over the weekend, claims about 100 GB from the OCF/LF Logistics platform and demands $5 million. Notion says Fireworks AI's breach exposed Notion AI chat transcripts from its Insights dataset in a small number of workspaces, mostly unattributable to users; it says fewer than 1% of users are affected and advises rotating any passwords or keys entered into affected chats. Vanderbilt said in a 10 NOV evening update that full restoration will take multiple weeks and it is still determining what data was accessed; Texas HHSC said it is aware of BYOD's claims, is working with Texas Cyber Command and federal partners, and that the claims are unverified. Poland temporarily shut down ePUAP, its national e-government platform, after detecting and stopping an attack; officials say it was a precaution and no compromise is confirmed.
- IMPACT ASSESSMENT: The Notion disclosure confirms that data sent to third-party AI providers through SaaS features can leak, including secrets people paste into chats. Maersk's breach is limited to a legacy subsidiary system by its own account.
- ACTION FOR ADMINS: Notion workspace owners should check Security incident review in the desktop or web app and rotate any credentials that were ever pasted into Notion AI chats. Treat legacy systems from acquisitions as a priority for isolation or retirement.
- SOURCE SYNOPSIS: BleepingComputer and Security Affairs (search excerpts) for Maersk and Notion; Inside Higher Ed, Breach Signal and Tx Cyber Net (search excerpts) for Vanderbilt and HHSC; The Record (11 NOV, read directly) for Poland.
- FRAMING (TRADE/MAINSTREAM): Security Affairs noted WhiteArmor's justification that $5 million is "roughly four hours of revenue."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH on company and government statements. LOW on WhiteArmor's and BYOD's data claims (see Quarantined).

## ITEM 8: iOS "worse_query" Sandbox Escape Is Public With No Confirmed Fix; eMudhra Revokes Eight More Intermediate CAs

- WHAT / WHERE / WHEN: A public proof of concept called worse_query (GitHub `forcequitOS/worse_query`) shows an iOS sandbox escape: an app with an App Group container swaps its Library/Caches directory for a symlink, then asks containermanagerd for a sandbox token, which it grants for the symlink's target without checking it stays inside the container. Ostorlab says it affects iOS 26.0 through 26.7.2 and 27.2 and can reach other apps' data containers and, on iOS 27, some system paths. Binance warned it could expose crypto wallet keys; Security Affairs and The Hacker News report Apple has not confirmed a fix. Separately, certificate authority eMudhra revoked eight more RSA intermediate CA certificates on 07 NOV, bringing the total to 16, after finding it never checked key strength during generation; some of the new eight issued TLS and code-signing certificates from May 2026 to 03 NOV.
- IMPACT ASSESSMENT: worse_query needs a malicious app on the device, so risk is highest with sideloaded or untrusted apps. It matters for managed iPhones holding corporate data. eMudhra customers' certificates have been replaced, per the company.
- ACTION FOR ADMINS: Limit app installs on managed iOS devices to vetted apps, watch for an Apple update, and update promptly when one ships. Check for any eMudhra-issued certificates in your environment.
- SOURCE SYNOPSIS: Ostorlab, GitHub repo, The Hacker News and Security Affairs (search titles and excerpts); BleepingComputer on eMudhra (search excerpt).
- FRAMING (TRADE/MAINSTREAM): Security Affairs: "iOS Sandbox Escape Is Public, and Apple Hasn't Confirmed a Fix."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): An X trending summary links the flaw to reported losses of $15,000 and $85,000 from iPhone wallets (see Quarantined).
- CONFIDENCE: MODERATE (technical details from the researcher and a security firm; Apple has not commented in sources reviewed).

## ITEM 9: KEV Status — No Additions on Veterans Day; SSHole and Three Others Due Today, Barracuda Tomorrow

- WHAT / WHERE / WHEN: The CISA KEV catalog was still at version 2026.11.10 at about 0725 CST today; nothing was added on 11 NOV, a federal holiday. Due today, 12 NOV: OpenSSH SSHole CVE-2026-123158, GPUStack CVE-2026-102895, FreeSWITCH CVE-2026-116779 and IBM Aspera Faspex CVE-2026-123218. Due tomorrow, 13 NOV: Barracuda CVE-2026-116606 and CVE-2026-111560, and Ivanti Connect Secure CVE-2026-118527.
- IMPACT ASSESSMENT: No change in risk; the deadlines are the news. Expect a larger KEV update once CISA returns from the holiday.
- ACTION FOR ADMINS: Finish OpenSSH 10.6p2 or later and the other 12 NOV items today. Confirm Barracuda appliances are patched and admin UIs are off the internet before tomorrow.
- SOURCE SYNOPSIS: CISA KEV JSON (read directly); prior IT dailies.
- FRAMING (TRADE/MAINSTREAM): No new coverage.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: HIGH.

## GAME PRESERVATION AND PIRACY

## ITEM 10: Humble Bundle's Redesigned Site Drops Two-Factor Login and Password-Change Checks

- WHAT / WHERE / WHEN: Humble Bundle's new site, launched this week, has no two-factor authentication: users cannot enable it, and accounts that had it can log in with only an email and password (PC Gamer, 12 NOV, confirmed on the writer's own account). Kotaku and others report password changes no longer require the current password and email changes lack confirmation. Humble's FAQ still recommends 2FA. Humble had not responded to PC Gamer as of publication. Some users report they cannot remove saved payment details.
- IMPACT ASSESSMENT: Accounts hold saved cards and unredeemed game keys, which are easy to resell. With 2FA gone and password-change checks removed, a reused password is enough for a takeover.
- ACTION FOR ADMINS: For Kyle personally: change the Humble password to a unique one, redeem any outstanding keys, and remove saved payment methods if the site allows it until 2FA returns.
- SOURCE SYNOPSIS: PC Gamer (12 NOV, read directly); Kotaku and Frandroid (search titles and excerpts).
- FRAMING (TRADE/MAINSTREAM): PC Gamer: "I recommend removing your saved payment details, at least for now." Kotaku called the redesign "vibecoded-looking."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): The SpaceBattles thread "Humble Bundle just completely killed most of their security through vibecoding" reached 307 points and 188 comments on HN. Users on r/humblebundle (quoted by PC Gamer) called it "insanely bad." An X summary notes game creator Kenney criticized the change and points to owner Ziff Davis for a fix.
- CONFIDENCE: HIGH on the missing 2FA. MODERATE on the password and email-change details (secondary reports). The "vibe-coded" cause is speculation.

## ITEM 11: Preservation and Piracy Briefs — PS5 Delistings Through Year-End; Destruction AllStars 25 NOV; Lawsuit Over Fake Meta Takedowns

- WHAT / WHERE / WHEN: Push Square lists eight or more PS5 games being delisted in November and December, including Avatar: The Last Airbender: Quest for Balance, Hotel Transylvania 3: Monsters Overboard and Street Outlaws titles on 31 DEC; NBA 2K25 servers end 31 DEC and Zenith: Nexus 18 DEC. Destruction AllStars online support still ends 25 NOV. TorrentFreak reports a lawsuit against a "copyright-strike-for-hire" service accused of filing fake takedowns with Meta (headline only).
- IMPACT ASSESSMENT: Buy wanted titles before 31 DEC delistings; purchased copies generally remain downloadable, but online modes end.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: Push Square and PlayStation server page (search summary); TorrentFreak archive (read directly; article not opened).
- FRAMING (TRADE/MAINSTREAM): Routine.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked.
- CONFIDENCE: MODERATE (search summaries).

## EMULATION

## ITEM 12: No New Takedowns or Major Releases; Coverage of Nintendo's Picofly Notice Spreads

- WHAT / WHERE / WHEN: No new Nintendo DMCA notices or emulator lawsuits were found in the window. Coverage of the 06 NOV Picofly modchip-firmware notice (144 repos disabled) spread to VGC, Nintendo Everything and Tom's Hardware, which called it a "DMCA wave" following the Team-Xecuter criminal case. Switch 2 forks such as Eden NX2 and Eglantine remain unstable prereleases and are not named in any notice. No significant new Dolphin, RPCS3, shadPS4 or Xenia releases were found beyond routine development builds.
- IMPACT ASSESSMENT: Quiet day. The open question is whether Nintendo's next notices reach the Switch 2 forks.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: TorrentFreak (11 NOV, covered yesterday), VGC and Nintendo Everything (search titles); Tom's Hardware (HN link title); LoveGame and Retro Replay roundups (search summaries).
- FRAMING (TRADE/MAINSTREAM): VGC: "Nintendo's battle against piracy continues."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): The Tom's Hardware and TorrentFreak posts each got 2 to 3 points on HN. r/emulation and GBAtemp were not checked.
- CONFIDENCE: MODERATE.

## PATCH AND KEV WATCH

- NEW KEV: none on 11 NOV (catalog still 2026.11.10 at ~0725 CST 12 NOV).
- KEV due today, 12 NOV: OpenSSH CVE-2026-123158 (SSHole), GPUStack CVE-2026-102895, FreeSWITCH CVE-2026-116779, IBM Aspera Faspex CVE-2026-123218.
- KEV due 13 NOV: Barracuda CVE-2026-116606 and CVE-2026-111560 (ESG 9.4.0.030+), Ivanti Connect Secure CVE-2026-118527.
- KEV due next week and after: Apple CVE-2024-27834 (18 NOV); SonicWall CVE-2026-19868 (20 NOV); Microsoft Outlook CVE-2026-124194, Chromium CVE-2026-125350, Cisco BroadWorks CVE-2026-20320, Openwave CVE-2026-111793 (24 NOV).
- Exploited, not in KEV: ScreenConnect RMM+ extension abuse (no CVE; disable the five extensions); Xen Orchestra auth bypass (no CVE; 6.9.2 / 6.10.1) and VM-import zero-day (no fix); WP Duplicate CVE-2026-123751 (no patch).
- Critical patches: Apache httpd 2.4.71 (CVE-2026-119618, CVE-2026-106023); Microsoft November (see 11 NOV IT daily) and the KB5132061 repair; Adobe Connect APSB26-191; N-central 2026.4 HF2.
- Pending fixes: Xen Orchestra VM-import zero-day; iOS worse_query (no Apple fix confirmed); N-able follow-up hotfix; Ubuntu kernels for CVE-2026-98432 (not rechecked).

## OPEN THREADS CARRIED FORWARD

- ScreenConnect/SCKit campaign (new): root cause confirmation from ConnectWise, victim count, any CVE.
- Xen Orchestra (new): zero-day fix and CVE assignment.
- Nvidia / Jensen Huang: board decision pending; earnings 17 NOV.
- Microsoft Patch Tuesday: KB5132061 repair rollout; watch for exploitation of Windows Search/Exchange (CVE-2026-116928) and LDAP (CVE-2026-119958).
- N-able Able2Shell: follow-up hotfix pending; no new developments found this run.
- Barracuda ESG exploitation: KEV due 13 NOV; no attribution yet.
- Cisco BroadWorks "Operation Snowball": no new developments found.
- Turla Cereal: no new developments found.
- Vanderbilt / BYOD: multi-week restoration; HHSC claims unverified.
- Fireworks AI / Notion: Notion confirmed chat-transcript exposure.
- SonicWall CVE-2026-19868 (due 20 NOV), WP Duplicate CVE-2026-123751 (unpatched), Ubuntu CVE-2026-98432, NoName057(16) doxxing: not rechecked this run.
- Destruction AllStars shutdown 25 NOV; Football Manager 27 / Denuvo: no change found.
- Nintendo GitHub campaign: no new notices; Switch 2 forks still not named.

## UNCONFIRMED / QUARANTINED

- WhiteArmor's claims about Maersk data (30,000 driver records, plaintext passwords, 33 super-admin accounts, 27,842 device logs) come from the gang; Maersk says no sensitive data appears disclosed.
- BYOD's claims against Vanderbilt (over 1 million SSNs, domain-controller takeover) and Texas HHSC (about 2 million Texans' benefit and banking data) remain leak-site claims; HHSC calls them unverified.
- Reported $15,000 and $85,000 iPhone wallet losses linked to worse_query come from an X trending summary and are not tied to the flaw by any reputable source.
- Sophos tracking the ScreenConnect campaign appears only in an X summary.
- Colette Kress as Nvidia interim CEO and the WSJ ouster report rest on anonymous sources; Nvidia had announced nothing as of early 12 NOV.
- The "vibe-coded" explanation for Humble Bundle's redesign is community speculation.

## GAPS AND NOTES

- Reddit blocked automated reads this run, so r/sysadmin, r/msp, r/netsec, r/emulation, r/Piracy and r/CrackWatch were not checked; Huntress's Reddit post and r/humblebundle quotes come through The Register and PC Gamer. Slashdot and lobste.rs were not searched. Community framing comes from Hacker News (Algolia) and X news summaries.
- Read directly: CISA KEV JSON, Apache httpd security page, CNBC, PC Gamer, The Record and the TorrentFreak archive. BleepingComputer (403), SecurityWeek, Huntress, ConnectWise, The Hacker News, Ostorlab and others came through search excerpts; The Register and SecurityWeek excerpts included near-full text.
- Correction to the 11 NOV IT daily: it said Microsoft listed no known issues for KB5132061. Microsoft has since confirmed install failures tied to KB5127936 and is rolling out a repair.
- Google (outside Gemini), Intel, AMD, Cisco, Broadcom/VMware, Oracle, Valve, Sony, Meta, OpenAI and xAI had no verified major items in the window.

UNCLASSIFIED // FOR INFORMATIONAL USE  
