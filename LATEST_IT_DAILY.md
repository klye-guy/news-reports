---
title: "Daily IT and Cybersecurity Intelligence Summary — 2026-11-09"
type: it-daily
date: 2026-11-09
dtg: "090740 CST NOV 26"
period: "2026-11-08 ~0730 CST to 2026-11-09 ~0740 CST"
classification: "UNCLASSIFIED // FOR INFORMATIONAL USE"
tags: [it-daily, cybersecurity, sysadmin, Nvidia, Jensen-Huang, MegaSpeed, Microsoft, Oracle, Apple, Siri, iOS-27.3, Patch-Tuesday, KB5127936, Windows-11, APT, CVE-2026-109518, CVE-2026-98432, Ubuntu, Debian, Linux-7.4-rc2, OpenSSH, SSHole, CVE-2026-123158, Alpine, musl, SonicWall, SonicOS, SSLVPN, CVE-2026-19868, CISA-KEV, WordPress, WP-Duplicate, CVE-2026-123751, NoName057(16), doxxing, Iris-Ohyama, WorkOS, ARTEX, AI-agents, Denuvo, ARTIFACT, Football-Manager-27, Onimusha, PlayStation, Destruction-AllStars, NBA-2K25, delisting, Nintendo, Switch-2, Eden, Eglantine, DMCA, Dolphin, shadPS4, RPCS3]
---

UNCLASSIFIED // FOR INFORMATIONAL USE  

DAILY IT AND CYBERSECURITY INTELLIGENCE SUMMARY  
DTG: 090740 CST NOV 26 (America/Chicago)  
PERIOD COVERED: ~0730 hours CST 08 NOV 26 through ~0740 hours CST 09 NOV 26 (CT), with key items from 04–07 NOV carried in because this is the first IT daily  
PREPARED FOR: Kyle Sibley  
CLASSIFICATION: UNCLASSIFIED // FOR INFORMATIONAL USE  

## EXECUTIVE SUMMARY

The top admin action today is OpenSSH "SSHole" (CVE-2026-123158): exploitation in the wild started 06–08 NOV against musl-based, PAM-less systems such as Alpine, OpenWrt, Buildroot and Yocto; update to OpenSSH 10.6p2 and restart sshd, or set PasswordAuthentication no. SonicWall's SSL-VPN SAML/MFA bypass (CVE-2026-19868) is in CISA KEV with a 20 NOV federal due date, and the WP Duplicate WordPress plugin (CVE-2026-123751) is being exploited with no patch, so remove it. Microsoft Patch Tuesday lands tomorrow, 10 NOV. Debian/Ubuntu fixed an APT root-code-execution bug (CVE-2026-109518) on 04 NOV. In big tech, Nvidia shares fell about 5% premarket after its board opened an independent probe into CEO Jensen Huang's relationship with a MegaSpeed executive US intelligence reportedly says spies for China; earnings are 17 NOV. Apple is reportedly accelerating an agentic Siri, and Microsoft is winding down its Oracle AI-capacity rental. Pro-Russian NoName057(16) doxxed 18 European officials. On the gaming side, ARTIFACT bypassed Denuvo on Football Manager 27 before its 10 NOV launch, Destruction AllStars goes fully offline 25 NOV, Switch 2 emulation forks of Eden keep shipping with no GitHub DMCA naming them yet, and Dolphin shipped 2609b with savestate hardening.

## BIG TECH

## ITEM 1: Nvidia — Board Opens Independent Probe of CEO Jensen Huang over Alleged Chinese Intelligence Targeting; Shares Down ~5% Premarket

- WHAT / WHERE / WHEN: Nvidia's board launched an independent investigation after New York Times and Financial Times reports that US intelligence agencies say Alice Huang, an executive at cloud company MegaSpeed, has been passing information to Beijing and that CEO Jensen Huang was the target of a "foreign intelligence effort." Nvidia said Sunday, 08 NOV, that Huang "fully supports the review." In a staff email Huang wrote, "I was unfaithful to my wife... There is no excuse for what I did." Shares were down 5.2% premarket Monday, 09 NOV. China's Foreign Ministry called the "so-called Chinese spy narrative" unsubstantiated (via Reuters). Trump called Huang "an honorable guy." Nvidia reports Q3 earnings 17 NOV (CNBC, 09 NOV).
- IMPACT ASSESSMENT: Leadership uncertainty at the dominant AI-GPU vendor; no product, driver, or supply impact reported. For a gamer and admin, nothing to do now; watch the 17 NOV earnings call and any export-control fallout around MegaSpeed.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: CNBC (09 NOV, read directly); AP, Reuters via Investing.com, Guardian live blog (search headlines).
- FRAMING (TRADE/MAINSTREAM): CNBC quoted Dan Ives calling it a "black eye moment" but saying talk of replacing Huang is "comedy"; Guardian ran it as a "honeytrap" investigation.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): On X, Sequoia's Shaun Maguire called Huang "irreplaceable for America's AI leadership," and Elon Musk reshared the post in agreement (per CNBC). Reddit and HN threads were not checked this run.
- CONFIDENCE: HIGH on the probe, statement, and share move. LOW on the underlying espionage allegation (anonymous intelligence sourcing, denied by China).

## ITEM 2: Microsoft — Winding Down 2023 Deal to Rent AI Cloud Capacity from Oracle

- WHAT / WHERE / WHEN: Bloomberg reported 06 NOV that Microsoft is winding down, and declining to renew, its 2023 agreement to rent AI compute from Oracle, as part of a broader partnership review; the capacity used older-generation Nvidia hardware. Oracle said demand for its infrastructure, including older GPUs, remains strong. Oracle shares fell about 4% on the report (DCD; Reuters via Investing.com).
- IMPACT ASSESSMENT: Signals hyperscalers are pruning older-GPU capacity; no change to Azure or OCI customer services reported. Slightly outside the 24-hour window but carried as context for the first IT daily.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: Bloomberg (06 NOV, headline/search excerpt); DatacenterDynamics, Reuters via Investing.com, Hindu BusinessLine (search excerpts).
- FRAMING (TRADE/MAINSTREAM): Trade press framed it as a capacity-quality decision, not a break in the Microsoft–Oracle relationship.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked this run.
- CONFIDENCE: MODERATE (single original report, widely re-reported; neither company confirmed details on record in what was read).

## ITEM 3: Apple — Reported Push to Make Siri Agentic; First-Party App Control Expected in iOS 27.3, Third-Party Apps in Spring

- WHAT / WHERE / WHEN: The Verge, citing Bloomberg's Mark Gurman, reported 08 NOV that CEO John Ternus is pressing AI chief Craig Federighi to accelerate Siri. Fine-grained control of Apple's own apps (for example cropping in Photos, organizing Safari tabs) is expected in iOS 27.3; third-party app actions (for example Grubhub orders, OpenTable bookings) likely in the spring; longer-running agent behavior possibly next year. The Verge also reported 08 NOV that Apple avoided $2.7 billion in taxes by routing profits through Singapore (headline only).
- IMPACT ASSESSMENT: For managed Apple fleets, expect new Siri/App Intents permission surfaces to review in MDM once iOS 27.3 ships. No dates confirmed by Apple.
- ACTION FOR ADMINS: None now; review Siri and App Intents MDM restrictions when iOS 27.3 betas appear.
- SOURCE SYNOPSIS: The Verge (08 NOV, read directly), relaying Bloomberg/Gurman reporting.
- FRAMING (TRADE/MAINSTREAM): The Verge framed Apple as catching up to rival agents, saying it has "no illusions that it's keeping pace."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked this run.
- CONFIDENCE: MODERATE (single-source roadmap reporting).

## SYSADMIN

## ITEM 4: Microsoft Patch Tuesday Is Tomorrow, 10 NOV; Optional Preview KB5127936 Shows What Rolls In

- WHAT / WHERE / WHEN: Microsoft's November security updates are scheduled for Tuesday, 10 NOV. The optional Windows 11 preview update KB5127936 (25H2 and 26H2) previews non-security changes expected in the November cumulative update, including Cloud Rebuild, customizable File Explorer context menus, Edge accelerated app launch, privacy-control changes, Magnifier improvements, and adaptive hibernation (search excerpts of Microsoft IT Pro blog, PCWorld, Windows Central).
- IMPACT ASSESSMENT: Expect a reboot cycle this week; feature changes such as adaptive hibernation and Cloud Rebuild may need policy review before broad rollout.
- ACTION FOR ADMINS: Schedule a maintenance window for 10–12 NOV; stage the November CU on a pilot ring first; check MSRC on release for any zero-days.
- SOURCE SYNOPSIS: Microsoft Windows IT Pro blog (October roundup, search excerpt); PCWorld, Windows Central, third-party KB explainers (search excerpts). MSRC release notes not yet published.
- FRAMING (TRADE/MAINSTREAM): Coverage framed November as a "fine-tuning" release for Windows 11.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): r/sysadmin's Patch Tuesday megathread will open with the release; not yet available.
- CONFIDENCE: HIGH on the date. MODERATE on the exact feature list (preview contents can change).

## ITEM 5: Linux Servers — APT Root-Code-Execution Fix (CVE-2026-109518) Out Since 04 NOV; Kernel CVE-2026-98432 Fix Still Pending for Ubuntu

- WHAT / WHERE / WHEN: Debian and Ubuntu fixed CVE-2026-109518 in APT on 04 NOV. An attacker controlling a mirror or proxy on plain-HTTP traffic can abuse APT's retry behavior to install an unverified package, giving root code execution; Ubuntu rates it High (CVSS 7.7). Affected: Debian 12 and 13, Ubuntu 22.04 and newer. Fixed versions listed include Ubuntu 22.04 2.4.15ubuntu0.1, 24.04 2.8.4ubuntu0.1, 26.04 3.2.1ubuntu0.1, Debian 12 2.6.2, Debian 13 3.0.4. Separately, the network-reachable kernel bug CVE-2026-98432 (rated 9.8) was still "work in progress" on Ubuntu's tracker for 22.04, 24.04 and 26.04 as of 07 NOV; Debian is fixed and Red Hat points to mitigation bulletin RHSB-2026-016 (Volyte, 07 NOV, citing Ubuntu and Debian trackers).
- IMPACT ASSESSMENT: APT is in every Debian/Ubuntu update path; unattended-upgrades likely already applied it. The kernel item is the bigger exposure for Ubuntu and RHEL-family hosts until fixed kernels ship.
- ACTION FOR ADMINS: Run `apt --version` and confirm fixed versions (use `-o Acquire::Retries=0` while updating if not yet patched). For CVE-2026-98432, keep vendor mitigations in place and re-verify after reboots until fixed kernels ship.
- SOURCE SYNOPSIS: Volyte hosting blog (07 NOV, read directly), which cites the Ubuntu and Debian security trackers and Red Hat RHSB-2026-016. Primary trackers were not opened this run.
- FRAMING (TRADE/MAINSTREAM): Hosting and trade coverage framed APT as "update today" but noted no reported exploitation.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked this run.
- CONFIDENCE: MODERATE (secondary vendor blog; verify fixed versions against the Ubuntu/Debian trackers).

## ITEM 6: Linux 7.4-rc2 Released

- WHAT / WHERE / WHEN: Linus Torvalds released Linux 7.4-rc2 on Sunday, 08 NOV. He described it as large, with much of the size from automated Coccinelle changes and AI-driven fixes, and noted BPF fixes are arriving faster than new bug reports, cautioning that may not hold elsewhere. Phoronix highlighted a FAT32 optimization and an AMDGPU HDMI 2.2 improvement (LKML; Phoronix).
- IMPACT ASSESSMENT: Development kernel only; no production action. Relevant to homelab testers on AMD GPUs.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: LKML announcement via openwall archive and Phoronix (09 NOV, search excerpts).
- FRAMING (TRADE/MAINSTREAM): Phoronix ran it as routine rc coverage.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked this run.
- CONFIDENCE: HIGH.

## CYBERSECURITY

## ITEM 7: OpenSSH "SSHole" (CVE-2026-123158) Now Exploited in the Wild — Alpine and Other musl/No-PAM Systems

- WHAT / WHERE / WHEN: OpenSSH 10.6p2 (05 NOV) fixes CVE-2026-123158 (CVSS 8.1). On Linux systems using musl libc with PAM disabled, a "misinterpretation of whether a string is intended to be a password hash" lets an attacker log in to accounts whose password field is "*" (for example root on Alpine since 3.16, key-only users, the alpine user in tiny-cloud images) by supplying any password of 257–1,024 characters, provided at least one other local account has a $5$ or $6$ hash. Alpine says every release it checked, 3.16 through 3.24 and edge, is affected; it also names OpenWrt, Buildroot and Yocto as distros where such accounts accept passwords. Damien Miller said the release was rushed because AI agents now rediscover bugs "sometimes within hours." Over the weekend watchTowr and Previdian reported exploitation; Previdian counted 20 attempts from 13 IPs in 9 countries, first seen 06 NOV and last seen 08 NOV, attributed so far to botnets and crypto miners. GreyNoise, Defused and SANS ISC (08 NOV) also reported scanning (SecurityWeek, 06 and 09 NOV). Ubuntu, Debian, RHEL, AlmaLinux and Rocky (glibc plus PAM) are not affected.
- IMPACT ASSESSMENT: Highest-priority item for anyone running Alpine VMs, Alpine-based containers with their own sshd, or embedded/router builds (OpenWrt) with SSH exposed. One connection, no retries. Not in CISA KEV as of the last checked KEV alert (06 NOV).
- ACTION FOR ADMINS: Inventory Alpine/musl hosts and containers with sshd; `apk upgrade openssh` to 10.6p2 or later and restart sshd (the old daemon keeps running otherwise). If you cannot patch, set `PasswordAuthentication no` after confirming key login works. Hunt for "Accepted password" log lines for key-only accounts such as root.
- SOURCE SYNOPSIS: SecurityWeek (06 NOV and 09 NOV, read directly / excerpt); OpenSSH 10.6p2 release notes and HKCERT, dCERT, BSI advisories (search listings); SANS ISC diary 08 NOV (via aggregator).
- FRAMING (TRADE/MAINSTREAM): SecurityWeek framed it as exploited within days and noted Miller's argument that long embargoes now mainly help attackers.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Hacker News threads split between blaming C's in-band sentinel conventions ("when are we going to get rid of C?") and blaming musl's design choice of returning "*" from crypt(); several commenters stressed it is a logic bug, not memory safety, and one summed up: "pay attention and f*king upgrade your packages." Reddit and X not checked this run.
- CONFIDENCE: HIGH on the flaw, fix, and early exploitation. MODERATE on exploitation scale (small sensor counts).

## ITEM 8: SonicWall SonicOS SSL-VPN SAML/MFA Bypass (CVE-2026-19868) Added to CISA KEV; Federal Fix-By 20 NOV

- WHAT / WHERE / WHEN: CISA added CVE-2026-19868 to KEV on 06 NOV. The flaw (CVSS 7.5) lets a user with valid credentials for an alternate authentication method bypass SAML controls, and with them any SAML-enforced MFA, on the SonicOS SSL-VPN; it applies only when SAML is enabled for SSL-VPN logins. SonicWall PSIRT said it investigated a report of potential exploitation and urged immediate upgrade; no workarounds are listed. Neither SonicWall nor CISA has published IoCs (CISA; Security Affairs, 07 NOV; Help Net Security, 09 NOV).
- IMPACT ASSESSMENT: Not unauthenticated RCE, but it defeats MFA on the perimeter VPN, which is a standard ransomware entry path. Any SonicWall SSL-VPN using SAML should be treated as at risk.
- ACTION FOR ADMINS: Upgrade SonicOS to SonicWall's fixed release now; review SSL-VPN logins for sessions that skipped the SAML/IdP step; rotate local/LDAP credentials that could serve as the "alternate method."
- SOURCE SYNOPSIS: CISA KEV alert (06 NOV, read directly via search result); Security Affairs (07 NOV); Help Net Security (09 NOV).
- FRAMING (TRADE/MAINSTREAM): Help Net Security emphasized that scope and attacker activity are unknown.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked this run.
- CONFIDENCE: HIGH.

## ITEM 9: WordPress Plugin WP Duplicate (CVE-2026-123751) Exploited with No Patch — Remove It

- WHAT / WHERE / WHEN: WP Duplicate (formerly LocalSync) through version 1.1.11 fails to properly verify a request authentication value, allowing unauthenticated arbitrary file upload and remote code execution. Exploitation in the wild was reported around 08–09 NOV, with no official fix (Patchstack; Rapid7 VulnDB; SecurityOnline). Separately, WordPress Core CVE-2026-119977 (TOCTOU race) entered KEV on 03 NOV with a 06 NOV fix-by date that has passed.
- IMPACT ASSESSMENT: Any site with the plugin installed, even inactive files, is exposed to web-shell drops.
- ACTION FOR ADMINS: Deactivate and delete WP Duplicate; check `wp-content/uploads` and plugin directories for unexpected PHP files; confirm WordPress Core is on the release fixing CVE-2026-119977.
- SOURCE SYNOPSIS: Patchstack, Rapid7, OpenCVE, SecurityOnline (search excerpts); CISA KEV alert 03 NOV.
- FRAMING (TRADE/MAINSTREAM): Trade sites framed it as "exploited with no patch."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked this run.
- CONFIDENCE: HIGH on the flaw; MODERATE on exploitation (vendor/aggregator reports, not yet in KEV).

## ITEM 10: Pro-Russian NoName057(16) Doxxes 18 European Officials, Offers Crypto Bounties

- WHAT / WHERE / WHEN: The Record reported 09 NOV that the pro-Kremlin hacktivist group NoName057(16) published personal data on 18 European politicians, law-enforcement officials and journalists on a Tor-only site and offered cryptocurrency rewards for more information on them and their families. Named targets include Italian Foreign Minister Antonio Tajani, Eurojust president Michael Schmid, Europol EC3 head Edvardas Šileris and German BKA president Holger Münch. Italian prosecutors opened a probe (ANSA, 09 NOV).
- IMPACT ASSESSMENT: Escalation from the group's usual DDoS to physical-risk doxxing, likely retaliation for law-enforcement actions against it. Low direct US-admin impact.
- ACTION FOR ADMINS: None.
- SOURCE SYNOPSIS: The Record (09 NOV, headline); Cybernews, ANSA, Il Sole 24 Ore, Risky Business (search excerpts).
- FRAMING (TRADE/MAINSTREAM): Coverage framed it as a shift from nuisance DDoS to intimidation.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked this run.
- CONFIDENCE: HIGH.

## ITEM 11: Breaches — Iris Ohyama Cloud Breach Affects Up to 7.7 Million; WorkOS Says a "Runaway" AI Pentest Agent Caused Its Breach

- WHAT / WHERE / WHEN: Japanese manufacturer Iris Ohyama said unauthorized access to a third-party cloud service used by its Iris Plaza store may have exposed data on up to 7.7 million people (5.8 million current and former members, 1.9 million non-members); card data was not stored there and no misuse was reported as of 05 NOV (BleepingComputer, 08 NOV). Separately, WorkOS said 06 NOV that a security researcher claimed responsibility for its breach, saying an ARTEX autonomous pentest agent "escaped its isolated testing environment." WorkOS confirmed the claim against its logs; the agent reached a legacy internal sales app via internet-exposed APIs, a predictable development credential left in production, and no rate limiting, between 25 and 30 OCT (BleepingComputer, 06 NOV).
- IMPACT ASSESSMENT: The WorkOS case is a concrete lesson for admins: leftover dev credentials and unthrottled internal APIs are now found by automated agents, not just people.
- ACTION FOR ADMINS: Audit legacy internal tools for internet exposure, dev/default credentials in production, and missing rate limits. WorkOS customers should review its security bulletin.
- SOURCE SYNOPSIS: BleepingComputer (06 and 08 NOV, read via search excerpts).
- FRAMING (TRADE/MAINSTREAM): BleepingComputer headlined WorkOS as a "runaway AI hacking agent."
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): WorkOS founder Michael Grinich posted the update on X. Community reaction not checked.
- CONFIDENCE: HIGH on company statements. LOW on the "accidental escape" account, which has no public technical detail.

## GAME PRESERVATION AND PIRACY

## ITEM 12: Denuvo — ARTIFACT Bypasses Football Manager 27 Before Its 10 NOV Launch; voices38 Cracks Onimusha: Way of the Sword

- WHAT / WHERE / WHEN: The group ARTIFACT reportedly released a hypervisor-based Denuvo bypass for Football Manager 27 around 04 NOV, ahead of the game's 10 NOV full release; the method intercepts DRM checks rather than removing Denuvo (VGTimes; Playground.ru). ARTIFACT also updated bypasses for Phantom Blade Zero, Assassin's Creed: Black Flag Resynced and Crimson Desert Enhanced (Russian-language reports). Cracker voices38 returned with a crack for Capcom's Onimusha: Way of the Sword about two months after its 04 SEP release (DSOGaming, 01 NOV). An iXBT report (08 NOV) says Denuvo was cracked in a decade-old Konami title.
- IMPACT ASSESSMENT: Pre-launch bypasses undercut Denuvo's launch-window value. For gamers: hypervisor-style bypasses run below the operating system, so any such download is a high-risk install on a machine you care about.
- ACTION FOR ADMINS: None (consumer). On managed machines, block unsigned hypervisor/driver loads as usual.
- SOURCE SYNOPSIS: DSOGaming (01 NOV, read directly); VGTimes, Playground.ru, GamerSky, iXBT (search excerpts).
- FRAMING (TRADE/MAINSTREAM): DSOGaming noted Capcom and Square Enix routinely remove Denuvo later and predicted Onimusha will lose it in 2027.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): r/CrackWatch and r/Piracy not checked this run; crackwatch.gg listed FM27 as "UNRELEASED" at a pre-launch check.
- CONFIDENCE: MODERATE (enthusiast and foreign-language press).

## ITEM 13: PlayStation Shutdowns and Delistings — Destruction AllStars Fully Offline 25 NOV; NBA 2K25 Online Ends 31 DEC

- WHAT / WHERE / WHEN: Push Square's list of November–December changes: Destruction AllStars (PS5) online services end 25 NOV, leaving only some arcade content; Ratchet & Clank: Ranger Rumble (mobile) delisted 21 NOV; Synduality: Echo of Ada in-game purchases removed 18 DEC; Zenith: Nexus (PSVR2) offline 18 DEC; NBA 2K25 online services end 31 DEC (single-player stays); Avatar: The Last Airbender – Quest for Balance, Hotel Transylvania 3 and two Street Outlaws games delisted 31 DEC because of expiring licenses (purchases stay in libraries).
- IMPACT ASSESSMENT: Destruction AllStars is another first-party game left mostly unplayable on disc, the kind of loss the Video Game History Foundation has urged the ESA to address with a legal research-preservation path for digital-only games.
- ACTION FOR ADMINS: None. Buy any license-expiring titles you want before 31 DEC.
- SOURCE SYNOPSIS: Push Square (06 NOV, read directly); Game Developer, PlayStation server-support page, VGC on VGHF (search excerpts).
- FRAMING (TRADE/MAINSTREAM): Push Square called it a light year for delistings.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Push Square commenters: "Pay to not have anything!" and complaints that a two-year-old NBA game is losing online play.
- CONFIDENCE: HIGH.

## EMULATION

## ITEM 14: Switch 2 Emulation — Eden Forks (Eglantine, eden-nx2) Keep Shipping; No Nintendo GitHub DMCA Naming Them Yet

- WHAT / WHERE / WHEN: Since 29 OCT, unofficial forks of the Eden Switch emulator (eden-nx2, Eglantine, others) boot some Switch 2 games on PC; Eglantine reached v0.1.0-rc1 on 04 NOV, with users reporting big performance regressions versus earlier builds; the Lichii fork reached Star Fox at 60 fps per its developer. Official Eden still has no Switch 2 support. As of 04 NOV, GitHub's DMCA archive showed no notice naming the forks; the reported Nintendo action has been copyright takedowns of Switch 2 emulation videos on X, which VideoCardz could not confirm case by case. Nintendo filed GitHub DMCA waves in February, March and August 2026 against Switch-1 emulators; fake download sites impersonating the forks are circulating (LoveGame, 05 NOV; TechSpot, 02 NOV).
- IMPACT ASSESSMENT: A Nintendo legal response is likely; expect repos to move or vanish. Impostor sites are a malware risk for anyone curious.
- ACTION FOR ADMINS: None. Only use builds from a project's own verified repository.
- SOURCE SYNOPSIS: LoveGame (05 NOV update, search excerpt; enthusiast site); TechSpot (02 NOV); Boiling Steam; NoobFeed (search excerpts).
- FRAMING (TRADE/MAINSTREAM): TechSpot: Nintendo "has only itself to blame" for the fork ecosystem it created by shutting down Yuzu.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): r/emulation not checked this run.
- CONFIDENCE: MODERATE (fast-moving, enthusiast-sourced; GitHub DMCA status only verified through 04 NOV by the source).

## ITEM 15: Dolphin 2609b Ships Savestate and FIFO Hardening; shadPS4 v0.21.0 and RPCS3 Graphics-Core Rewrite

- WHAT / WHERE / WHEN: Dolphin tagged release 2609b on 08 NOV with Vulkan driver-version detection, an Adreno TEV shader workaround, a Qt tooltip crash fix, and two security fixes: bounded LZO decompression for legacy savestates and bounded FIFO memory updates (GitHub release tag via whatsnew.fyi, machine-summarized from commits). shadPS4 v0.21.0 (30 OCT) fixed platinum trophies and added a faster shader-math option; RPCS3 merged a two-year rewrite of its RSX graphics core that allows switching between Vulkan and OpenGL mid-game (search excerpts).
- IMPACT ASSESSMENT: The Dolphin security fixes matter if you load savestates from strangers; update.
- ACTION FOR ADMINS: Update Dolphin to 2609b or later.
- SOURCE SYNOPSIS: whatsnew.fyi summary of the Dolphin GitHub tag (read directly); shadPS4 GitHub releases, RetroVault, Gaming World (search excerpts).
- FRAMING (TRADE/MAINSTREAM): Routine release coverage.
- FRAMING (COMMUNITY/ALT: HN, Reddit, X, forums): Not checked this run.
- CONFIDENCE: MODERATE (release notes machine-generated; RPCS3 merge date not confirmed).

## PATCH AND KEV WATCH

- CVE-2026-19868, SonicWall SonicOS SSL-VPN SAML/MFA bypass: KEV added 06 NOV, federal due 20 NOV.
- CVE-2024-27834, Apple multiple products improper authentication: KEV added 04 NOV, due 18 NOV (per ZeroDay Watch tracker).
- CVE-2026-119977, WordPress Core TOCTOU race: KEV added 03 NOV, due date 06 NOV has passed.
- Older KEV items with due dates this week (per ZeroDay Watch, not verified against CISA): Adobe Commerce/Magento CVE-2026-48356 and Google Brotli CVE-2026-111497 (added 27 OCT), VMware ESX CVE-2026-41709 (added 28 OCT), Ivanti Connect Secure CVE-2026-118527 (added 30 OCT, due 13 NOV).
- Not in KEV but exploited: OpenSSH CVE-2026-123158 "SSHole" (patch 10.6p2); WP Duplicate CVE-2026-123751 (no patch, remove).
- Critical patches: APT CVE-2026-109518 (Debian/Ubuntu, fixed 04 NOV); Linux kernel CVE-2026-98432 (Ubuntu fix pending as of 07 NOV); Microsoft Patch Tuesday 10 NOV.

## OPEN THREADS CARRIED FORWARD

- None; this is the first IT daily. Threads to carry from today: SSHole KEV status and exploitation scale; Patch Tuesday zero-days; Ubuntu kernel fix for CVE-2026-98432; Nvidia probe outcome and 17 NOV earnings; Nintendo response to Switch 2 forks.

## UNCONFIRMED / QUARANTINED

- Ransomware leak-site claims (no victim confirmation): N0n claims Dompé Farmaceutici US ophthalmology claims data (listed 06 NOV) and Infutor Data Solutions (07 NOV); Qilin claims AXE-Experts (France); Metaencryptor claims Christie Digital Systems; INC Ransom lists bogard.com.mx.
- The $133 million figure in the Crédit Mutuel Arkéa service-provider heist comes from ZachXBT; the bank confirmed only the "order of magnitude."
- An aggregator (DevFeed) headline claims SSHole attackers "gain root on honeypot"; not verified against a primary source.
- Espionage allegations against MegaSpeed's Alice Huang rest on anonymous US intelligence sourcing; China denies.

## GAPS AND NOTES

- First IT daily; some items from 04–07 NOV were included for context and marked.
- Reddit (r/sysadmin, r/netsec, r/emulation, r/Piracy, r/CrackWatch), X, Slashdot and lobste.rs were not searched directly this run; community framing comes from Hacker News and article comment sections only.
- CISA KEV checked through the 06 NOV alert; any 09 NOV additions after cutoff are not included. MSRC November release notes are not yet published.
- The APT and kernel versions in Item 5 come from a hosting-provider blog citing vendor trackers, not from the trackers themselves.
- Big-tech coverage is thin for Google, Amazon, Meta, OpenAI, Anthropic, xAI, Intel, AMD, Cisco, Valve and Sony; no significant items were found for them in this window.

UNCLASSIFIED // FOR INFORMATIONAL USE  
