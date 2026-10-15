# Lesson 06 — GitHub Actions CI/CD

## Objective

Automate testing and code-quality checks for the Student Management API using GitHub Actions.

## 1. CI/CD Fundamentals

- **Continuous Integration (CI):** Automatically validate code changes using tests and code-quality checks.
- **Continuous Delivery:** Automatically prepare software for release.
- **Continuous Deployment:** Automatically release validated changes to production.

In this lesson, we implement CI and learn the basics of deployment.

## 2. GitHub Actions Concepts

| Concept | Description |
|---|---|
| Workflow | YAML file defining automation |
| Event | Trigger such as `push` or `pull_request` |
| Runner | Machine executing the workflow |
| Job | Group of related steps |
| Step | Command or reusable action |
| Secret | Encrypted value used for credentials |

Workflows are stored in `.github/workflows/`.

## 3. Workflow Implementation

File: `.github/workflows/python-ci.yml`

The workflow:

1. Checks out repository code.
2. Sets up Python 3.12.
3. Installs dependencies.
4. Checks formatting with Ruff.
5. Runs Ruff linting.
6. Runs tests with pytest.

The workflow runs on relevant pushes and pull requests, and can also be triggered manually.

## 4. Local Validation

Run from the Part 5 directory:

```bash
python -m pip install -r requirements.txt
python -m pip install ruff pytest
ruff format --check .
ruff check .
pytest -v
```

Fix failures locally before pushing.

## 5. Debugging Failed Workflows

1. Open the repository on GitHub.
2. Select **Actions**.
3. Open the failed workflow run.
4. Select the failed job and inspect its logs.
5. Reproduce the failing command locally.
6. Fix the issue, rerun checks, commit, and push.

Common causes include missing dependencies, incorrect paths, formatting errors, failing tests, and missing environment variables.

## 6. Environment Variables and Secrets

Never commit passwords, database credentials, API keys, or production secret keys.

- Keep `.env` out of Git.
- Commit `.env.example` with placeholder values only.
- Store deployment credentials in GitHub repository or environment secrets when needed.
- Configure required environment variables in the test workflow if tests depend on them.

For a production deployment, use a separate production secret key rather than a development value.

## 7. Branch Protection

Branch protection can require pull requests and passing CI checks before changes are merged into a protected branch.

After the workflow has run successfully:

1. Open repository settings.
2. Locate branch protection or rulesets.
3. Configure a rule for your default branch.
4. Require pull requests if appropriate.
5. Require the CI status check before merging.

The exact settings available depend on your GitHub repository and plan.

## 8. Deployment Fundamentals

CI verifies that code is ready; deployment makes the application available to users.

Typical deployment steps include:

1. Choose a hosting platform.
2. Configure production environment variables and secrets.
3. Configure the production database and networking.
4. Start the FastAPI application using a suitable production server configuration.
5. Add health checks, logging, and monitoring.
6. Test the deployed API.

Do not add deployment credentials to the test workflow. Deployment should be a separate, deliberate step.

## 9. Practical Exercise

- [ ] Create `.github/workflows/python-ci.yml`.
- [ ] Configure Python 3.12.
- [ ] Install project dependencies.
- [ ] Add Ruff formatting and lint checks.
- [ ] Run pytest.
- [ ] Push a change and inspect the GitHub Actions run.
- [ ] Intentionally introduce a small test or lint failure in a safe branch, observe the failure, then fix it.
- [ ] Review GitHub Secrets and branch protection options.
- [ ] Explain the difference between CI and deployment.

## 10. Completion Criteria

The lesson is complete when:

- The workflow is visible in GitHub Actions.
- Formatting and lint checks pass.
- Automated tests pass.
- You can locate and diagnose a failed workflow.
- You understand how secrets and branch protection help protect a repository.

## Git Commands

From the repository root:

```bash
git status
git add AI-Learning/.github/workflows/python-ci.yml
git add python/05-api-development/lessons/06-github-cicd/README.md
git commit -m "feat: add Python API CI workflow"
git push
```

Adjust the paths if your repository layout differs.

Great! Now that all your Student Management API tests pass, let's finish Lesson 06 — GitHub Actions CI/CD.

We'll keep the existing practice lessons unchanged and configure CI to check only your standalone project. The workflow will run Ruff formatting, linting, and pytest whenever relevant project code is pushed or a pull request is opened.

## Step 1 — Run the final local checks

From your `AI-Learning` repository root:

```
cd /var/www/html/AI-Learning

cd python/05-api-development

ruff format --check projects/student-management-api/app projects/student-management-api/tests
ruff check projects/student-management-api/app projects/student-management-api/tests
pytest -v
```

All three commands should pass. If Ruff reports issues, fix them only in the standalone project rather than formatting all the practice lessons.

## Step 2 — Create the GitHub Actions workflow

Important: GitHub discovers workflows only from `.github/workflows/` at the repository root. For your repository, use:

`AI-Learning/.github/workflows/python-ci.yml`

If you currently have a workflow inside `python/05-api-development/.github/workflows/`, move it to the repository-level folder.

Create the file:

```
cd /var/www/html/AI-Learning

mkdir -p .github/workflows
touch .github/workflows/python-ci.yml
```

Add this complete workflow:

```

name: Student Management API CI

on:
  push:
    paths:
      - "python/05-api-development/projects/student-management-api/**"
      - "python/05-api-development/pyproject.toml"
      - "python/05-api-development/requirements.txt"
      - ".github/workflows/python-ci.yml"
  pull_request:
    paths:
      - "python/05-api-development/projects/student-management-api/**"
      - "python/05-api-development/pyproject.toml"
      - "python/05-api-development/requirements.txt"
      - ".github/workflows/python-ci.yml"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  test:
    name: Lint and Test API
    runs-on: ubuntu-latest

    defaults:
      run:
        working-directory: python/05-api-development

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r projects/student-management-api/requirements.txt
          pip install ruff pytest

      - name: Check formatting
        run: |
          ruff format --check \
            projects/student-management-api/app \
            projects/student-management-api/tests

      - name: Run lint checks
        run: |
          ruff check \
            projects/student-management-api/app \
            projects/student-management-api/tests

      - name: Run tests
        run: pytest -v

```

This configuration assumes your root `pyproject.toml` contains the pytest settings we added earlier:

```
[tool.pytest.ini_options]
testpaths = ["projects/student-management-api/tests"]
pythonpath = ["projects/student-management-api"]
```

## Step 3 — Commit and push

From the repository root:

```
git status
git add .github/workflows/python-ci.yml
git add python/05-api-development/pyproject.toml
git add python/05-api-development/projects/student-management-api/
git commit -m "ci: automate Student Management API checks"
git push
```

Only stage the files that actually changed. Review `git diff --cached` before committing.

## Step 4 — Verify CI on GitHub

Formatting

Only the standalone project's application and test files are checked.

Linting

Ruff validates only the selected project files.

Tests

Pytest uses the root configuration to discover only the project's tests.

Open your GitHub repository, select Actions, and inspect the `Student Management API CI` run.

One detail to remember: the workflow's `paths` filters control when CI starts, while Ruff's arguments and pytest's configuration control what gets checked.

Once this workflow passes on GitHub, your Lesson 06 CI implementation is complete. The next learning step is deployment: running the FastAPI project in a production-like environment.

## Next Step

Proceed to production deployment and learn how to configure, deploy, and monitor a FastAPI application safely.


