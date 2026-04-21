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

## AI Behaviour
- Ask clarifying questions if the task is ambiguous.
- When making large-scale changes, provide a summary of proposed actions before execution.
- Do not delete files unless explicitly instructed.
