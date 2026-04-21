---
name: analyze-saudi-labor-dispute
description: "Workflow for analyzing Saudi labor disputes, HR files, and disciplinary matters under Saudi workplace context. Coordinates Document Research Agent and Arabic Legal Analyst to build chronology, map evidence, surface contradictions, assess procedural fairness, and produce cautious Arabic-first formal wording."
context: |
  This prompt guides a disciplined workflow for analyzing Saudi labor disputes
  and HR/disciplinary records inside the Khalid framework.

  It is designed to work with:
  - Document Research Agent
  - Arabic Legal Analyst

  It does not replace either agent.
  It orchestrates how they are used together for Saudi-context labor matters.

  Use when working with:
  - Saudi labor disputes (private sector or government-adjacent)
  - HR and disciplinary files
  - warning letters and termination notices
  - investigation committee minutes
  - attendance, payroll, and performance records
  - internal correspondence and official notifications
  - procedural fairness concerns
  - chronology building and contradiction analysis
  - evidence-heavy materials that need Arabic-first cautious framing

  This workflow is evidence-aware and uncertainty-aware.
  It does not replace licensed legal advice and does not produce jurisdiction-specific rulings.
---

# Analyze Saudi Labor Dispute Workflow

## Overview

This workflow is for **Saudi labor dispute and HR/disciplinary file analysis** inside the Khalid framework.

It should be used when the task requires:
- careful document extraction from Arabic HR/labor records
- Arabic RTL preservation
- chronology building across the employment relationship
- evidence mapping across notices, minutes, warnings, and decisions
- contradiction analysis across overlapping records
- procedural fairness analysis of disciplinary steps
- cautious Arabic-first formal wording suitable for objections, grievances, or labor office submissions

This workflow must preserve the distinction between:
1. **document extraction**
2. **research and validation**
3. **legal analysis**

It must not convert suspicion into proof and must not assume conclusions that the Saudi-context record does not support.

---

## Step 1: Identify the Source Package

**Action:** Determine what HR/labor material exists and what state it is in.

### Check:
- [ ] What files are included? (contracts, warnings, minutes, notices, payslips, attendance, emails)
- [ ] Are they PDFs, images, screenshots, exported emails, or manually transcribed text?
- [ ] Are the files original, scanned, re-exported, or forwarded copies?
- [ ] Is extraction already complete, partially complete, or not started?
- [ ] Are there multiple versions of the same document (draft vs. signed, Arabic vs. English)?
- [ ] Are attachments, appendices, signatures, stamps, or referenced documents missing?
- [ ] Are there gaps in the employment chronology (hiring, warnings, investigation, termination)?
- [ ] Is there any visible issue with quality, structure, or completeness?

### Output:
Create a **Source Package Summary** including:
- file types
- number of documents
- known gaps across the employment timeline
- whether extraction is needed
- whether version comparison may be required
- whether signatures, stamps, or distribution references are missing

---

## Step 2: Run Document Extraction and Validation First

**Action:** Use **Document Research Agent** before any legal analysis begins.

### Required extraction rules:
- Preserve Arabic right-to-left order
- Prefer native PDF extraction before OCR
- Use OCR only when needed
- Keep formatting, section order, and document hierarchy where possible
- Preserve dates, names, job titles, references, amounts, and official titles exactly
- Preserve reference numbers, memo numbers, and registry identifiers verbatim
- Do not guess unclear Arabic text without marking uncertainty

### Required content separation:
For extracted material, classify content as:
- **Verified Extracted Text**
- **Interpreted Text**
- **Uncertain Fragments**

### Also record:
- OCR limitations
- metadata uncertainty
- partial pages
- weak scan quality
- mixed Arabic/English directionality issues
- missing pages, attachments, or signatures
- suspected version differences (e.g., draft vs. final warning)
- suspected backdating or inconsistent date formats

### Output:
Create an **Extraction and Validation Summary** containing:
- extraction method used
- confidence level
- key text blocks extracted
- unclear sections
- any structure, metadata, or signature concerns

---

## Step 3: Build the Employment Chronology

**Action:** Construct a clean timeline of the employment relationship and dispute.

### Extract and organize:
- [ ] hiring date and contract type
- [ ] role changes, transfers, promotions
- [ ] performance reviews and KPI records
- [ ] attendance and leave records
- [ ] warnings (verbal, written, final)
- [ ] complaints raised by or against the employee
- [ ] investigation committee formation and minutes
- [ ] hearing dates and responses submitted
- [ ] disciplinary decisions
- [ ] suspension, salary hold, or benefits change
- [ ] termination notice and end-of-service calculation
- [ ] labor office / GOSI / related filings referenced
- [ ] correspondence dates (creation, send, acknowledgment)

### Chronology rules:
- Prefer exact dates over approximate phrases
- Preserve both Hijri (هجري) and Gregorian (ميلادي) dates when present
- Mark date ambiguity clearly
- Separate document date from event date when they differ
- Separate creation date, send date, signature date, and acknowledgment date where relevant
- Identify missing chronology links explicitly (e.g., warning referenced but not produced)

### Output:
Create a **Chronology Table** with:
- date / period (Hijri + Gregorian where available)
- event
- actor (employee, manager, HR, investigation committee, legal, external body)
- supporting record
- confidence level
- notes on ambiguity, missing links, or backdating concerns

---

## Step 4: Map the Evidence

**Action:** Build a structured evidence inventory for the labor file.

### Map:
- contracts and addenda
- job descriptions and KPIs
- warnings and disciplinary notices
- investigation minutes and statements
- witness statements
- attendance, biometric, and access logs
- payroll and deductions
- email and messaging records
- official correspondence and stamped letters
- signatures, stamps, and distribution references
- missing items
- contradictions between records

### For each evidence item, identify:
- what it is
- what it proves directly
- what it may suggest
- what weakens it
- whether it is signed, dated, stamped, complete, revised, partial, or uncertain
- whether it supports chronology, authorship, circulation, content, procedure, or quantum

### Contradiction mapping:
When two or more records differ, identify:
- exact contradiction
- where it appears
- whether it affects credibility, timing, authorship, procedure, or legal framing
- whether the contradiction is proven or only suspected

### Output:
Create an **Evidence Map** with:
- item name
- type
- evidentiary value
- weaknesses
- linked contradictions
- missing related material

---

## Step 5: Procedural Fairness Analysis

**Action:** Examine the disciplinary process for procedural integrity, without asserting specific legal rulings.

### Examine, where the record allows:
- [ ] whether the employee received clear written notice of the allegations
- [ ] whether the employee was given a meaningful opportunity to respond
- [ ] whether the employee had access to the evidence used against them
- [ ] whether an investigation committee was formed and properly constituted
- [ ] whether statements were recorded, signed, and shared
- [ ] whether warnings were issued in sequence and acknowledged
- [ ] whether the decision-maker was distinct from the investigator
- [ ] whether timelines between notice, hearing, and decision are reasonable
- [ ] whether the stated reason for any decision matches the evidentiary record
- [ ] whether required internal approvals, signatures, or stamps are present

### Discipline rules:
- Do not assert violations of specific Saudi statutory articles unless the record directly supports them
- Frame procedural concerns as **observations on the record**, not legal verdicts
- Keep wording evidence-bounded

### Output:
Create a **Procedural Fairness Observations** section listing:
- each procedural concern
- what in the record supports it
- what is missing that would confirm or rebut it
- confidence level

---

## Step 6: Hand Over to Arabic Legal Analyst

**Action:** After extraction, chronology, evidence mapping, and procedural observations are done, use **Arabic Legal Analyst**.

The legal analysis must clearly separate:

1. **Verified Facts**
2. **Plausible Inferences**
3. **Unresolved Points**

### Handover rule:
Do not let legal analysis begin from raw or unclear source material without noting the extraction status.

If extraction quality or provenance is weak, that weakness must remain visible inside the legal analysis.

### Output:
Prepare a **Legal Analysis Input Summary** for the Arabic Legal Analyst containing:
- validated facts
- chronology summary
- evidence map
- contradictions
- procedural fairness observations
- extraction limitations
- unresolved record gaps

---

## Step 7: Assess Legal Significance Carefully

**Action:** Evaluate the legal significance without overstating certainty.

### Assess, where relevant:
- procedural fairness weaknesses
- denial of access to evidence or inability to respond
- evidentiary weakness of the employer's stated reason
- contradiction significance across records
- authorship/provenance weakness (unsigned, unstamped, undated)
- document-integrity concerns (suspected backdating, altered versions)
- administrative implications of procedural gaps
- labor implications of an unsupported termination or disciplinary decision
- credibility impact of contradictions
- significance of missing attachments, missing minutes, or missing chronology links
- end-of-service and entitlement exposure where the record allows

### Discipline rules:
- Do not convert suspicion into proof
- Do not assume legal classification that the record does not support
- Do not invent specific Saudi statutory outcomes without support
- Keep conclusions proportional to the evidence
- Make uncertainty visible, not hidden

### Output:
Create a **Legal Significance Summary** showing:
- what matters legally or procedurally
- why it matters
- what supports that significance
- what remains too weak or incomplete

---

## Step 8: Produce Structured Final Output

**Action:** Generate the final analysis in this exact structure:

### 1. Verified Facts
- include only what is directly supported by the record

### 2. Plausible Inferences
- include cautious reasoned conclusions that are not fully proven

### 3. Unresolved Points
- list contradictions, missing items, ambiguities, and evidentiary gaps

### 4. Procedural Fairness Observations
- summarize the process concerns supported by the record

### 5. Legal Significance / Why It Matters
- explain why the strongest points matter legally or procedurally

### 6. Top 3 Critical Points
- identify only the three most outcome-relevant points

### 7. What Proves Each Point
- state the strongest supporting material for each critical point

### 8. What Is Still Missing
- state what additional document, signature, stamp, metadata, testimony, chronology link, or attachment would materially strengthen each point

### 9. Formal Wording
- provide concise Arabic-first wording suitable for:
  - internal objection to a disciplinary decision
  - grievance letter
  - labor office submission summary
  - internal memo
  - case-preparation note

---

## Step 9: Formal Wording Rules

**Action:** Make the closing wording usable in serious Saudi labor-style drafting.

### Formal wording standards:
- Arabic-first
- restrained
- evidence-based
- memo-ready
- not exaggerated
- not conclusory beyond the record
- preserves legally meaningful Arabic wording
- suitable for sensitive labor/HR workflows in a Saudi workplace context

### The final wording must:
- reflect the actual evidence strength
- avoid certainty inflation
- avoid casual language
- avoid asserting specific statutory violations without support
- remain usable for follow-up drafting by a qualified legal professional

---

## Required Quality Rules

Before finalizing, verify all of the following:

- [ ] Arabic RTL order was preserved during extraction
- [ ] Hijri and Gregorian dates were preserved where present
- [ ] Extraction limitations were recorded clearly
- [ ] Verified text is separated from interpreted text and uncertain fragments
- [ ] Chronology is organized and source-linked
- [ ] Evidence items are mapped individually
- [ ] Contradictions are identified precisely
- [ ] Procedural fairness concerns are framed as record-based observations
- [ ] Legal analysis starts from validated material, not raw assumptions
- [ ] Verified Facts, Plausible Inferences, and Unresolved Points are clearly separated
- [ ] Legal significance is proportionate to the evidence
- [ ] Final wording is Arabic-first, formal, restrained, and usable

---

## Output Format

Use this final output structure:

### Source Package Summary
- ...

### Extraction and Validation Summary
- ...

### Chronology Table
- ...

### Evidence Map
- ...

### Procedural Fairness Observations
- ...

### Verified Facts
- ...

### Plausible Inferences
- ...

### Unresolved Points
- ...

### Legal Significance / Why It Matters
- ...

### Top 3 Critical Points
- ...

### What Proves Each Point
- ...

### What Is Still Missing
- ...

### Formal Wording
- ...

---

## Example Use Case

**User:**  
"Use Document Research Agent to extract this Saudi HR disciplinary file, then use Arabic Legal Analyst to prepare a cautious summary for an objection to a termination decision."

**Workflow should:**
1. inspect the HR/labor file set
2. extract and validate Arabic content, preserving Hijri and Gregorian dates
3. preserve RTL order
4. separate verified extraction from uncertain fragments
5. build the employment chronology
6. map evidence, signatures, stamps, and contradictions
7. record procedural fairness observations
8. hand over to Arabic Legal Analyst
9. produce a structured Arabic-first labor dispute summary with formal wording

---

## Limitations

- This workflow belongs to a **GitHub Copilot agent framework**, not a standalone legal platform
- It does not replace licensed legal advice from a Saudi-qualified lawyer
- It does not assume live access to Saudi labor databases, court systems, or official registries
- It does not issue statutory rulings or definitive legal classifications
- It must remain evidence-aware and uncertainty-aware at every stage

---

**Created:** 2026-04-21 | **Khalid Saudi Labor Dispute Analysis Workflow**
