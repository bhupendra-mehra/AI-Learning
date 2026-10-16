
# Lesson 08 — Dockerize the Student Management API

## Objective

Containerize the FastAPI Student Management API using Docker and Docker Compose, configure environment variables, and persist the SQLite database.

## Prerequisites

- Docker Engine and Docker Compose plugin
- Python project dependencies
- Student Management API working locally
- Passing project tests

## 1. Docker Files

The project includes:

- `Dockerfile` — builds the API image.
- `.dockerignore` — excludes unnecessary and sensitive files.
- `docker-compose.yml` — configures the API service and database volume.
- `.env` — local configuration; never commit it.
- `.env.example` — safe configuration template.

## 2. Build the Image

Run from `projects/student-management-api/`:

```bash
docker compose config
docker compose build
```

## 3. Start the API

```bash
docker compose up -d
docker compose ps
docker compose logs api
```

Open `http://localhost:8000/docs`.

## 4. Verify the API

```bash
curl -i http://localhost:8000/
curl -i http://localhost:8000/health
```

Use Swagger to test registration, login, student CRUD, PUT, and PATCH.

## 5. Database Persistence

The Compose configuration stores the SQLite database in a named volume mounted at `/app/data`.

To verify persistence:

1. Register a user and create a student.
2. Record the student ID.
3. Restart the container with `docker compose restart api`.
4. Retrieve the same student.
5. Confirm the record still exists.

`docker compose down` normally preserves named volumes. `docker compose down -v` deletes them and can permanently remove the database data.

## 6. Troubleshooting

Check the service and logs:

```bash
docker compose ps
docker compose logs --tail=100 api
docker compose config
```

Common problems:

- Missing `SECRET_KEY`
- Incorrect `DATABASE_URL`
- Missing dependencies
- Incorrect application import path
- Port 8000 already in use
- Database volume permissions
- Health check endpoint unavailable

Fix the underlying issue rather than suppressing the error.

## 7. Security Notes

- Never copy `.env` into the image.
- Never commit production secrets.
- Run the application as a non-root user.
- Keep persistent database files out of Git.
- Use persistent storage and backups for important data.
- Review image and dependency updates.
- Use HTTPS and appropriate network controls when deployed.

## 8. Practical Exercises

- [ ] Build the image successfully.
- [ ] Start the API using Docker Compose.
- [ ] Open Swagger UI.
- [ ] Verify the health endpoint.
- [ ] Register, log in, and create a student.
- [ ] Restart the container and verify data persistence.
- [ ] Inspect logs and container status.
- [ ] Confirm `.env` and database files are excluded from the build context.
- [ ] Stop the service without deleting the database volume.
- [ ] Run Ruff and pytest locally against the standalone project.

## 9. Cleanup

Stop the containers while preserving the named volume:

```bash
docker compose down
```

Do not use `docker compose down -v` unless you intentionally want to delete the stored database volume.

## 10. Completion Criteria

The lesson is complete when:

- The image builds successfully.
- The API starts and responds to requests.
- Authentication and student endpoints work.
- Data survives a container restart.
- The application logs and health status can be inspected.
- Secrets and database files are not committed to Git.