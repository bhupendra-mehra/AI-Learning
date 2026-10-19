# Lesson 02 — Python Packaging and Distribution

## 1. Objective

Learn how to turn reusable Python code into a distributable package that can be installed and used by other Python projects.

By the end of this lesson, you will be able to:

- Understand Python modules, packages, and distributions.
- Organize a Python package using the `src/` layout.
- Configure package metadata using `pyproject.toml`.
- Build a wheel and a source distribution.
- Install and test a package in a clean virtual environment.
- Understand semantic versioning.
- Validate a package before publishing it.
- Understand the basics of publishing to PyPI and TestPyPI.

## 2. Understand the Concepts

### Module versus package versus distribution

| Concept | Meaning | Example |
|---|---|---|
| Module | A Python file containing reusable code | `text.py` |
| Package | A collection of related Python modules | `learning_utils` |
| Distribution | The installable artifact published or shared with others | `learning-utils-demo` |
| Wheel | A built distribution that can be installed using pip | `.whl` |
| Source distribution | An archive containing source files used to build the package | `.tar.gz` |
| `pyproject.toml` | Project metadata and build-tool configuration | Package configuration file |
| PyPI | The Python Package Index, used to distribute Python packages | `pypi.org` |

**Important distinction:** The distribution name used by `pip` does not have to match the Python import name.

For example:

```bash
pip install learning-utils-demo
```

The import could be:

```python
from learning_utils import clean_text
```

## 3. Create the Project Structure

Create a new project inside your `AI-Learning` repository.

```text
python/
└── 06-professional-development-tools/
    └── lessons/
        └── 02-python-packaging/
            ├── README.md
            └── project/
                └── learning-utils-demo/
                    ├── pyproject.toml
                    ├── README.md
                    ├── src/
                    │   └── learning_utils/
                    │       ├── __init__.py
                    │       └── text.py
                    └── tests/
                        └── test_text.py
```

The lesson's `README.md` is this guide. The project's own `README.md` describes the package for future users.

Open a terminal at your repository root and create the folders:

```bash
mkdir -p python/06-professional-development-tools/lessons/02-python-packaging/project/learning-utils-demo/src/learning_utils

mkdir -p python/06-professional-development-tools/lessons/02-python-packaging/project/learning-utils-demo/tests
```

Change into the project directory:

```bash
cd python/06-professional-development-tools/lessons/02-python-packaging/project/learning-utils-demo
```

## 4. Build a Reusable Python Utility

We will build a small text utility package.

### File 1: `src/learning_utils/text.py`

```python
def clean_text(value: str) -> str:
    """Remove leading and trailing whitespace and normalize internal spaces."""
    return " ".join(value.split())


def slugify(value: str) -> str:
    """Convert a string into a simple lowercase hyphen-separated slug."""
    return "-".join(value.lower().split())
```

This package contains two reusable functions.

Example:

```python
from learning_utils import clean_text, slugify

print(clean_text("  Hello    Python  "))
print(slugify("Student Management API"))
```

Expected output:

```text
Hello Python
student-management-api
```

### File 2: `src/learning_utils/__init__.py`

```python
from learning_utils.text import clean_text, slugify

__all__ = ["clean_text", "slugify"]
```

This file exposes the public functions so users can import them directly from `learning_utils`.

### File 3: `tests/test_text.py`

```python
from learning_utils import clean_text, slugify


def test_clean_text_removes_extra_whitespace():
    assert clean_text("  Hello    Python  ") == "Hello Python"


def test_clean_text_handles_empty_string():
    assert clean_text("") == ""


def test_slugify_converts_text():
    assert slugify("Student Management API") == "student-management-api"


def test_slugify_handles_uppercase():
    assert slugify("PYTHON PACKAGING") == "python-packaging"
```

## 5. Configure the Package Using `pyproject.toml`

Create `pyproject.toml` in the project root.

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "learning-utils-demo"
version = "0.1.0"
description = "A small reusable Python utility package for learning packaging"
readme = "README.md"
requires-python = ">=3.10"
license = "MIT"
authors = [
    { name = "Your Name" }
]
dependencies = []

[project.optional-dependencies]
dev = [
    "build",
    "pytest",
    "ruff",
    "twine"
]

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]

[tool.ruff]
line-length = 88
```

Replace `Your Name` with your preferred author name.

### Understand the important fields

- `build-system`: Specifies the tool used to build the package.
- `project.name`: The distribution name used by package installers.
- `project.version`: The current package version.
- `description`: A short summary of the package.
- `readme`: The package description displayed by supported package indexes.
- `requires-python`: The minimum supported Python version.
- `dependencies`: Runtime dependencies; this package has none.
- `optional-dependencies.dev`: Development tools that are not required at runtime.
- `packages.find`: Tells setuptools to discover packages inside `src/`.

The `src/` layout helps prevent Python from accidentally importing your package directly from the project directory when you intend to test the installed distribution.

## 6. Write the Package README

Create `README.md` inside `project/learning-utils-demo/`.

```md
# Learning Utils Demo

A small reusable Python utility package.

## Installation

Install the built package using pip.

## Usage

```python
from learning_utils import clean_text, slugify

print(clean_text("  Hello    Python  "))
print(slugify("Student Management API"))
```

## Functions

- `clean_text(value)`: Normalizes whitespace.
- `slugify(value)`: Converts text into a lowercase hyphen-separated string.

## Version

0.1.0
```

## 7. Create a Virtual Environment and Install Development Tools

From the project root, create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the development dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The `-e` option installs the project in editable mode. It is useful during development, but we will not use it for our final installation test.

Run the tests:

```bash
python -m pytest -v
```

Expected result: all four tests pass.

Run Ruff:

```bash
ruff check .
ruff format --check .
```

Fix any reported issues before proceeding.

## 8. Build the Wheel and Source Distribution

Install the build tools if you have not already:

```bash
python -m pip install build
```

Build the package:

```bash
python -m build
```

The build command should create:

```text
dist/
├── learning_utils_demo-0.1.0-py3-none-any.whl
└── learning_utils_demo-0.1.0.tar.gz
```

The exact archive names may use normalized versions of the distribution name.

### What are these files?

**Wheel (`.whl`)**

A built distribution that pip can install directly. It avoids rebuilding the package from source during a normal installation when a compatible wheel is available.

**Source distribution (`.tar.gz`)**

An archive containing the package's source files and build metadata. It can be used to build a wheel.

List the generated files:

```bash
ls -lh dist/
```

Do not manually edit the generated files inside `dist/`.

## 9. Validate the Distributions

Run the package metadata checks:

```bash
python -m twine check dist/*
```

Resolve any errors before distributing the package.

Inspect the wheel contents:

```bash
python -m zipfile -l dist/learning_utils_demo-0.1.0-py3-none-any.whl
```

Inspect the source archive:

```bash
tar -tzf dist/learning_utils_demo-0.1.0.tar.gz
```

Confirm that the package modules and metadata are included.

## 10. Test the Built Wheel in a Clean Environment

This is the most important exercise in the lesson.

The goal is to verify that the built artifact can be installed independently of the editable development installation.

### Step 1 — Leave the development environment

```bash
deactivate
```

### Step 2 — Create a clean environment

From the package project root:

```bash
python3 -m venv /tmp/learning-utils-test
source /tmp/learning-utils-test/bin/activate
```

On Windows, create and activate a separate virtual environment using your usual PowerShell commands.

### Step 3 — Install the wheel

On Linux or WSL:

```bash
python -m pip install dist/learning_utils_demo-0.1.0-py3-none-any.whl
```

If the generated filename differs, use the actual wheel filename shown in `dist/`.

### Step 4 — Test the installed package outside the source directory

Move outside the package project directory:

```bash
cd /tmp
```

Run:

```bash
python -c "from learning_utils import clean_text, slugify; print(clean_text('  Hello    Python  ')); print(slugify('Student Management API'))"
```

Expected output:

```text
Hello Python
student-management-api
```

Check where the package is imported from:

```bash
python -c "import learning_utils; print(learning_utils.__file__)"
```

The location should point to the clean environment's installed packages, not your project's `src/` directory.

**Completion check:** If the package imports and both functions work in this clean environment, the built wheel is usable independently of your development setup.

Deactivate and remove the temporary environment when finished:

```bash
deactivate
rm -rf /tmp/learning-utils-test
```

Only run the removal command if you have confirmed that `/tmp/learning-utils-test` is the temporary environment created for this exercise.

## 11. Understand Semantic Versioning

A common versioning convention is:

`MAJOR.MINOR.PATCH`

For example, `1.4.2` means:

| Component | Meaning | Example change |
|---|---|---|
| MAJOR | Breaking changes | Remove or change an existing public function |
| MINOR | Backward-compatible functionality | Add a new public function |
| PATCH | Backward-compatible bug fixes | Correct an existing function's behavior |

For this package, we started at `0.1.0` because it is an initial learning release.

Try these exercises:

1. Add a new function that capitalizes a string and increment the minor version to `0.2.0`.
2. Fix a bug without changing the public interface and increment the patch version.
3. Consider a breaking API change and explain why it might require a major version increase after the package reaches a stable `1.0.0` release.

Update the version in `pyproject.toml` before rebuilding.

When testing a new version, clean old build artifacts first:

```bash
rm -rf build dist src/*.egg-info
python -m build
```

Then repeat the clean-environment installation test with the newly generated wheel.

## 12. Understand Publishing to PyPI

PyPI is the public Python Package Index. Publishing makes a package available for other developers to install using pip.

TestPyPI is a separate test index for practising the publishing workflow.

Official references:

- PyPA packaging guide: https://packaging.python.org/en/latest/tutorials/packaging-projects/
- Build and distribution: https://packaging.python.org/en/latest/guides/section-build-and-publish/
- PyPI: https://pypi.org/
- TestPyPI: https://test.pypi.org/

### Before publishing

- Choose a unique distribution name.
- Confirm the version is correct and has not already been released.
- Include accurate package metadata and documentation.
- Build and validate both distributions.
- Test installation in a clean environment.
- Check licensing and ensure you have permission to distribute the code.
- Keep publishing credentials and API tokens out of source control.

### Optional publishing practice

For a future release, you can practise uploading the artifacts to TestPyPI with Twine after creating and configuring a TestPyPI account.

```bash
python -m twine upload --repository testpypi dist/*
```

Use a TestPyPI API token when prompted, following the official instructions. Do not use your real PyPI credentials for TestPyPI.

This command uploads artifacts to TestPyPI. It is not necessary for completing this lesson, and you should not upload this demonstration package to the public PyPI index merely to finish the exercise.

## 13. Troubleshooting

### `No module named build`

Install the build tool:

```bash
python -m pip install build
```

### `No module named twine`

Install Twine:

```bash
python -m pip install twine
```

### `No module named learning_utils`

Check that:

- The package has an `__init__.py` file.
- Package discovery in `pyproject.toml` points to `src`.
- The wheel was built successfully.
- You installed the wheel into the active environment.
- You are testing outside the source directory.

### Old version appears after rebuilding

Remove old artifacts, rebuild, and install the newly generated wheel. Ensure that the wheel filename matches the version you intend to test.

### Build fails because of invalid metadata

Review the `pyproject.toml` syntax, required metadata, README path, and build configuration.

## 14. Final Practical Exercise

Complete this workflow without copying commands blindly:

1. Build the `learning-utils-demo` package.
2. Run all tests.
3. Run Ruff checks.
4. Generate the wheel and source distribution.
5. Validate both distributions using Twine.
6. Install the wheel in a clean virtual environment.
7. Import and execute both utility functions outside the source directory.
8. Change the package version and rebuild it.
9. Explain the difference between installing a package, building a package, and publishing a package.
10. Document the commands and successful results in your project README.

## 15. Completion Checklist

- [ ] Understand modules, packages, and distributions.
- [ ] Created the `src/` package structure.
- [ ] Configured `pyproject.toml`.
- [ ] Implemented reusable utility functions.
- [ ] Wrote and passed pytest tests.
- [ ] Passed Ruff checks.
- [ ] Built a wheel and source distribution.
- [ ] Validated distributions with Twine.
- [ ] Installed the wheel in a clean virtual environment.
- [ ] Verified imports outside the source directory.
- [ ] Understood semantic versioning.
- [ ] Reviewed the PyPI and TestPyPI publishing workflow.

## Completion Criteria

Build a reusable Python package, validate its distributions, install and test the built wheel in a clean environment, and explain how package versioning and publishing work.

## Part 6 — Completion Summary

After finishing Lessons 01 and 02 of the revised Part 6 plan, you should be able to:

- Use Git and GitHub in your development workflow.
- Understand branching and pull requests.
- Write automated tests and maintain code quality.
- Package reusable Python code.
- Build and validate Python distributions.
- Understand versioning and package publishing.
- Containerize and deploy Python applications.

**Part 6 is complete once the packaging checklist is satisfied.** The next stage is to continue with your existing AI roadmap rather than repeating the Git, testing, Docker, or deployment topics already covered.
