# Khalid – AI Agent Coordination Framework

**Khalid** is a configuration-based framework for coordinating GitHub Copilot agents and prompts. It enables structured, multi-agent collaboration for software development with specialized roles: Planning, Building, and Reviewing.

## 🎯 Purpose

Khalid provides a reusable system for GitHub Copilot to work in coordinated teams on your projects. Instead of one generic AI assistant, you get:

- **Planner** — Analyzes requirements and creates detailed work breakdowns
- **Builder** — Implements code changes, writes tests, ensures quality
- **Reviewer** — Audits code, identifies bugs, suggests improvements

Plus a **Project Operator** agent to manage Khalid itself.

## 📋 Core Components

### Agents (`.github/agents/`)

| Agent | Purpose | When to Use |
|-------|---------|------------|
| **Planner** | Plans work and breaks requirements into logical subtasks | Starting a feature, breaking down complex requirements |
| **Builder** | Implements code changes, writes tests, runs validation | Implementing planned work, fixing bugs, building features |
| **Reviewer** | Reviews code, checks standards, identifies issues | Before merging, validating quality, refactoring sessions |
| **Operator** | Manages Khalid repository, coordinates agents, improves framework | Maintaining Khalid, adding new agents/prompts |
| **Document Research** | Analyzes documents, extracts Arabic text, performs deep research, finds code on GitHub | Extracting from PDFs/images, researching topics, discovering code patterns, Arabic intelligence |

### Prompts (`.github/prompts/`)

| Prompt | Workflow |
|--------|----------|
| **build-feature** | Implement new features end-to-end |
| **debug-bug** | Identify and fix bugs systematically |
| **review-refactor** | Review code and suggest refactoring |
| **analyze-document-and-research** | Extract from documents, perform deep research, discover code patterns |

### Instructions (`copilot-instructions.md`)

Global guidelines for all agents:
- Code style preferences (Python: snake_case, JavaScript: camelCase, etc.)
- Project structure standards
- Testing requirements
- Security practices
- Git workflow conventions

## 🚀 Quick Start

### 1. **Activate Khalid in Your Project**

Copy the Khalid agents and prompts to your project's `.github/` directory:

```bash
# In your project
cp -r /path/to/Khalid/.github/agents .github/
cp -r /path/to/Khalid/.github/prompts .github/
cp /path/to/Khalid/copilot-instructions.md .
```

Or create a symbolic reference to keep Khalid centralized.

### 2. **Use in VS Code with GitHub Copilot**

In your chat:
- Type `/` to see available agents and prompts
- Select the Planner to break down your work
- Use the Builder to implement planned tasks
- Invoke the Reviewer to audit code quality

### 3. **Example Workflow**

```
1. User: "I need to add user authentication to my app"
2. Invoke: /Planner
   → Creates breakdown: schema changes, API endpoints, tests, UI
3. For each task, invoke: /Builder
   → Implements changes, updates tests, runs suite
4. Final: /Reviewer
   → Audits code quality, security, test coverage
```

## 📝 Using Khalid Agents in Chat

### Planner Agent

```
You: "Plan how to add dark mode support to our React app"

Planner will:
- Identify affected components
- Break work into subtasks
- Suggest test changes needed
- Ask clarifying questions if needed
```

### Builder Agent

```
You: "Implement the color scheme provider (following the plan above)"

Builder will:
- Create/modify files as needed
- Write unit tests
- Run the test suite
- Summarize changes and results
```

### Reviewer Agent

```
You: "Review the dark mode implementation for bugs and improvements"

Reviewer will:
- Check code quality
- Identify issues
- Suggest security/performance improvements
- Recommend additional tests
```

## 🌍 Arabic Language & Document Intelligence

Khalid now includes specialized capabilities for Arabic language processing and document analysis:

### Arabic-First Understanding

When working with Arabic content, the Document Research Agent:
- Preserves Arabic semantic meaning and cultural context
- Maintains right-to-left (RTL) text direction throughout extraction and analysis
- Respects proper names, dates, numerics, and punctuation
- Never reverses Arabic text order or breaks formatting

### Document Text Extraction

The Document Research Agent can:
- Extract text from PDFs accurately (preferring native extraction over OCR)
- Identify extraction barriers (encryption, image-only, degraded quality)
- Preserve document structure, formatting, and hierarchy
- Distinguish **verified extraction** (confirmed via native method) from **interpreted** text (inferred) and **uncertain** fragments (ambiguous/unclear)

### Deep Research & Evidence

When researching topics:
- Performs evidence-based, source-grounded research with citations
- Cross-references multiple sources to verify claims
- Clearly marks confidence levels and identifies gaps
- Cites all sources and access dates

### GitHub Code Pattern Discovery

When searching for code implementations:
- Filters repositories by quality metrics (stars, maintenance, code quality, documentation)
- Ranks results by credibility, recent maintenance, and practical relevance
- Provides multiple options with comparative pros/cons analysis
- Explains why recommended implementations are suitable for the task

### Document Research Workflow

Use the **analyze-document-and-research** prompt to guide a systematic workflow:
1. Inspect and identify document format
2. Extract text carefully with validation
3. Validate Arabic reading order and structure (if applicable)
4. Separate verified extraction from interpretation and uncertainty
5. Identify key facts and entities
6. Perform targeted deep research where needed
7. Search GitHub for relevant code patterns (if coding involved)
8. Generate structured final report with citations and confidence levels

### Limitations & Transparency

- **Not a runtime platform:** Khalid is a GitHub Copilot agent framework, not a Python/Node.js/Docker runtime
- **Requires GitHub Copilot:** All capabilities depend on GitHub Copilot Chat in VS Code
- **AI-assisted accuracy:** While Document Research agents are designed for precision, always verify critical information independently
- **OCR limitations:** Scanned documents with poor quality may require manual review
- **Language complexity:** Very specialized Arabic dialects or historical texts may require domain expert review
- **Code discovery limitations:** GitHub search reflects available public repositories; not all code is published

## 📝 Using the Document Research Agent in Chat

### Example: Extract Arabic Contract

```
You: "Extract the key terms from this Arabic commercial contract PDF"

Document Research Agent will:
- Inspect the PDF structure
- Extract text while preserving Arabic RTL order
- Identify verified vs. uncertain sections
- Extract key dates, parties, amounts, deliverables
- Return structured extraction with confidence levels
```

### Example: Research & Verify

```
You: "Research whether the company name and registration date in this document are accurate"

Document Research Agent will:
- Extract company name and date from document
- Search for official records or verification sources
- Cross-reference findings
- Report what was verified, conflicts found, or gaps
- Provide source citations and confidence levels
```

### Example: Find Code on GitHub

```
You: "Find a well-maintained Arabic text extraction library for PDFs"

Document Research Agent will:
- Search GitHub for relevant libraries
- Rank by stars, maintenance status, documentation quality
- Compare top 3 options with pros/cons
- Recommend the best match with explanation
```

## 🔧 Extending Khalid

### Add a New Agent

1. Create `.github/agents/my-agent.agent.md`
2. Define frontmatter (name, description)
3. Write the agent's role, scope, and operating instructions
4. Update `README.md` with the new agent
5. Commit with a clear message

### Add a New Prompt

1. Create `.github/prompts/my-task.prompt.md`
2. Define frontmatter (name, description, context)
3. Write the prompt workflow as numbered steps
4. Update `README.md` to reference it
5. Commit with a clear message

### Improve Instructions

1. Edit `copilot-instructions.md`
2. Update guidelines based on your team's standards
3. Test with agents in your project
4. Commit with explanation of changes

## 📊 Repository Structure

```
Khalid/
├── .github/
│   ├── agents/
│   │   ├── planner.agent.md            ← Plan work & subtasks
│   │   ├── builder.agent.md            ← Implement code
│   │   ├── reviewer.agent.md           ← Review code quality
│   │   ├── operator.agent.md           ← Manage Khalid
│   │   └── document-research.agent.md  ← Arabic & document intelligence
│   ├── prompts/
│   │   ├── build-feature.prompt.md
│   │   ├── debug-bug.prompt.md
│   │   ├── review-refactor.prompt.md
│   │   └── analyze-document-and-research.prompt.md
│   └── workflows/
│       └── blank.yml                   ← CI/CD template
├── copilot-instructions.md             ← Global AI guidelines
└── README.md                            ← This file
```

## 🔄 Git Workflow

All changes to Khalid use standard GitHub practices:

1. **Create a feature branch:** `git checkout -b feature/agent-name`
2. **Make changes** to agents, prompts, or instructions
3. **Commit with clear messages:** `git commit -m "Add security-audit agent"`
4. **Push and create a PR:** `git push origin feature/agent-name`
5. **Merge after review** to `main`

## 🛠️ Maintaining Khalid

Use the **Operator** agent for:
- Auditing repository integrity
- Adding new agents or prompts
- Fixing configuration issues
- Improving documentation
- Managing CI/CD workflows

## 📚 Best Practices

- **Clear agent descriptions** — Help users know when to invoke each agent
- **Descriptive prompts** — Each prompt should explain what workflow it supports
- **Consistent style** — Agents and prompts follow YAML frontmatter conventions
- **Tested on real projects** — Validate agents/prompts in actual codebases before committing
- **Keep instructions updated** — Reflect your team's evolving standards

## 🤝 Contributing

To contribute improvements to Khalid:

1. Clone the repository
2. Create a feature branch
3. Test your changes (agents, prompts, instructions)
4. Submit a PR with clear description
5. Engage in review process

## 📖 Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)
- [Khalid Agent Customization Guide](./agent-customization-guide.md) (coming soon)

---

**Project Khalid** — Structured AI collaboration for better code. 🚀

*Last Updated: 2026-04-21*