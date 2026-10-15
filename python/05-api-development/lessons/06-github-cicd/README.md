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
git add python/05-api-development/.github/workflows/python-ci.yml
git add python/05-api-development/lessons/06-github-cicd/README.md
git commit -m "feat: add Python API CI workflow"
git push
```

Adjust the paths if your repository layout differs.

## Next Step

Proceed to production deployment and learn how to configure, deploy, and monitor a FastAPI application safely.