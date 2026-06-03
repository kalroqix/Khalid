# GitHub Copilot Setup Guide

This guide will help you set up GitHub Copilot in your IDE, command line, and Windows Terminal.

## 1. IDE Setup - Install the GitHub Copilot Extension

### Visual Studio Code
1. Open VS Code
2. Go to **Extensions** (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "GitHub Copilot"
4. Click **Install** on the official extension by GitHub
5. Sign in with your GitHub account when prompted

### JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.)
1. Open your JetBrains IDE
2. Go to **File → Settings → Plugins** (or **IDE → Preferences → Plugins** on macOS)
3. Search for "GitHub Copilot"
4. Click **Install**
5. Restart your IDE
6. Sign in with your GitHub account

### Neovim
1. Install the Copilot plugin using your plugin manager
2. For vim-plug: Add `Plug 'github/copilot.vim'` to your config
3. Run `:PlugInstall`
4. Run `:Copilot setup` to authenticate

### Other Editors
- **Visual Studio**: Install from the Visual Studio Marketplace
- **Sublime Text**: Install via Package Control
- **Vim**: Use your vim plugin manager

---

## 2. Command Line Setup - Install GitHub Copilot CLI

### Prerequisites
- Node.js (v18 or higher)
- npm or yarn

### Installation Steps

1. **Install the Copilot CLI:**
   ```bash
   npm install -g @github/copilot-cli
   ```

2. **Authenticate:**
   ```bash
   gh copilot auth login
   ```
   This will open your browser to authenticate with GitHub.

3. **Verify Installation:**
   ```bash
   gh copilot --version
   ```

### Using Copilot CLI

**Get help with a command:**
```bash
gh copilot suggest "how to list files recursively"
```

**Explain a command:**
```bash
gh copilot explain "ls -la"
```

---

## 3. Windows Terminal Setup - Connect Copilot with Terminal Chat

### Prerequisites
- Windows Terminal (install from Microsoft Store)
- GitHub Copilot CLI installed (from Step 2)

### Configuration

1. **Open Windows Terminal Settings:**
   - Press `Ctrl+,` or go to **Settings** in the menu

2. **Add a Copilot Profile (Optional):**
   - In `settings.json`, add a new profile or modify your default profile
   - Add Copilot-specific settings if desired

3. **Using Copilot in Terminal:**
   ```bash
   gh copilot suggest "your command here"
   ```

4. **Create a Keyboard Shortcut (Optional):**
   - Add to your Terminal `settings.json`:
   ```json
   {
     "actions": [
       {
         "command": "newTab",
         "keys": "alt+shift+t"
       }
     ]
   }
   ```

---

## Quick Start

### VS Code
- Open any file and start typing
- Copilot will suggest code automatically
- Press `Tab` to accept suggestions
- Press `Escape` to dismiss

### Terminal
```bash
# Get a command suggestion
gh copilot suggest "find all Python files"

# Explain a command
gh copilot explain "grep -r 'pattern' ."
```

---

## Troubleshooting

### Not seeing suggestions in IDE?
- Ensure you're signed in to GitHub
- Check that Copilot is enabled in settings
- Try restarting your IDE

### CLI authentication issues?
- Run `gh auth status` to check your authentication
- Try `gh copilot auth logout` then `gh copilot auth login` again

### Windows Terminal not recognizing commands?
- Verify Node.js is installed: `node --version`
- Verify CLI is installed: `gh copilot --version`
- Restart Windows Terminal after installation

---

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Copilot CLI GitHub Repo](https://github.com/github/copilot-cli)
- [Best Practices for Using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)
