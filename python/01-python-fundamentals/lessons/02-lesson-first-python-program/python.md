Install Python (Windows 11 + WSL Ubuntu)

## Goal

Install and verify Python inside **WSL Ubuntu**.

> **Note:** We are **not** installing Python on Windows. Since you'll build AI applications inside WSL (just like you develop Magento), Python should also be installed there.

---

## Step 1 – Open WSL

Open your Ubuntu terminal.

Verify you're in WSL:

```bash
pwd
```

Expected output:

```text
/home/ubuntu
```

### What does this command do?

Displays your current working directory.

### Why do we run it?

To confirm you're working inside WSL and not in Windows Command Prompt or PowerShell.

### Magento Equivalent

Similar to checking that you're logged into the correct Magento server before running commands.

---

## Step 2 – Update Ubuntu Package Information

### Command

```bash
sudo apt update
```

### What does this command do?

Refreshes Ubuntu's package list.

### Why do we need it?

Before installing any software, Ubuntu should know the latest available package versions.

### Magento Equivalent

Conceptually similar to refreshing package metadata before installing dependencies.

---

## Step 3 – Check Whether Python Is Already Installed

### Command

```bash
python3 --version
```

### Expected Output

```text
Python 3.12.3
```

### What does this command do?

Displays the installed Python version.

### Why do we need it?

We should always verify whether Python is already installed before attempting to install it.

### Your Result

```text
Python 3.12.3
```

✅ **Python is already installed.**

> **Conclusion:** You do **not** need to install Python.

---

## Step 4 – Install Python (Only If Step 3 Fails)

If the previous command returns:

```text
python3: command not found
```

then install Python using:

```bash
sudo apt install python3
```

When prompted:

```text
Do you want to continue? [Y/n]
```

Type:

```text
Y
```

and press **Enter**.

---

## Step 5 – Verify the Installation

Run:

```bash
python3 --version
```

Expected output:

```text
Python 3.x.x
```

This confirms Python has been installed successfully.

---

# Lesson Summary

You learned:

* How to verify you're working inside WSL.
* How to refresh Ubuntu's package list.
* How to check whether Python is installed.
* How to install Python if it's missing.
* How to verify the installation.

---

## Current Status

| Step                  | Status          |
| --------------------- | --------------- |
| WSL Working           | ✅               |
| Python Installed      | ✅ Python 3.12.3 |
| Ready for Next Lesson | ✅               |

---

From the next lesson onward, we'll install **pip** (Python's package manager), but only after understanding **what it is, why it's needed, and how it's similar to Composer in PHP**. We won't install anything without first understanding its purpose.
