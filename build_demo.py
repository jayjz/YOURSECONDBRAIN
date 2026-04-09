# -*- coding: utf-8 -*-
import os

demo_files = {
    "BRAIN.md": """# MovingBytes Knowledge Operating System: Core Schema
You are the automated librarian for this agency. Your job is to read all data in the `raw/` folder and compile it into the `wiki/` folder.

## Rules of Engagement
1. **Never delete raw data.** You only read from `raw/` and write to `wiki/`.
2. **Synthesize, don't just summarize.** Connect the dots. If a Slack thread contradicts a Google Doc, update the wiki with the most recent timeline and flag the contradiction.
3. **Mandatory Backlinking.** Every claim in the wiki MUST link back to the source file in `raw/`. 

## Taxonomy
- `wiki/clients/`: One file per client. Must include: Executive Summary, Key Personnel, Buying Triggers, Active Campaigns.
- `wiki/campaigns/`: One file per project. Must include: Budget, Deadlines, Core Messaging, Status.
- `wiki/INDEX.md`: The master dashboard. Update this every time a new file is created.
""",

    "README.md": """# MovingBytes: The Agency Knowledge Base (Demo)
**Welcome to your team's new brain.**

If you run an agency, your most valuable asset-client context, campaign learnings, and strategy-is currently dying in Slack threads, buried in Google Drive, and locked in Zoom transcripts. 

This repository demonstrates how **MovingBytes** solves that.

### How to navigate this demo:
1. **Look at the Chaos:** Open the `raw/` folder. Read the messy Slack export, the rambling Zoom transcript, and the outdated Google Doc. This is what your data actually looks like today.
2. **Look at the Brain:** Open `BRAIN.md`. This is the custom schema we write for you. It tells our AI exactly how your agency operates.
3. **Look at the Clarity:** Open the `wiki/` folder (start with `INDEX.md`). Look at how the AI automatically caught the budget change, synthesized the client's buying psychology, and formatted it perfectly.

**Zero manual data entry. Zero lost context. Maintained for you automatically every month.**
👉 **[Book a Discovery Call](https://calendly.com/wizardordinals/second-brain-consultation) to get this built for your agency.**
""",

    "raw/slack_exports/apex_q3_pivot_chat.txt": """[2026-04-12 10:02 AM] Sarah Chen (Account Exec): Hey team, Apex just pinged me. They want to pivot the Q3 push. 
[2026-04-12 10:04 AM] Mike T. (Strategist): Wait what? We already locked the "Operational Efficiency" messaging last week. 
[2026-04-12 10:05 AM] Sarah Chen: I know. But their CFO just stepped in. He's breathing down the marketing team's neck. They need the whole campaign to be strictly about "Cost-Reduction ROI" now.
[2026-04-12 10:12 AM] Dave (Creative): God dammit. Do we have the new budget numbers?
[2026-04-12 10:15 AM] Sarah Chen: Let me check the drive. I think it's in the V2 folder. Or V3. Give me a sec.
[2026-04-12 10:18 AM] Sarah Chen: Okay found it. Budget is bumped to $120k, but timeline is compressed. We need the new deck by the 28th.
[2026-04-12 10:20 AM] Mike T.: Fine. I'll rewrite the brief. Somebody make sure the VP of Ops (John? Jack?) is cc'd on the new mockups.""",

    "raw/slack_exports/stratashift_rebrand_chaos.txt": """[2026-03-02 09:14 AM] Dave (Creative): Did anyone get the new hex codes for StrataShift?
[2026-03-02 09:20 AM] Sarah Chen: I think the client emailed them to Mike.
[2026-03-02 11:05 AM] Mike T.: Yeah, hold on. The CEO said to ditch the old Navy Blue. New primary is Midnight Slate (#1A2B3C) and accent is Neon Teal (#00FFCC).
[2026-03-02 11:08 AM] Dave: Awesome. Updating the Figma files now. Wait, the brief in Drive says the accent is Orange?
[2026-03-02 11:15 AM] Mike T.: Ignore the Drive doc. It's from 2024. Stick to the Teal.""",

    "raw/slack_exports/onboarding_rant.txt": """[2026-04-01 02:30 PM] Sarah Chen: Guys, we missed the vendor setup for Apex Corp again. Finance is pissed.
[2026-04-01 02:35 PM] Mike T.: Do we even have an onboarding checklist?
[2026-04-01 02:40 PM] Sarah Chen: We used to. Basically it's: 1. Send MSA via DocuSign. 2. Get their billing contact info. 3. Set up the Slack Connect channel. 4. Send the intake questionnaire. But Dave usually sets up the Slack channel.
[2026-04-01 02:45 PM] Dave: I only do it if Sarah tells me to! We need this documented.""",

    "raw/drive_docs/Apex_Brief_v3_FINAL_reallyfinal.txt": """PROJECT BRIEF: APEX CORP Q3
Target Audience: Mid-market SaaS, manufacturing logistics ops teams.
Goal: Lead gen for Q3.
Budget: $90,000 [NOTE from Sarah: THIS IS OUTDATED, DO NOT USE]
Core Message: Apex makes your team faster. [COMMENT: Mike - change this to ROI]
Deliverables: 1x Core Pitch Deck, 3x LinkedIn Ad variants, 1x Landing page copy
Deadlines: TBD. Sometime late April.""",

    "raw/drive_docs/StrataShift_Old_Brand_Guidelines.txt": """STRATASHIFT BRAND GUIDELINES (DRAFT 2024)
Primary Color: Navy Blue (#000080)
Accent Color: Industrial Orange (#FF8C00)
Tone of Voice: Traditional, Serious, Corporate.""",

    "raw/transcripts/apex_kickoff_zoom.md": """# Zoom Transcript: Apex Corp Q3 Kickoff
**Date:** March 15, 2026
**Participants:** Sarah Chen (Agency), Mike T. (Agency), John Davis (Apex VP Ops)

[00:01:45] Mike T.: Got it. So we lean heavily into the new automated dashboard features? Show them how fast it is?
[00:01:50] John Davis: No, no. Honestly, they don't care about the features. The CFOs we're selling to only care about bottom-line ROI. If the pitch deck doesn't explicitly show how our software saves them $50k in year one, they tune out immediately. 
[00:02:10] Sarah Chen: Understood. ROI-first framing. Cost reduction over feature lists.
[00:02:15] John Davis: Exactly. Also, just an FYI, our procurement cycle has slowed down. It's averaging like 6 weeks right now because both me and the CFO have to sign off on anything over $10k.""",

    "raw/transcripts/stratashift_kickoff.md": """# Transcript: StrataShift Q2 Rebrand Kickoff
[00:04:12] Client CEO: Look, logistics is boring. We want to stop sounding like a traditional trucking company and start sounding like a tech company. 
[00:04:30] Mike T.: So, edgier tone? Shorter sentences?
[00:04:35] Client CEO: Exactly. Punchy. "We move freight, faster." That kind of thing. No more corporate jargon.""",

    "wiki/INDEX.md": """# Agency Master Knowledge Base
*Last Compiled: Automated Health Check Passed (April 2026)*

Welcome to the Agency Wiki. All raw Slack threads, transcripts, and drive docs have been synthesized below. 

### Client Intelligence
* [Apex Corp](./clients/apex_corp.md) - *Mid-market SaaS (Active)*
* [StrataShift](./clients/stratashift.md) - *Enterprise Logistics (Active)*

### Active Campaigns
* [Apex Q3 B2B Push](./campaigns/apex_q3_push.md) - *Status: Pivoting*
* [StrataShift Q2 Rebrand](./campaigns/stratashift_rebrand.md) - *Status: In Progress*

### Internal Operations
* [SOP: Client Onboarding](./internal_process/client_onboarding.md)

### Automated System Flags
* **Automated Action:** Extracted missing onboarding process from Slack chat and created new SOP.
* **Automated Action:** Resolved brand color contradiction for StrataShift.
* *See full log in [`../automated_reports/health_check_apr2026.md`](../automated_reports/health_check_apr2026.md)*
""",

    "wiki/clients/apex_corp.md": """# Apex Corp
**Industry:** Mid-Market SaaS (Manufacturing & Logistics focus)
**Status:** Active Client

## Key Personnel
* **John Davis (VP of Ops):** Key decision-maker. Cares strictly about bottom-line ROI, not feature lists. [Source: `raw/transcripts/apex_kickoff_zoom.md`]
* **CFO (Name Unknown):** Joint sign-off required for any deal over $10k. Highly focused on cost-reduction. [Source: `raw/slack_exports/apex_q3_pivot_chat.txt`]

## Buying Triggers & Sales Psychology
Three years of engagement data and recent kickoff calls reveal a strict pattern:
1. **ROI-First Framing:** Apex's target accounts are tightening budgets. Pitches must explicitly show a path to saving $50k+ in year one. 
2. **Feature Fatigue:** Do not lead with UI/UX or dashboard features. 
3. **Procurement Cycle:** Currently averaging 6 weeks due to dual sign-off requirements (VP Ops + CFO).

## Active Campaigns
* **[Q3 B2B Push](../campaigns/apex_q3_push.md)**
""",

    "wiki/clients/stratashift.md": """# StrataShift
**Industry:** Enterprise Logistics & Supply Chain
**Status:** Active Client

## Brand Identity (Updated March 2026)
* **Tone of Voice:** Punchy, tech-forward, edgy. No corporate jargon. (e.g., "We move freight, faster.") [Source: `raw/transcripts/stratashift_kickoff.md`]
* **Primary Color:** Midnight Slate (#1A2B3C)
* **Accent Color:** Neon Teal (#00FFCC)
* *Note: The 2024 Drive doc referencing Navy/Orange is obsolete. Do not use.* [Source: `raw/slack_exports/stratashift_rebrand_chaos.txt`]

## Active Campaigns
* **[Q2 Brand Repositioning](../campaigns/stratashift_rebrand.md)**
""",

    "wiki/campaigns/apex_q3_push.md": """# Campaign: Apex Q3 B2B Push

## Overview
* **Goal:** Q3 Lead Generation targeting mid-market operations teams.
* **Budget:** $120,000 *(Updated April 12)*
* **Deadline:** April 28, 2026

## STRATEGY PIVOT (Action Required)
As of April 12, the core messaging has pivoted away from "Operational Efficiency" to **"Cost-Reduction ROI."** This was mandated by the client's CFO. [Source: `raw/slack_exports/apex_q3_pivot_chat.txt`]

### Deliverables Update
* 1x Core Pitch Deck (Must explicitly model $50k+ year-one savings)
* 3x LinkedIn Ad variants (ROI focused)
* 1x Landing page copy

*Note to Creative:* Ensure John Davis (VP Ops) is CC'd on all new mockups to bypass procurement delays.
""",

    "wiki/campaigns/stratashift_rebrand.md": """# Campaign: StrataShift Q2 Brand Repositioning

## Overview
* **Goal:** Transition brand identity from "traditional trucking" to "logistics tech company."

## Key Directives
* Ensure all new creatives utilize the Midnight Slate / Neon Teal palette. 
* All copy must be rewritten to match the new punchy, tech-forward tone.
""",

    "wiki/internal_process/client_onboarding.md": """# SOP: New Client Onboarding
*Last Updated: April 2026 via Slack extraction*

To prevent missed vendor setups and finance delays, follow this strict 4-step order for all new clients:

1. **Contracting:** Send MSA via DocuSign (Owner: Account Exec).
2. **Finance:** Secure client billing contact info and submit to internal finance (Owner: Account Exec).
3. **Comms:** Setup Slack Connect channel and invite client stakeholders (Owner: Creative/Dave, triggered by AE).
4. **Discovery:** Send the standard Intake Questionnaire to the client.

[Source: `raw/slack_exports/onboarding_rant.txt`]
""",

    "automated_reports/health_check_apr2026.md": """# MovingBytes Automated Health Check
**Run Date:** April 14, 2026
**Status:** Complete with actions taken.

## Contradictions Resolved
* **StrataShift Brand Colors:** `raw/drive_docs/StrataShift_Old_Brand_Guidelines.txt` listed Navy/Orange, but recent Slack data (`stratashift_rebrand_chaos.txt`) stated Midnight Slate/Teal. 
  * *Action:* Updated `wiki/clients/stratashift.md` to reflect the new Slack data and flagged the drive doc as obsolete.
* **Apex Corp Budget:** Drive brief stated $90k, Slack history confirmed an increase to $120k. 
  * *Action:* Updated `wiki/campaigns/apex_q3_push.md`.

## Knowledge Extraction
* Extracted new internal process from `raw/slack_exports/onboarding_rant.txt`. 
  * *Action:* Created new SOP at `wiki/internal_process/client_onboarding.md`.

## Data Gaps Identified
* **Missing Deadline:** The StrataShift Q2 Rebrand has no formal launch date listed in any raw data sources. Please upload a timeline document to the `raw/` folder for ingestion.
"""
}

# Delete the old CLAUDE.md if it exists so we don't have duplicates
if os.path.exists("CLAUDE.md"):
    os.remove("CLAUDE.md")

# Create folders and files safely
for filepath, content in demo_files.items():
    os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())

print("SUCCESS: Demo repo fully populated with BRAIN.md and unbreakable encoding.")