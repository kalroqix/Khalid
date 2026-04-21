# Copilot Instructions for Project Khalid

## Overview
These instructions guide GitHub Copilot and related agents in contributing to this repository. They define language preferences, project structure, coding conventions, and behavioural constraints.

## Language and Style
- Use English for all code and comments, unless otherwise specified in a particular file.
- Follow consistent naming conventions: use snake_case for variables and functions in Python, camelCase for JavaScript or TypeScript, and PascalCase for classes.
- Write clear, descriptive docstrings or comments for functions and classes to explain their purpose and parameters.
- Do not change the architectural structure of the project or break compatibility without explicit instruction.

## Project Structure Guidelines
- Keep logic, configuration, services, user interface, utilities, and tests in separate folders.
- When adding new modules or files, place them in the appropriate directory.
- If a new feature requires changes to multiple files, summarise the changes and rationale in the pull request.

## Testing
- Before finalising code, ensure tests are updated or added for new functionality.
- Run tests locally and fix failing tests before committing.
- Do not disable or remove existing tests without explanation.

## Security and Secrets
- Do not hardcode credentials, API keys or secrets. Use environment variables or configuration files.
- Avoid exposing sensitive information in logs or error messages.

## Git and Branching
- Always create a new branch for each feature or bug fix.
- Write small, focused commits with clear commit messages.
- Open a pull request and request review when the feature is ready.

## Arabic Language & Right-to-Left (RTL) Text Handling

When working with Arabic content:

### Understanding & Response Quality
- Prioritize deep, accurate understanding of Arabic semantic meaning, not just literal translation.
- Preserve Arabic punctuation, diacritics, and formatting throughout analysis.
- Respect proper names, dates, numeric context, and cultural references in Arabic.
- If responding to Arabic queries, match the user's language preference (Arabic or English response as appropriate).

### Text Extraction & Preservation
- **Never reverse Arabic text order** — maintain correct RTL reading direction (right-to-left).
- Extract Arabic text from PDFs/images in its native reading order.
- When combining Arabic with other languages, preserve each language's directionality.
- Mark any structural changes or reordering clearly to avoid confusion.

### Extraction Accuracy & Uncertainty
- **Distinguish three categories explicitly**:
  1. **Verified extracted text** — Text confirmed by native extraction method
  2. **Inferred interpretation** — Logical interpretation based on context
  3. **Uncertain fragments** — Text that may be damaged, unclear, or ambiguous
- Never guess unclear extracted text without marking the uncertainty explicitly.
- If OCR produces questionable results, note confidence level or fallback to alternative extraction methods.
- Perform structural validation: verify line breaks, word order, and paragraph flow make semantic sense in Arabic.

### Document Extraction Strategy
1. Prefer native text extraction from PDFs (without OCR) as the first option.
2. Use OCR only when native extraction fails or produces incomplete results.
3. Validate extracted Arabic with language and structural checks.
4. Compare extracted text against document metadata (author, title, dates) for plausibility.

## Deep Research & Evidence-Based Analysis

### Research Quality Standards
- Perform evidence-based research: cite sources, link to verifiable information.
- Prefer precise, source-grounded conclusions over speculation.
- When research is needed, state clearly:
  * Which sources were consulted
  * What information was found vs. not found
  * Any conflicting interpretations or gaps in data
- Do not present uncertain information as fact.

### GitHub Code Pattern Discovery

When searching GitHub for code patterns or implementations:

**Search & Ranking Criteria:**
1. **Credibility**: Sort by star count, reliability, and community adoption.
2. **Maintenance**: Prefer recently maintained repositories (active commits in past 3-6 months).
3. **Code Quality**: Look for clean structure, clear variable naming, proper error handling.
4. **Documentation**: Prefer repos with comprehensive README, examples, and API documentation.
5. **Issue Activity**: Active, responsive issue management indicates healthy project.
6. **Relevance**: Match the exact feature or pattern requested, not just tangentially related code.

**Integration Rules:**
- Do not copy code blindly; understand it first.
- Adapt found patterns to the project's conventions and context.
- Explain why the chosen implementation is suitable for the task.
- Credit the original source and respect open-source licenses.
- If no trustworthy match exists on GitHub, say so clearly and build from first principles.

## AI Behaviour
- Ask clarifying questions if the task is ambiguous.
- When making large-scale changes, provide a summary of proposed actions before execution.
- Do not delete files unless explicitly instructed.
- When handling multilingual content (especially Arabic), confirm understanding of cultural and linguistic nuances before proceeding.
