---
icon: material/package-variant-plus
status: published
tags:
    - terminal
    - prompt
---

# :material-package-variant-plus: How to install

The official install guide is available at [https://starship.rs/guide/#🚀-installation](https://starship.rs/guide/#🚀-installation){target="_blank"}

## Install on macOS :simple-macos: using Homebrew :simple-homebrew:

=== "To install - using Homebrew"

    ```bash title="Install on macOS using Homebrew"

    brew install starship

    ```

=== "To install - through zinit"

    ```bash title="Install on macOS using zinint (add into ~/.zshrc)"
    ### --- PROMPT: STARSHIP ---
    # This 'ice' command tells Zinit to:
    # - Download the binary from GitHub releases (as-program)
    # - Pick the 'starship' executable
    # - Run 'starship init zsh' and source the output (atclone/atpull)
    zinit ice as"program" from"gh-r" \
            atclone"./starship init zsh > init.zsh" \
            atpull"%atclone" src"init.zsh"
    zinit light starship/starship

    ```

=== "After install"

    ```bash
    which starship
    ```
    !!! success

        `which starship` should show the full path depending on your installation method.