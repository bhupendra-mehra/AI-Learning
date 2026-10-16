# Lesson 09 — Deployment

## Objective

Deploy the Dockerized Student Management REST API to a cloud hosting platform, configure environment variables securely, verify its endpoints, and understand the difference between a learning deployment and production hosting.

## Prerequisites

- Lessons 01–08 completed.
- Student Management API working locally.
- Docker and Docker Compose installed.
- Dockerized API tested successfully.
- Project committed and pushed to GitHub.
- GitHub Actions tests and Ruff checks passing.
- A Render account: https://render.com/

## 1. Understand the Deployment Flow

The deployment process follows this flow:

```text
Local Development
       |
       v
Student Management API
       |
       v
Dockerfile and Dependencies
       |
       v
GitHub Repository
       |
       v
Render Builds Docker Image
       |
       v
Cloud Web Service
       |
       v
Public HTTPS API URL
```

Render can build and deploy a Dockerized application from a connected GitHub repository. It also supports automatic deployments when changes are pushed to the configured branch.

Reference: https://render.com/docs/web-services

## 2. Prepare the Dockerfile

Open:

`python/05-api-development/projects/student-management-api/Dockerfile`

Update the final command so the application uses the port provided by the hosting platform.

```dockerfile
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
```

Keep the other Dockerfile instructions unchanged.

### Why is this required?

- `0.0.0.0` allows the application to receive external traffic through the container.
- `PORT` allows the hosting platform to provide the listening port.
- `8000` is the fallback for local Docker execution.

Save the file and verify that the API still works locally.

```bash
docker compose config
docker compose build
docker compose up -d
docker compose ps
```

Verify:

- `http://localhost:8000/docs`
- `http://localhost:8000/health`

Check the logs if anything fails:

```bash
docker compose logs api
```

## 3. Verify the Application Configuration

Before deploying, confirm that the application reads configuration from environment variables.

Check `app/database.py` and `app/auth.py` to verify that the database URL and secret key are not hardcoded.

The application should use the configured database URL and secret key supplied through the environment.

### Environment variables

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Signs and validates JWT tokens |
| `DATABASE_URL` | Configures the database connection |

Generate a secure secret locally:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the generated value for use in Render.

**Security rules**

- Never commit `.env` to Git.
- Never place real secrets in the Dockerfile.
- Never publish your JWT signing secret in documentation or screenshots.
- Use environment variables for deployment configuration.

## 4. Push the Changes to GitHub

Run these commands from the root of your `AI-Learning` repository.

```bash
git status
git add python/05-api-development/projects/student-management-api/Dockerfile
git diff --cached
git commit -m "chore: prepare API for deployment"
git push
```

If your working branch is not the default branch, push the branch you intend to deploy.

Confirm that GitHub Actions passes before deploying.

## 5. Create a Render Web Service

### Step 1 — Connect GitHub

1. Sign in to Render.
2. Connect your GitHub account if it is not already connected.
3. Select **New → Web Service**.
4. Select your `AI-Learning` repository.
5. Authorize access to the private repository if requested.

### Step 2 — Configure the service

Use the following settings.

| Setting | Value |
|---|---|
| Service name | `student-management-api` |
| Branch | Your chosen deployment branch |
| Runtime | Docker |
| Root directory | `python/05-api-development/projects/student-management-api` |
| Dockerfile path | `Dockerfile` |
| Instance type | Free, for learning purposes |

The root directory is important because your Dockerfile and `requirements.txt` are inside the standalone project directory rather than the repository root.

If the Render dashboard displays additional Docker build settings, confirm that the Docker build context points to the project directory.

### Step 3 — Configure environment variables

In the service's environment-variable settings, add:

| Key | Value |
|---|---|
| `SECRET_KEY` | The generated secret from Step 3 |
| `DATABASE_URL` | `sqlite:////tmp/student_management.db` |

The database URL above is for this temporary learning deployment only. Use it only if the application supports the supplied SQLite URL and the configured database directory is writable.

Do not upload your local `.env` file.

### Step 4 — Deploy

1. Click **Create Web Service**.
2. Wait for the Docker image to build.
3. Review the deployment logs.
4. Wait until Render reports that the service is live.
5. Copy the public service URL.

Your URL will look similar to:

`https://your-service-name.onrender.com`

Use the actual URL shown by Render; do not copy the example literally.

## 6. Verify the Deployed API

Replace `YOUR_RENDER_URL` with your actual service URL.

### Health check

Open:

`https://YOUR_RENDER_URL/health`

Expected result: a successful response from your health-check endpoint.

### API documentation

Open:

`https://YOUR_RENDER_URL/docs`

Confirm that the FastAPI Swagger UI loads and displays your API routes.

### Test the API

Using Swagger UI:

1. Register a test user.
2. Log in with the registered credentials.
3. Copy the access token returned by the login endpoint.
4. Click **Authorize** and provide the token using the format expected by your API.
5. Access the current-user endpoint.
6. Create a student.
7. Retrieve the student.
8. Update the student.
9. Delete the test student.

Confirm that successful requests return the expected responses and that invalid or unauthenticated requests are handled correctly.

You can also use `curl` for the health check:

```bash
curl -i https://YOUR_RENDER_URL/health
```

## 7. Understand Database Persistence

Your local Docker Compose setup uses a named volume to preserve SQLite data across container restarts.

Cloud hosting introduces a different concern: the service's local filesystem may be temporary.

Render Free web services can spin down after 15 minutes without traffic, and their local filesystem changes are lost when the service restarts, spins down, or redeploys.

Therefore, the SQLite database configured for this learning deployment may lose its records.

**Important:** Do not store real user information or rely on this deployment for durable records.

For a more production-oriented deployment, use a managed PostgreSQL database, configure the application's SQLAlchemy connection for PostgreSQL, and implement the necessary schema migrations. A database's own retention, backup, and pricing policies must also be checked before choosing it.

References:

- https://render.com/docs/free
- https://render.com/docs/deploys

## 8. Test Automatic Deployment

After the initial deployment succeeds:

1. Make a small, harmless change to the project README.
2. Commit and push the change to the configured branch.
3. Open your Render service dashboard.
4. Check the deployment history and logs.
5. Wait for the new deployment to finish.
6. Reopen `/health` and `/docs`.

Confirm that the service redeploys successfully.

Remember that redeployment does not guarantee that local SQLite data will survive.

## 9. Troubleshooting

### Docker build fails

Check that:

- The root directory points to the Student Management API project.
- `Dockerfile` exists in that directory.
- `requirements.txt` contains the required dependencies.
- The Docker build context includes the `app/` directory.

### The service fails to start

Check:

- Render deployment logs.
- The Dockerfile's `CMD`.
- Whether the application starts using `app.main:app`.
- Whether the application binds to `0.0.0.0`.
- Whether the application uses the supplied `PORT` value.

### Health check fails

Check that:

- `/health` exists in the application.
- The endpoint responds successfully locally.
- The application starts without an exception.
- The service is listening on the expected port.

### Authentication fails

Check:

- `SECRET_KEY` is configured.
- The application reads the environment variable correctly.
- Login credentials are correct.
- The token is supplied in the expected authorization format.
- The service logs do not contain configuration errors.

### Database errors occur

Check:

- `DATABASE_URL` is supported by the application.
- The database directory is writable.
- SQLAlchemy can create or connect to the configured database.
- The database configuration is consistent between local and cloud environments.

### The first request is slow

Render Free web services can spin down after inactivity. The first request after the service has spun down may take longer because the service needs to start again.

## 10. Final Verification Checklist

- [ ] Dockerfile supports the hosting platform's port.
- [ ] Local Docker Compose execution still works.
- [ ] Changes are committed and pushed to GitHub.
- [ ] GitHub Actions checks pass.
- [ ] Render builds the Docker image successfully.
- [ ] Environment variables are configured.
- [ ] `.env` and secrets are excluded from Git.
- [ ] The deployed `/health` endpoint works.
- [ ] Swagger UI loads at `/docs`.
- [ ] Registration and login work.
- [ ] JWT authentication works.
- [ ] Student CRUD endpoints work.
- [ ] Deployment logs have been reviewed.
- [ ] Database persistence limitations are understood.
- [ ] Deployment instructions are documented.

## 11. Cleanup

When you finish the exercise:

1. Stop or delete the Render service if you no longer need it.
2. Review the Render dashboard to confirm that you have not created any paid resources.
3. Remove any test data that you can still access.
4. Keep the project code and deployment instructions in GitHub.

Do not assume that a free service is permanent or that every associated resource is free. Review the plan and resource details before creating additional services.

## Deliverables

- Updated `Dockerfile` supporting the deployment port.
- Deployed Student Management API.
- Public API URL for testing.
- Verified health-check and documentation endpoints.
- Successful authentication and CRUD tests.
- Deployment instructions documented in the project README.

## Completion Criteria

Deploy the Dockerized Student Management API to Render, verify its health endpoint, API documentation, authentication, and CRUD functionality, and understand the limitations of temporary cloud storage.

## Part 5 — Final Completion

After completing Lesson 09, Part 5 — API Development is complete.

You should now be able to:

- Understand HTTP, REST APIs, and JSON.
- Consume external APIs using Requests.
- Build REST APIs with FastAPI.
- Integrate SQL databases using SQLAlchemy.
- Implement authentication and JWT-based authorization.
- Test APIs using pytest.
- Maintain code quality using Ruff.
- Automate checks using GitHub Actions.
- Prepare an API for production.
- Containerize applications using Docker and Docker Compose.
- Deploy and verify a Dockerized API on a cloud platform.

**Next roadmap stage:** Apply these backend skills to data processing, AI API integration, and AI-powered applications.