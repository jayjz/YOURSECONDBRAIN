import os

demo_data = {
    # --- MORE RAW CHAOS ---
    "raw/slack_exports/stratashift_rebrand_chaos.txt": """
[2026-03-02 09:14 AM] Dave (Creative): Did anyone get the new hex codes for StrataShift?
[2026-03-02 09:20 AM] Sarah Chen: I think the client emailed them to Mike.
[2026-03-02 11:05 AM] Mike T.: Yeah, hold on. The CEO said to ditch the old Navy Blue. New primary is Midnight Slate (#1A2B3C) and accent is Neon Teal (#00FFCC).
[2026-03-02 11:08 AM] Dave: Awesome. Updating the Figma files now. Wait, the brief in Drive says the accent is Orange?
[2026-03-02 11:15 AM] Mike T.: Ignore the Drive doc. It's from 2024. Stick to the Teal.
    """,
    "raw/slack_exports/onboarding_rant.txt": """
[2026-04-01 02:30 PM] Sarah Chen: Guys, we missed the vendor setup for Apex Corp again. Finance is pissed.
[2026-04-01 02:35 PM] Mike T.: Do we even have an onboarding checklist?
[2026-04-01 02:40 PM] Sarah Chen: We used to. Basically it's: 1. Send MSA via DocuSign. 2. Get their billing contact info. 3. Set up the Slack Connect channel. 4. Send the intake questionnaire. But Dave usually sets up the Slack channel.
[2026-04-01 02:45 PM] Dave: I only do it if Sarah tells me to! We need this documented.
    """,
    "raw/drive_docs/StrataShift_Old_Brand_Guidelines.txt": """
STRATASHIFT BRAND GUIDELINES (DRAFT 2024)
Primary Color: Navy Blue (#000080)
Accent Color: Industrial Orange (#FF8C00)
Tone of Voice: Traditional, Serious, Corporate.
    """,
    "raw/transcripts/stratashift_kickoff.md": """
# Transcript: StrataShift Q2 Rebrand Kickoff
[00:04:12] Client CEO: Look, logistics is boring. We want to stop sounding like a traditional trucking company and start sounding like a tech company. 
[00:04:30] Mike T.: So, edgier tone? Shorter sentences?
[00:04:35] Client CEO: Exactly. Punchy. "We move freight, faster." That kind of thing. No more corporate jargon.
    """,

    # --- MORE SYNTHESIZED WIKI FILES ---
    "wiki/clients/stratashift.md": """
# StrataShift
**Industry:** Enterprise Logistics & Supply Chain
**Status:** Active Client

## Ìæ® Brand Identity (Updated March 2026)
* **Tone of Voice:** Punchy, tech-forward, edgy. No corporate jargon. (e.g., "We move freight, faster.") [Source: `raw/transcripts/stratashift_kickoff.md`]
* **Primary Color:** Midnight Slate (#1A2B3C)
* **Accent Color:** Neon Teal (#00FFCC)
* *Note: The 2024 Drive doc referencing Navy/Orange is obsolete. Do not use.* [Source: `raw/slack_exports/stratashift_rebrand_chaos.txt`]

## Ì≥Å Active Campaigns
* **[Q2 Brand Repositioning](../campaigns/stratashift_rebrand.md)**
    """,
    "wiki/campaigns/stratashift_rebrand.md": """
# Campaign: StrataShift Q2 Brand Repositioning

## Ì≥ä Overview
* **Goal:** Transition brand identity from "traditional trucking" to "logistics tech company."

## Ì≥ù Key Directives
* Ensure all new creatives utilize the Midnight Slate / Neon Teal palette. 
* All copy must be rewritten to match the new punchy, tech-forward tone.
    """,
    "wiki/internal_process/client_onboarding.md": """
# SOP: New Client Onboarding
*Last Updated: April 2026 via Slack extraction*

To prevent missed vendor setups and finance delays, follow this strict 4-step order for all new clients:

1. **Contracting:** Send MSA via DocuSign (Owner: Account Exec).
2. **Finance:** Secure client billing contact info and submit to internal finance (Owner: Account Exec).
3. **Comms:** Setup Slack Connect channel and invite client stakeholders (Owner: Creative/Dave, triggered by AE).
4. **Discovery:** Send the standard Intake Questionnaire to the client.

[Source: `raw/slack_exports/onboarding_rant.txt`]
    """,
    
    # --- AUTOMATED REPORTS (THE PROOF IT WORKS) ---
    "automated_reports/health_check_apr2026.md": """
# Ì¥ñ MovingBytes Automated Health Check
**Run Date:** April 14, 2026
**Status:** ‚úÖ Complete with actions taken.

## Ì¥Ñ Contradictions Resolved
* **StrataShift Brand Colors:** `raw/drive_docs/StrataShift_Old_Brand_Guidelines.txt` listed Navy/Orange, but recent Slack data (`stratashift_rebrand_chaos.txt`) stated Midnight Slate/Teal. 
  * *Action:* Updated `wiki/clients/stratashift.md` to reflect the new Slack data and flagged the drive doc as obsolete.
* **Apex Corp Budget:** Drive brief stated $90k, Slack history confirmed an increase to $120k. 
  * *Action:* Updated `wiki/campaigns/apex_q3_push.md`.

## Ì∑† Knowledge Extraction
* Extracted new internal process from `raw/slack_exports/onboarding_rant.txt`. 
  * *Action:* Created new SOP at `wiki/internal_process/client_onboarding.md`.

## ‚ö†Ô∏è Data Gaps Identified
* **Missing Deadline:** The StrataShift Q2 Rebrand has no formal launch date listed in any raw data sources. Please upload a timeline document to the `raw/` folder for ingestion.
    """
}

# Create the files
for filepath, content in demo_data.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())

print("‚úÖ Massive demo data payload injected successfully.")
