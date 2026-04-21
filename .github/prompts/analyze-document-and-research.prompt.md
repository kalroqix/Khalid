---
name: analyze-document-and-research
description: "Workflow for analyzing documents, extracting Arabic text, performing deep research, searching GitHub for code patterns, and producing structured reports. Use when: extracting from PDFs/images, analyzing Arabic content, researching topics with evidence, or discovering quality code implementations."
context: |
  This prompt guides the Document Research Agent through a systematic workflow for:
  - Document inspection and text extraction
  - Arabic language preservation and RTL formatting
  - Distinction between verified extraction, interpretation, and uncertainty
  - Deep, evidence-based research with citations
  - GitHub code pattern discovery ranked by quality metrics
  - Structured final report generation
---

# Analyze Document and Research Workflow

## Overview

This prompt guides a comprehensive workflow for document analysis, accurate text extraction, evidence-based research, and GitHub code discovery. Follow these steps in order for consistent, high-quality results.

---

## Step 1: Inspect Source & Identify Format

**Action:** Examine the source document/data type

- [ ] **Document Type**: Is this a PDF, image, scanned document, structured file, or web content?
- [ ] **Language(s)**: Identify all languages present (Arabic, English, mixed, etc.)
- [ ] **Format**: Single file, multiple pages, tables, hierarchical structure, mixed content?
- [ ] **Condition**: Is the source clean, degraded, encrypted, or partially corrupted?
- [ ] **Directionality**: Does the document contain RTL (Arabic, Hebrew, Urdu) or LTR (English, French) text?
- [ ] **Special Content**: Charts, images embedded in text, footnotes, annotations, watermarks?

**Output:** Document profile summary

---

## Step 2: Extract Text Carefully

**Action:** Perform accurate text extraction while preserving structure

### Extraction Strategy:

1. **For PDFs (native extraction first):**
   - Attempt native text extraction without OCR
   - Preserve original reading order (RTL for Arabic, LTR for English)
   - Maintain formatting: paragraphs, line breaks, sections
   - Capture metadata if available (author, title, creation date)

2. **For Images (OCR as needed):**
   - If native extraction not available, use OCR as fallback
   - Note OCR confidence level (high/medium/low/uncertain)
   - Validate extracted text against visible structure
   - Flag any garbled, reversed, or questionable portions

3. **For Mixed Content (RTL + LTR):**
   - Preserve language separation and directionality
   - Extract each language block in its native reading direction
   - Document transition points between languages clearly
   - Avoid mixing text directions inappropriately

### Extraction Checklist:

- [ ] Reading order preserved (especially RTL for Arabic)
- [ ] Line breaks and paragraph structure intact
- [ ] Special characters, diacritics, numerals extracted correctly
- [ ] Tables/lists formatted appropriately
- [ ] Headers, footers, and sections identified
- [ ] No reversed or garbled text

**Output:** Extracted text organized by structure

---

## Step 3: Validate Arabic Reading Order & Structure

**Action:** Verify Arabic text correctness (if applicable)

If the document contains Arabic text:

- [ ] **Direction Check**: Confirm all Arabic text flows right-to-left (never left-to-right)
- [ ] **Word Order**: Verify word sequence makes semantic sense in Arabic
- [ ] **Line Breaks**: Check that line breaks don't disrupt word or phrase meaning
- [ ] **Diacritics**: Confirm diacritical marks (tashkeel) are preserved if present
- [ ] **Numerals**: Arabic numerals (٠-٩) and context-appropriate (never ASCII 0-9 where Arabic expected)
- [ ] **Punctuation**: Arabic punctuation marks (،؛؟ etc.) are correct
- [ ] **Names & Dates**: Proper names and temporal expressions are recognizable

### Structural Validation:

- [ ] Paragraphs are coherent and complete
- [ ] Lists maintain logical order
- [ ] Cross-references and citations are intact
- [ ] Tables preserve cell relationships

**Output:** Validation report with confidence assessment

---

## Step 4: Separate Extraction, Interpretation, and Uncertainty

**Action:** Clearly categorize extracted content

For each section or claim, classify as:

### **Category 1: Verified Extracted Text**
- Text confirmed via native PDF extraction or high-confidence OCR
- No ambiguity or damage
- Exactly as it appears in the source
- **Mark with:** ✓ VERIFIED

### **Category 2: Inferred Interpretation**
- Logical deduction based on context
- Combining partial extractions into meaningful units
- Clarifying abbreviations or unclear references
- **Mark with:** ⟷ INTERPRETED

### **Category 3: Uncertain Fragments**
- Text that may be damaged, blurry, or ambiguous
- OCR confidence below threshold
- Unclear without additional context
- Multiple possible readings
- **Mark with:** ⚠ UNCERTAIN [confidence level]

**Example Format:**
```
✓ VERIFIED: Company name is "Al-Farabi Technologies"
⟷ INTERPRETED: "Est. 2015" means established in 2015
⚠ UNCERTAIN [low]: Second word in line 3 appears to be "القانون" or "القانونية" (cannot distinguish clearly)
```

**Output:** Categorized content with clear markings

---

## Step 5: Identify & Extract Key Facts

**Action:** Distill document into key information

Extract:

- [ ] **Main Subject**: What is this document about?
- [ ] **Key Entities**: Important names, organizations, locations, dates
- [ ] **Factual Claims**: Statements that can be verified or researched
- [ ] **Decisions/Recommendations**: What is being decided or recommended?
- [ ] **Numbers & Metrics**: Figures, amounts, percentages, measurements
- [ ] **Temporal Elements**: Dates, timelines, deadlines, effective periods
- [ ] **References**: Citations, links to other documents or sources

**Format as:**
- Bulleted list with category labels
- Use "VERIFIED", "INTERPRETED", or "UNCERTAIN" markers
- Include page numbers or section references where applicable

**Output:** Structured fact extraction

---

## Step 6: Perform Targeted Deep Research (If Needed)

**Action:** Research claims and gather evidence

### When Research is Needed:

- User requested verification of facts
- Document contains claims requiring credibility assessment
- Legal, technical, or financial information that should be current
- References to regulations, standards, or codes
- Quotes or citations requiring source verification

### Research Process:

1. **Identify Research Questions** — What specifically needs verification?
2. **Gather Sources** — Find authoritative, credible sources (official sites, academic, documented)
3. **Evaluate Credibility** — Assess reliability, recency, potential bias
4. **Cross-Reference** — Verify claims across multiple independent sources
5. **Document Findings** — Record source URLs, access dates, findings
6. **Compare to Document** — Note agreements, conflicts, or new information
7. **Report Gaps** — Clearly state what could not be verified

### Research Output Format:

```
📚 RESEARCH FINDING:
  Claim from document: [original statement]
  Sources checked: [list URLs/sources]
  Finding: [VERIFIED / PARTIALLY VERIFIED / CONFLICTING / NOT FOUND]
  Details: [what was found, what wasn't, any conflicts noted]
  Confidence: [HIGH / MEDIUM / LOW / UNKNOWN]
  Citation: [proper source attribution]
```

**Output:** Research findings with citations and confidence levels

---

## Step 7: Search GitHub for Code Patterns (If Applicable)

**Action:** Discover quality code implementations if coding is relevant

### Only if user requested code discovery, such as:
- "Find a library for X"
- "Search for implementations of Y"
- "Find examples of how to do Z"

### Search & Ranking Process:

1. **Define Requirements** — What exact feature/language/framework is needed?
2. **Search GitHub** — Look for multiple implementations, not just first match
3. **Apply Filters** — Use ranking criteria below
4. **Analyze Top Results** — Study 3-5 best options
5. **Compare** — Pros/cons for each top choice
6. **Recommend** — Suggest best fit with justification

### Quality Ranking Criteria (Weighted):

| Criterion | What to Check | Score |
|-----------|--------------|-------|
| **Stars** | 1000+ = 5pts, 100-1000 = 3pts, <100 = 1pt | — |
| **Maintenance** | Last commit <3mo = 5pts, 3-6mo = 3pts, >1yr = 1pt | — |
| **Code Quality** | Clean structure, proper naming, error handling | — |
| **Documentation** | README + API docs + examples = 5pts, partial = 3pts, minimal = 1pt | — |
| **Issues** | Responsive maintainer, resolved issues = 5pts, stale = 1pt | — |
| **License** | Compatible with project = 5pts, unclear/restrictive = 1pt | — |
| **Relevance** | Exact match = 5pts, related = 3pts, tangential = 1pt | — |

### Code Discovery Output Format:

```
🔍 TOP CODE RECOMMENDATIONS:

1. [Repository Name]
   URL: [github.com/...]
   Stars: [number] | Last Updated: [date]
   Quality Score: [calculation]
   Strengths: [what it does well]
   Limitations: [what it doesn't cover]
   License: [license type]
   Why suitable: [explain fit for task]

2. [Alternative option]
   ...
```

**Output:** Ranked code options with comparative analysis

---

## Step 8: Generate Structured Final Report

**Action:** Synthesize all findings into organized, verified report

### Report Structure:

#### **1. Executive Summary**
- 2-3 sentence overview of document and key findings
- Main takeaway or conclusion

#### **2. Source & Methodology**
- Document type and source
- How analysis was performed
- What was examined (full document, specific sections, etc.)
- Languages present and handling approach
- Research methods used (if applicable)

#### **3. Extracted Content**
- Organized by logical sections or categories
- Separated by: VERIFIED | INTERPRETED | UNCERTAIN
- Confidence levels noted
- Original language preserved (especially Arabic—don't over-translate)

#### **4. Key Findings & Insights**
- Main conclusions
- Critical information
- Important decisions or recommendations in the document
- Relationships between facts

#### **5. Evidence & Research Results**
- Citations for verified claims
- Source links with access dates
- Research findings with confidence levels
- Any conflicts noted between document and external sources

#### **6. Gaps & Limitations**
- Information that could not be extracted clearly
- Claims that could not be verified
- Data that appears to be missing or outdated
- Uncertain portions requiring clarification

#### **7. Recommendations or Next Steps**
- What should be done with this information
- Further research or verification needed
- Actionable items
- Required follow-up

### Report Formatting:

- Use clear headings and sections
- Employ bullet points for readability
- Include tables for comparative or complex data
- Highlight key numbers and dates
- Preserve Arabic text in original (with translations if helpful)
- Use visual separators for different confidence levels

**Output:** Structured, comprehensive report

---

## Quality Checklist

Before completing the workflow:

- [ ] All extracted text is accurate and complete
- [ ] Arabic text direction is preserved (RTL not reversed)
- [ ] Verified, interpreted, and uncertain content clearly marked
- [ ] Key facts extracted and organized logically
- [ ] Research conducted and cited where applicable
- [ ] Code options ranked fairly using quality criteria
- [ ] Final report is well-organized and actionable
- [ ] Gaps and limitations explicitly stated
- [ ] Original language preserved (no unnecessary translation)
- [ ] All sources properly credited

---

## Example Output

### For an Arabic Legal Document:

```
📄 DOCUMENT ANALYSIS REPORT

EXECUTIVE SUMMARY:
This is a commercial contract dated 15 March 2025 between Company A and 
Company B for software development services. Key obligations, deliverables, 
and payment terms have been extracted and verified.

SOURCE & METHODOLOGY:
- Type: Arabic PDF contract (10 pages)
- Method: Native PDF extraction + Arabic RTL validation
- Coverage: Full document analyzed
- Confidence: 94% verified, 4% interpreted, 2% uncertain

EXTRACTED KEY TERMS:
✓ VERIFIED: Parties: شركة الفارابي للتقنية (Al-Farabi Tech) & Company B Solutions
✓ VERIFIED: Contract Date: 15 مارس 2025 (March 15, 2025)
✓ VERIFIED: Project Scope: تطوير تطبيق الويب (Web application development)
⟷ INTERPRETED: Duration: 6 months (from start of Phase 1)
⚠ UNCERTAIN: Final payment amount (page 7, second table - OCR confidence 65%)

RESEARCH RESULTS:
Al-Farabi Tech: ✓ Verified as established company, registered 2018
Payment terms reference standard practices: ✓ Confirmed with similar contracts

GAPS & LIMITATIONS:
- Appendix B (technical specifications) partially illegible in original PDF
- Signatory names on final page marked with uncertain confidence (low OCR quality)

RECOMMENDATIONS:
- Request clarification on final payment amount
- Obtain clearer copy of Appendix B for specification review
```

---

**Created:** 2026-04-21 | **Khalid Document Research Workflow**
