# **🔱 VS Code Extensions Setup**

This workflow explains how to set up VS Code extensions on a **new virtual machine or remote environment** (e.g., a Coder/code-server instance) when **automatic Settings Sync via GitHub is not available**.

> For machines where you are logged in with GitHub, extensions will sync automatically. This guide is only needed for manual installation.

---

## **1. Prepare the extension list**

Create a file named `vs_code_extensions.txt` in the root directory of your workspace.

- Each line should contain **one VS Code extension ID**.
- Lines starting with `#` can be used as **comments** and will be ignored.
- Example:

```text
- ms-python.python  # Python
- PKief.material-icon-theme  # Material Icon Theme
```

## **2. Install or uninstall extensions via command line**

Run the following command in the terminal inside your VS Code or Coder environment:

**✅ Install all extensions**

```bash
CODE_CMD=$(which code-server) && \
  grep '^- ' vs_code_extensions.txt | \
  sed -n 's/^- *//;s/[[:space:]]*#.*//;s/^[[:space:]]*//;s/[[:space:]]*$//p' | \
  xargs -L 1 "$CODE_CMD" --install-extension
```

**❌ Uninstall all extensions**

```bash
CODE_CMD=$(which code-server) && \
  grep '^- ' vs_code_extensions.txt | \
  sed -n 's/^- *//;s/[[:space:]]*#.*//;s/^[[:space:]]*//;s/[[:space:]]*$//p' | \
  xargs -L 1 "$CODE_CMD" --uninstall-extension
```

**Command breakdown**

| Part                                                                         | Explanation                                                                                                     |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `CODE_CMD=$(which code-server)`                                              | Automatically detects the path to the `code-server` binary on your environment.                                 |
| `grep '^- ' vs_code_extensions.txt`                                          | Selects only lines starting with `- ` (the actual extension entries), ignoring headings, emojis, or other text. |
| `sed -n 's/^- *//;s/[[:space:]]*#.*//;s/^[[:space:]]*//;s/[[:space:]]*$//p'` | Removes the leading dash, strips inline comments, and trims leading/trailing whitespace.                        |
| `xargs -L 1 "$CODE_CMD" --install-extension`                                 | Passes each cleaned extension ID to `code-server --install-extension` (or `--uninstall-extension`) one by one.  |

> ✅ This ensures only valid extension IDs are processed, ignoring headings, emojis, comments, and blank lines, making it safe to run multiple times.
