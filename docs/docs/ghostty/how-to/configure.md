---
icon: octicons/package-dependents-16
status: published
tags:
    - terminal
    - emulator
---

# :octicons-package-dependents-16: How to configure

> Ghostty supports hundreds of configuration options to make it look and behave exactly how you want.

The official Configuration guide is available on [**https://ghostty.org/docs/config**](https://ghostty.org/docs/config){target="_blank"}.

## Configuration File Location

The configuration file is a plain text file that uses the [TOML](https://toml.io/en/){target="_blank"} format and is called **`config`**.

By default, Ghostty looks for a configuration file at the following location across all OS platforms:

- `$XDG_CONFIG_HOME/ghostty/config`
- if `XDG_CONFIG_HOME` is not defined, it defaults to `$HOME/.config/ghostty/config`

For **macOS-specific Path** (macOS only):

- `$HOME/Library/Application\ Support/com.mitchellh.ghostty/config`
- macOS also supports the XDG configuration path mentioned above.

If both locations exist, they are loaded in the order above with conflicting values in later files overriding earlier ones. Configuration is optional and if no configuration file is found, Ghostty will use its defaults.

## My Ghostty configuration

```toml title="~/.config/ghostty/config" linenums="1"

theme = Dracula

font-family = "JetBrains Mono Nerd Font Mono"
font-size = 14

focus-follows-mouse = true

cursor-style = block
cursor-style-blink = true

right-click-action = copy-or-paste
copy-on-select = clipboard

window-padding-x = 10
window-padding-y = 10
window-decoration = true
window-height = 40
window-width = 80

window-colorspace = "display-p3"
window-padding-balance = true
window-save-state = always


background-opacity = 0.92
background-blur = 18

macos-option-as-alt = true
macos-titlebar-style = transparent


shell-integration = zsh
shell-integration-features = cursor, title

# Ensure Home/End are passed as standard xterm sequences
keybind = home=text:\x1b[H
keybind = end=text:\x1b[F

```



