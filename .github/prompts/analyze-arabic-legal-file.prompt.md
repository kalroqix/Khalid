---
name: analyze-arabic-legal-file
description: "Workflow for analyzing Arabic legal, labor, HR, disciplinary, and evidence-heavy case files. Coordinates Document Research Agent and Arabic Legal Analyst to extract, validate, structure, and analyze sensitive materials without overstating certainty."
context: |
  This prompt guides a disciplined workflow for Arabic legal and evidence-heavy file analysis.
  It is designed to work with:
  - Document Research Agent
  - Arabic Legal Analyst

  It does not replace either agent.
  It orchestrates how they are used together.

  Use when working with:
  - Arabic legal documents
  - labor disputes
  - HR and disciplinary files
  - internal investigation records
  - official correspondence
  - evidence-heavy case materials
  - contradiction mapping
  - procedural fairness analysis
  - document-integrity concerns
---

# Analyze Arabic Legal File Workflow

## Overview

This workflow is for **Arabic legal and evidence-heavy case analysis** inside the Khalid framework.

It should be used when the task requires:
- careful document extraction
- Arabic RTL preservation
- chronology building
- contradiction mapping
- evidence classification
- cautious legal framing
- memo-ready Arabic legal wording

This workflow must preserve the distinction between:
1. **document extraction**
2. **research and validation**
3. **legal analysis**

It must not present uncertainty as proof.

---

## Step 1: Identify the Source Package

**Action:** Determine what material exists and what state it is in.

### Check:
- [ ] What files are included?
- [ ] Are they PDFs, images, screenshots, emails, letters, tables, logs, or text?
- [ ] Are the files original, scanned, exported, or manually transcribed?
- [ ] Is extraction already complete, partially complete, or not started?
- [ ] Are there multiple versions of the same document?
- [ ] Are attachments, appendices, or referenced documents missing?
- [ ] Is there any visible issue with quality, structure, or completeness?

### Output:
Create a **Source Package Summary** including:
- file types
- number of documents
- known gaps
- whether extraction is needed
- whether version comparison may be required

---

## Step 2: Run Document Extraction and Validation First

**Action:** Use **Document Research Agent** before legal analysis begins.

### Required extraction rules:
- Preserve Arabic right-to-left order
- Prefer native PDF extraction before OCR
- Use OCR only when needed
- Keep formatting, section order, and document hierarchy where possible
- Preserve dates, names, references, amounts, and official titles exactly
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
- missing pages or attachments
- suspected version differences

### Output:
Create an **Extraction and Validation Summary** containing:
- extraction method used
- confidence level
- key text blocks extracted
- unclear sections
- any structure or metadata concerns

---

## Step 3: Build the Chronology

**Action:** Construct a clean timeline from the validated material.

### Extract and organize:
- [ ] dates
- [ ] events
- [ ] actors
- [ ] decisions
- [ ] notices
- [ ] meetings
- [ ] statements
- [ ] document creation/export dates
- [ ] attachments referenced by time
- [ ] procedural sequence

### Chronology rules:
- Prefer exact dates over approximate phrases
- Mark date ambiguity clearly
- Separate document date from event date when they differ
- Separate creation date, send date, signature date, and export date where relevant
- Identify missing chronology links explicitly

### Output:
Create a **Chronology Table** with:
- date / period
- event
- actor
- supporting record
- confidence level
- notes on ambiguity or missing links

---

## Step 4: Map the Evidence

**Action:** Build a structured evidence inventory.

### Map:
- documents
- statements
- attachments
- signatures
- metadata
- distribution/circulation references
- version differences
- missing items
- contradictions between records

### For each evidence item, identify:
- what it is
- what it proves directly
- what it may suggest
- what weakens it
- whether it is signed, dated, complete, revised, partial, or uncertain
- whether it supports chronology, authorship, circulation, content, or procedure

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

## Step 5: Hand Over to Arabic Legal Analyst

**Action:** After extraction, chronology, and evidence mapping are done, use **Arabic Legal Analyst**.

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
- extraction limitations
- unresolved record gaps

---

## Step 6: Assess Legal Significance Carefully

**Action:** Evaluate the legal significance without overstating certainty.

### Assess, where relevant:
- procedural fairness
- denial of access to evidence
- inability to respond or confront allegations
- evidentiary weakness
- contradiction significance
- authorship/provenance weakness
- document-integrity concerns
- administrative implications
- labor implications
- credibility impact
- significance of missing attachments or missing chronology

### Discipline rules:
- Do not convert suspicion into proof
- Do not assume legal classification that the record does not support
- Do not invent jurisdiction-specific conclusions without support
- Keep conclusions proportional to the evidence
- Make uncertainty visible, not hidden

### Output:
Create a **Legal Significance Summary** showing:
- what matters legally
- why it matters
- what supports that significance
- what remains too weak or incomplete

---

## Step 7: Produce Structured Final Output

**Action:** Generate the final analysis in this exact structure:

### 1. Verified Facts
- include only what is directly supported by the record

### 2. Plausible Inferences
- include cautious reasoned conclusions that are not fully proven

### 3. Unresolved Points
- list contradictions, missing items, ambiguities, and evidentiary gaps

### 4. Legal Significance / Why It Matters
- explain why the strongest points matter legally or procedurally

### 5. Top 3 Critical Points
- identify only the three most outcome-relevant points

### 6. What Proves Each Point
- state the strongest supporting material for each critical point

### 7. What Is Still Missing
- state what additional document, signature, metadata, testimony, chronology, or attachment would materially strengthen each point

### 8. Formal Wording
- provide concise Arabic-first wording suitable for:
  - objection
  - complaint
  - legal summary
  - internal memo
  - case-preparation note

---

## Step 8: Formal Wording Rules

**Action:** Make the closing wording usable in serious legal-style drafting.

### Formal wording standards:
- Arabic-first
- restrained
- evidence-based
- memo-ready
- not exaggerated
- not conclusory beyond the record
- preserves legally meaningful Arabic wording
- suitable for sensitive labor/HR/legal workflows

### The final wording must:
- reflect the actual evidence strength
- avoid certainty inflation
- avoid casual language
- remain usable for follow-up drafting

---

## Required Quality Rules

Before finalizing, verify all of the following:

- [ ] Arabic RTL order was preserved during extraction
- [ ] Extraction limitations were recorded clearly
- [ ] Verified text is separated from interpreted text and uncertain fragments
- [ ] Chronology is organized and source-linked
- [ ] Evidence items are mapped individually
- [ ] Contradictions are identified precisely
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
"Use Document Research Agent to extract this Arabic disciplinary file, then use Arabic Legal Analyst to prepare a cautious summary for an objection memo."

**Workflow should:**
1. inspect the file set
2. extract and validate Arabic content
3. preserve RTL order
4. separate verified extraction from uncertain fragments
5. build chronology
6. map contradictions and evidence gaps
7. hand over to Arabic Legal Analyst
8. produce a structured Arabic-first legal summary with formal wording

---

## Limitations

- This workflow belongs to a **GitHub Copilot agent framework**, not a standalone legal platform
- It does not replace licensed legal advice
- It does not assume live legal databases or runtime infrastructure
- It must remain evidence-aware and uncertainty-aware at every stage

---

**Created:** 2026-04-21 | **Khalid Arabic Legal File Analysis Workflow**
