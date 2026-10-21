Perfect! 👍

This is actually a **great learning opportunity**.

Many beginners would just install it without understanding **why**.

Let's understand what's happening.

---

# Why did this happen?

You ran:

```bash
pip3 --version
```

Linux replied:

```text
Command 'pip3' not found...
```

This means:

* ✅ Python is installed.
* ❌ pip is not installed (or not available in your current environment).

Think of it like Magento.

Imagine you run:

```bash
composer install
```

and Linux says:

```text
composer: command not found
```

Does that mean PHP is broken?

**No.**

It simply means **Composer is not installed**.

The same thing is happening here.

---

# What is pip?

Before installing it, I want you to understand it.

Suppose tomorrow we want to use OpenAI.

Can Python talk to OpenAI by itself?

Yes, but it would require a lot of manual HTTP code.

Instead, OpenAI provides a library.

How do we install that library?

Using **pip**.

Think of it like this:

| Magento/PHP                      | Python             |
| -------------------------------- | ------------------ |
| Composer                         | pip                |
| composer.json                    | requirements.txt   |
| composer require monolog/monolog | pip install openai |
| vendor/                          | site-packages      |

So:

```bash
composer require magento/module-catalog
```

is conceptually similar to:

```bash
pip install openai
```

You're not installing Python itself. You're installing an additional package.

---

# Let's Install pip

Run these commands **one by one**.

## Step 1

Update package information:

```bash
sudo apt update
```

### Why?

Think of it as refreshing the package catalog before installing software.

It's similar in spirit to refreshing package metadata before installing dependencies.

---

## Step 2

Install pip:

```bash
sudo apt install python3-pip
```

Linux may ask:

```text
Do you want to continue? [Y/n]
```

Type:

```text
Y
```

and press **Enter**.

---

## Step 3

Verify the installation:

```bash
pip3 --version
```

Expected output:

```text
pip 24.x.x from ...
```

---

# What is `sudo`?

Since you're new to Linux, let's learn this properly.

Suppose you're working in Magento.

Can a normal customer install PHP?

No.

Only an administrator can.

Linux works the same way.

```text
Normal User

↓

Cannot install system software

Administrator (root)

↓

Can install software
```

`sudo` means:

> **Run this command with administrator privileges.**

Think of it like:

```text
Admin Permission

↓

Install Package
```

Without `sudo`, Linux protects your system.

---

# Your Homework (5 minutes)

Run:

```bash
sudo apt update
```

Then:

```bash
sudo apt install python3-pip
```

Finally:

```bash
pip3 --version
```

Paste **all three outputs** here.

---

## One More Thing (Professional Practice)

Since we're building this as a real developer course, I want us to follow one important principle:

> **Never copy-paste commands without understanding what they do.**

For every command, we'll answer:

1. **What does this command do?**
2. **Why do we need it?**
3. **What's the Magento/PHP equivalent?**

That way, you'll understand your environment instead of just getting it working. This habit will help you far beyond AI development.
