---
icon: material/head-question
tags:
  - vscode
  - cli
status: published
---

# :material-head-question: How To launch VS Code CLI on macOS

To launch the Visual Studio Code command line interface (CLI) on macOS, follow these steps:

1. **Open Visual Studio Code**: Start by launching the Visual Studio Code application on your macOS.
2. **Open the Command Palette**: Press `Cmd + Shift + P` to open the Command Palette.
3. **Install 'code' Command in PATH**: Type `Shell Command: Install 'code' command in PATH` and select it from the dropdown. This will add the `code` command to your system PATH.
4. **Restart Terminal**: Close and reopen your terminal to ensure the changes take effect.
5. **Verify Installation**: In your terminal, type `code --version` to verify that the `code` command is now available.

!!! info "Behind the Scenes"

    VS Code will add a symbolic link to the `code` command in `/usr/local/bin`, which is a directory included in your system's PATH by default.
