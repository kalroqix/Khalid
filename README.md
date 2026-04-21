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

### Prompts (`.github/prompts/`)

| Prompt | Workflow |
|--------|----------|
| **build-feature** | Implement new features end-to-end |
| **debug-bug** | Identify and fix bugs systematically |
| **review-refactor** | Review code and suggest refactoring |

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
│   │   ├── planner.agent.md       ← Plan work & subtasks
│   │   ├── builder.agent.md       ← Implement code
│   │   ├── reviewer.agent.md      ← Review code quality
│   │   └── operator.agent.md      ← Manage Khalid
│   ├── prompts/
│   │   ├── build-feature.prompt.md
│   │   ├── debug-bug.prompt.md
│   │   └── review-refactor.prompt.md
│   └── workflows/
│       └── blank.yml              ← CI/CD template
├── copilot-instructions.md        ← Global AI guidelines
└── README.md                       ← This file
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