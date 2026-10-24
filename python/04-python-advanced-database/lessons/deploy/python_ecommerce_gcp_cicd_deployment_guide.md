# Python E-Commerce Project: Docker, CI/CD and GCP Deployment Guide

**Repository:** `bhupendra-mehra/advanced-python-database`  
**Application directory:** `ecommerce-db`  
**Deployment platform:** Google Cloud Compute Engine VM (`docker-learning`)  
**Container registry:** GitHub Container Registry (GHCR)  
**Application:** Flask e-commerce project served by Gunicorn  
**Status:** The application is running on the GCP VM, and the GitHub Actions build/push/deploy workflow has completed successfully.

This guide records the implementation in the order it was built, the issues encountered, how they were diagnosed, and the fixes applied. Keep this document updated if image names, commit SHAs, VM details, environment variables, or deployment commands change.

> **Security reminder:** Never commit `.env` files, passwords, tokens, SSH private keys, or other secrets to GitHub. Do not paste secret values into logs or chats.

---

## Part 1 — Prepare the project, CI/CD and GCP deployment

## 1. Understand the final architecture

```text
Developer changes code
        |
        v
Push to GitHub: main
        |
        +----------------------+
        |                      |
        v                      v
CI workflow               CD workflow
pytest + Ruff              Build Docker image
        |                      |
        v                      v
Checks pass                Push image to GHCR
                               |
                               v
                         SSH into GCP VM
                               |
                               v
                         Pull new image
                               |
                               v
                    Initialize/check database tables
                               |
                               v
                      Replace ecommerce-app
                               |
                               v
                     Verify /store/ endpoint
```

**Important current-state note:** CI and CD are separate GitHub Actions workflows triggered by pushes to `main`. They have both been working, but a separate workflow trigger does not by itself guarantee that CD waits for CI to pass. Making CD depend on successful CI is a recommended future hardening step.

### Main components

| Component | Purpose |
|---|---|
| GitHub repository | Stores application code and workflow definitions |
| GitHub Actions | Runs automated tests and deployment steps |
| `requirements-dev.txt` | Installs application dependencies plus pytest and Ruff |
| Docker image | Packages the application and its runtime |
| GHCR | Stores versioned Docker images |
| GCP VM `docker-learning` | Runs the application and MySQL containers |
| `ecommerce-app` | Flask application served by Gunicorn on port 5000 |
| `ecommerce-mysql` | MySQL 8.0 database container |
| `ecommerce-mysql-data` | Named volume for persistent MySQL data |
| `ecommerce-app.env` | Environment variables supplied to the application container |
| `ecommerce-network` | Docker network used by the app and database |

---

## 2. Repository structure and locations

GitHub repository:

`https://github.com/bhupendra-mehra/advanced-python-database`

Important paths:

```text
advanced-python-database/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
└── ecommerce-db/
    ├── app/
    ├── requirements.txt
    ├── requirements-dev.txt
    └── Dockerfile
```

Local WSL application directory:

```bash
/var/www/html/advanced-python-database/ecommerce-db
```

Local repository root:

```bash
/var/www/html/advanced-python-database
```

The Docker build context in the workflow is `./ecommerce-db`. This matters because the Dockerfile and application files are inside that folder, while GitHub Actions workflow files are at the repository root.

### Issue: Docker could not find the Dockerfile

An earlier build failed with an error similar to:

```text
failed to read dockerfile: open Dockerfile: no such file or directory
```

**Cause:** The build was running from a directory that did not contain the Dockerfile, or the build context/path was incorrect.

**Fix:** Keep the Dockerfile inside `ecommerce-db` and use the correct build context:

```yaml
with:
  context: ./ecommerce-db
```

Also check that the Dockerfile does not contain an accidental duplicate `FROM` line.

---

## 3. Configure development dependencies and checks

The development dependency file is `ecommerce-db/requirements-dev.txt`:

```text
-r requirements.txt
pytest
ruff
```

From the application directory, run:

```bash
cd /var/www/html/advanced-python-database/ecommerce-db
pytest
ruff check .
```

The project has eight unit tests that use mocks, so they can run without connecting to a real MySQL instance.

### Issue: CI must not depend on a live database

**Fix:** Keep unit tests isolated from the live database and use mocks. This makes checks repeatable and avoids requiring production credentials during CI.

**Observed result:** All eight tests passed, and `ruff check .` passed.

---

## 4. Configure Continuous Integration (CI)

The CI workflow is stored at:

`.github/workflows/ci.yml`

Its intended triggers are pushes to `main` and pull requests targeting `main`:

```yaml
on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main
```

The workflow checks out the repository, installs dependencies, runs pytest, runs Ruff, and reports the result in GitHub Actions.

### Issues and fixes

- **Issue:** Tests could otherwise require the production database.  
  **Fix:** The unit tests use mocks.
- **Issue:** GitHub Actions showed Node 20/runner deprecation notices.  
  **Result:** These were notices, not blockers for the successful run.

### Verify CI

1. Open the repository on GitHub.
2. Select **Actions**.
3. Open the latest CI run.
4. Confirm that the test and lint steps are green.

---

## 5. Build and publish the Docker image to GHCR

The CD workflow is stored at `.github/workflows/cd.yml`.

Image naming pattern:

```text
ghcr.io/bhupendra-mehra/advanced-python-database:<commit-sha>
```

The workflow builds from `./ecommerce-db` and pushes an image tagged with the commit SHA. The relevant build configuration is:

```yaml
- name: Build and push Docker image
  uses: docker/build-push-action@v6
  with:
    context: ./ecommerce-db
    push: true
    tags: |
      ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
```

The workflow logs into GHCR using `GITHUB_TOKEN` and has `packages: write` permission.

### Why use a commit SHA tag?

A commit SHA identifies the exact code version packaged into the image. It is more traceable than relying only on a mutable tag such as `latest`.

### Issues encountered and fixes

**Docker pulls failed with `EOF`:** Some earlier pulls failed while resolving registry metadata. A request to Docker Hub's registry endpoint returned HTTP 401 with a Bearer authentication challenge, a normal response from that unauthenticated endpoint at that moment. Later, the image build and publication workflow succeeded.

**GHCR push access denied:** An earlier push failed with a message similar to:

```text
push access denied, repository does not exist or may require authorization
```

**Fix:** Use the correct GHCR image path, authenticate before pushing, and grant the workflow `packages: write` permission.

### Verify image publication

1. Open **GitHub → Actions** and inspect the latest CD run.
2. Confirm the build-and-push step is green.
3. Open the repository's Packages section or GHCR package page to confirm the package exists.

---

## 6. Prepare the GCP VM

The VM used for this project:

| Setting | Value |
|---|---|
| VM name | `docker-learning` |
| Zone | `us-east1-b` |
| Machine type | `e2-micro` |
| Operating system | Ubuntu 24.04.4 LTS |
| Application port | `5000` |
| Application container | `ecommerce-app` |
| Database container | `ecommerce-mysql` |

The VM has limited RAM (about 1 GiB), so avoid running unnecessary services or duplicate app containers. Swap was configured during troubleshooting because of the limited memory.

### Cost considerations

The VM was selected with free-tier/low-cost usage in mind, but actual costs depend on current Google Cloud free-tier eligibility, region, disk, IP address, and usage. Check Billing rather than assuming every resource is free. The current setup does not require Cloud SQL, GKE, a load balancer, or NAT.

### Important operational rule

**Do not delete the MySQL container's named volume.** The volume `ecommerce-mysql-data` stores database data independently of the app container. Normal app deployments should replace only `ecommerce-app`.

---

## 7. Run MySQL and the application on a Docker network

Docker network:

```text
ecommerce-network
```

Database container:

```text
ecommerce-mysql
```

It uses MySQL 8.0. Its ports appear as `3306/tcp` and `33060/tcp` inside Docker, but they are not published to the VM host. The app connects to MySQL using the Docker network and hostname `ecommerce-mysql`.

Persistent named volume:

```text
ecommerce-mysql-data
```

Mounted inside MySQL at:

```text
/var/lib/mysql
```

### Application environment file

The VM environment file is:

```text
/home/bhupendrabce/ecommerce-app.env
```

It contains the application's database settings and secrets. Known database settings include:

```dotenv
DB_HOST=ecommerce-mysql
DB_PORT=3306
DB_NAME=ecommerce
DB_USER=ecommerce_user
```

The file also contains private values such as the database password and Flask `SECRET_KEY`. Do not copy secret values into this document or Git.

### Why use the Docker network?

Containers on the same Docker network can reach each other by container name. This lets the app connect to `ecommerce-mysql` without publishing MySQL's port to the public internet.

---

## 8. Fix the missing database schema

### Issue

The storefront initially returned HTTP 500. Investigation showed that the `ecommerce.categories` table did not exist. The database container was running, but the expected application schema had not been created.

### Investigation and fix

1. Reviewed the application's table initialization code.
2. Found that the `app.tables` module executed without creating the expected tables.
3. Corrected `tables.py` locally.
4. Built and deployed a new Docker image.
5. Ran the schema initializer against MySQL through the Docker network.

The deployment command is:

```bash
sudo docker run --rm \
  --network ecommerce-network \
  --env-file /home/bhupendrabce/ecommerce-app.env \
  --entrypoint python \
  "$IMAGE" -m app.tables
```

This starts a temporary container from the new image, runs the table initializer, and removes the temporary container when the command completes.

### Tables verified in MySQL

```text
categories
customers
order_items
orders
products
```

### Verification

The VM-local storefront test returned HTTP 200:

```bash
curl -I --max-time 15 http://localhost:5000/store/
```

**Important:** The initializer is intended to be safe to execute repeatedly in this project. Review schema code before assuming future migrations or schema operations are repeatable.

---

## 9. Configure SSH access for GitHub Actions

The deployment workflow connects to the VM over SSH using `appleboy/ssh-action`.

Repository secrets:

| GitHub Actions secret | Purpose |
|---|---|
| `GCP_VM_HOST` | VM external IP address |
| `GCP_VM_USER` | Linux SSH username |
| `GCP_VM_SSH_KEY` | SSH private key |
| `GHCR_USERNAME` | GitHub username used for GHCR login |
| `GHCR_TOKEN` | Token with permission to pull the private GHCR image |

The Linux username used in the current setup is:

```text
bhupendrabce
```

### Issue: SSH private key was not recognized

The workflow initially failed with errors similar to:

```text
ssh.ParsePrivateKey: ssh: no key found
ssh: handshake failed: unable to authenticate
```

### Fix

A dedicated Ed25519 key was generated in WSL:

```bash
ssh-keygen -t ed25519 -C "github-actions-deploy" \
  -f ~/.ssh/gcp_cd_deploy -N ""
```

- The **public key** (`gcp_cd_deploy.pub`) was added to the VM user's `~/.ssh/authorized_keys`.
- The **private key** (`gcp_cd_deploy`) was stored as the GitHub Actions secret `GCP_VM_SSH_KEY`.
- Paste the private key in full, including its header and footer, without quotation marks or Markdown fences.
- The VM's `.ssh` directory and `authorized_keys` permissions/ownership must allow SSH to use the key.

**Security:** Never commit or share the private key. If it is exposed, replace it.

---

## 10. Fix non-interactive sudo in GitHub Actions

### Issue

After SSH authentication was fixed, the deployment failed with:

```text
sudo: a terminal is required to read the password
sudo: a password is required
```

GitHub Actions runs the remote script without an interactive terminal, so `sudo` could not ask for a password.

### Fix

A dedicated sudoers file was configured on the VM:

```bash
sudo visudo -f /etc/sudoers.d/github-actions-docker
```

The rule added was:

```text
bhupendrabce ALL=(root) NOPASSWD: /usr/bin/docker
```

Use the actual Docker binary path reported by `which docker` if it differs from `/usr/bin/docker`.

Test it with:

```bash
sudo -k
sudo -n docker ps
```

The second command must run without prompting for a password.

### Security note

Permission to run Docker commands as root is effectively root-level access because Docker can mount host filesystems and perform other privileged operations. Protect the deployment account and its SSH key. Do not add broader passwordless sudo permissions than needed.

---

# Part 2 — Automated deployment, troubleshooting and validation

## 11. Deploy the image from GitHub Actions to the VM

The CD workflow includes a remote deployment step after the image is pushed to GHCR. The remote script performs these operations:

1. Log in to GHCR.
2. Pull the image tagged with the current commit SHA.
3. Run the schema initializer.
4. Stop and remove only the existing application container.
5. Start the new application container.
6. Wait for the storefront to respond.
7. Print application logs and fail the workflow if the health check does not succeed.

Key commands:

```bash
sudo docker pull "$IMAGE"

sudo docker run --rm \
  --network ecommerce-network \
  --env-file /home/bhupendrabce/ecommerce-app.env \
  --entrypoint python \
  "$IMAGE" -m app.tables

sudo docker stop ecommerce-app || true
sudo docker rm ecommerce-app || true

sudo docker run -d \
  --name ecommerce-app \
  --network ecommerce-network \
  --restart unless-stopped \
  --env-file /home/bhupendrabce/ecommerce-app.env \
  -p 5000:5000 \
  "$IMAGE"
```

The storefront check is:

```bash
for i in $(seq 1 12); do
  if curl -fsS http://localhost:5000/store/ >/dev/null; then
    echo "Deployment successful"
    exit 0
  fi
  sleep 5
done

sudo docker logs --tail 80 ecommerce-app
exit 1
```

### Current deployment behavior and limitation

The script initializes tables before replacing the current app container, helping avoid replacement before schema initialization succeeds. However, it does **not** automatically restore the previous app container if the new container starts but fails its health check. Automatic rollback is a recommended future improvement.

---

## 12. Verify the deployment on the VM

After a successful deployment, this command showed the app and MySQL containers running:

```bash
sudo docker ps
```

The app container showed a port mapping similar to:

```text
0.0.0.0:5000->5000/tcp
[::]:5000->5000/tcp
```

The database container showed `3306/tcp` and `33060/tcp` without a host port mapping.

The listening socket was also checked:

```bash
sudo ss -lntp | grep ':5000'
```

It showed Docker listening on:

```text
0.0.0.0:5000
[::]:5000
```

This confirmed that the app was listening on all IPv4 and IPv6 interfaces on the VM, rather than only on `127.0.0.1`.

### Application test from the VM

```bash
curl -I --max-time 15 http://localhost:5000/store/
```

Expected response:

```text
HTTP/1.1 200 OK
```

The VM-local request succeeded.

---

## 13. Troubleshoot browser access to the VM

The application worked inside the VM, but the browser initially could not open:

```text
http://35.207.44.111:5000/store/
```

The browser showed:

```text
ERR_CONNECTION_TIMED_OUT
```

### What the timeout meant

A browser timeout means the client did not receive a TCP response from the target port in time. It does not by itself prove the application is broken. Since local `curl` worked and Docker published port 5000, troubleshooting moved to external network access.

### Step 1: Check the Docker port mapping

```bash
sudo docker ps
```

Observed app mapping:

```text
0.0.0.0:5000->5000/tcp
[::]:5000->5000/tcp
```

This was correct.

### Step 2: Check the listening socket

```bash
sudo ss -lntp | grep ':5000'
```

Observed listeners on `0.0.0.0:5000` and `[::]:5000`. This was correct.

### Step 3: Inspect the Google Cloud VPC firewall rule

The `port-5000` firewall rule was found in the Google Cloud Console. Its source IP range initially showed:

```text
35.207.44.111/32
```

That is the VM's external IP, not necessarily the public IP of the computer making the browser request.

### Step 4: Find the client computer's public IP

On the Windows computer, PowerShell was used:

```powershell
(Invoke-RestMethod https://api.ipify.org).Trim()
```

The returned address is the computer's public IPv4 address as seen by the external service. It can differ from the private Wi-Fi address shown by Windows and can change if the network or VPN changes.

### Step 5: Update the firewall source range

The source range for the `port-5000` ingress rule was changed to the client computer's current public IP followed by `/32`.

Format:

```text
YOUR_PUBLIC_IP/32
```

Use the actual public IP returned by PowerShell. Restricting the source to your own IP is safer than allowing `0.0.0.0/0`.

### Step 6: Test the TCP connection from Windows

In PowerShell:

```powershell
Test-NetConnection 35.207.44.111 -Port 5000
```

An earlier test showed:

```text
PingSucceeded    : True
TcpTestSucceeded : False
```

This indicated that the VM's IP responded to ping, but a TCP connection to port 5000 could not be established at that time.

### If browser access still fails

Verify all of the following, in order:

1. The public IP in the firewall rule still matches the computer's current public IP.
2. The rule is enabled, uses the VM's VPC network (`default` in the rule screenshot), has direction **Ingress**, action **Allow**, and permits `tcp:5000`.
3. The rule's target applies to the `docker-learning` VM.
4. The VM's external IP is still `35.207.44.111`; external IPs can change if they are ephemeral and the VM is stopped or recreated.
5. The VM's operating-system firewall is not blocking the port.

On the VM, inspect the OS firewall without changing it first:

```bash
sudo ufw status
sudo iptables -L INPUT -n -v
```

If the connection still fails, share the rule configuration (not secrets) and the output of the TCP test. Avoid making multiple firewall changes at once, so each test provides useful information.

**Security reminder:** Port 5000 is suitable for a controlled test, but it is not a production HTTPS setup. Do not expose admin pages, credentials, or customer information publicly without suitable TLS and application security.

---

## 14. Configure admin credentials for the deployed app

The application displayed:

```text
Admin credentials are not configured
```

This indicates that the application did not find the admin configuration it expects. Adding values to a local `.env` file does not automatically put them on the GCP VM or inside an already-running container.

### VM environment file

The deployed app is configured with:

```text
/home/bhupendrabce/ecommerce-app.env
```

The container receives variables from this file through Docker's `--env-file` option.

### Find the exact variable names

Before adding anything, inspect the application's authentication/configuration code in the local project directory:

```bash
cd /var/www/html/advanced-python-database/ecommerce-db

grep -RniE \
  "Admin credentials are not configured|ADMIN_.*(USER|PASSWORD)|ADMIN_USERNAME|ADMIN_PASSWORD" \
  app
```

Use the exact environment variable names expected by the application. Do not assume the names are `ADMIN_USERNAME` and `ADMIN_PASSWORD` unless the code confirms that.

### Add the values on the VM

Edit the VM environment file:

```bash
sudo nano /home/bhupendrabce/ecommerce-app.env
```

Add the correct variable names and values according to the application's code. Do not put the real values in Git, this document, screenshots, or chat.

### Recreate the app container to load changed variables

A simple `docker restart ecommerce-app` restarts the existing container and **does not reload** updated environment variables from the file. The container must be recreated with `--env-file` so Docker reads the changed values.

Use the same image tag and container settings as the currently approved deployment. General command pattern:

```bash
sudo docker stop ecommerce-app
sudo docker rm ecommerce-app

sudo docker run -d \
  --name ecommerce-app \
  --network ecommerce-network \
  --restart unless-stopped \
  --env-file /home/bhupendrabce/ecommerce-app.env \
  -p 5000:5000 \
  YOUR_APPROVED_IMAGE
```

Replace `YOUR_APPROVED_IMAGE` with the actual GHCR image reference. Do not copy that placeholder literally.

Then verify:

```bash
sudo docker ps
curl -I --max-time 15 http://localhost:5000/store/
sudo docker logs --tail 80 ecommerce-app
```

**Do not stop, remove, or recreate `ecommerce-mysql`. Do not delete `ecommerce-mysql-data`.** This step only recreates the application container.

---

## 15. Quick operational checklist

### Before pushing

- [ ] Run `pytest`.
- [ ] Run `ruff check .`.
- [ ] Confirm `.env` files and secrets are not staged for Git.
- [ ] Confirm the Docker build context is `./ecommerce-db`.
- [ ] Commit and push the intended changes to `main`.

### After pushing

- [ ] Confirm the CI workflow is green.
- [ ] Confirm the CD build-and-push step is green.
- [ ] Confirm the deploy step is green.
- [ ] Check `sudo docker ps` on the VM.
- [ ] Check `curl -I --max-time 15 http://localhost:5000/store/`.
- [ ] If testing from a browser, verify the current external IP and the VPC firewall rule.
- [ ] Check application logs if the health check fails.

### Protect persistent data

- [ ] Replace only `ecommerce-app` during normal app deployment.
- [ ] Keep `ecommerce-mysql` running unless a database maintenance operation is deliberately planned.
- [ ] Never delete `ecommerce-mysql-data` as part of an application deployment.
- [ ] Keep database credentials and Flask `SECRET_KEY` private.

---

## 16. Issues encountered — summary table

| Issue | Diagnosis | Fix or outcome |
|---|---|---|
| Docker build could not find `Dockerfile` | Wrong build directory/context or Dockerfile path | Used `./ecommerce-db` as build context and checked Dockerfile location |
| Docker pulls sometimes failed with `EOF` | Registry connection/metadata retrieval failure | Checked registry access; later CI/CD image publication succeeded |
| GHCR push access denied | Image path/authentication/permissions needed correction | Used the GHCR image path, login, and `packages: write` permission |
| Missing `ecommerce.categories` table | Database schema had not been initialized correctly | Fixed `app.tables`, deployed a new image, and initialized schema |
| SSH private key parse/authentication failed | GitHub Actions could not parse/use the configured key | Generated a dedicated Ed25519 key, installed public key on VM, stored private key as GitHub secret |
| `sudo` asked for a password in CI | Remote SSH script was non-interactive | Added a scoped Docker command sudoers rule and tested with `sudo -n docker ps` |
| Browser showed `ERR_CONNECTION_TIMED_OUT` | Local app worked, but remote TCP connection to port 5000 failed | Verified Docker mapping/listener and inspected VPC firewall; corrected source IP range, with TCP/browser access requiring final confirmation if still failing |
| `gcloud firewall-rules list` failed with insufficient authentication scopes | VM's gcloud credentials lacked required API scopes | Used Google Cloud Console to inspect firewall rules instead |
| Admin page said credentials were not configured | Required admin variables were not available to the running app | Locate exact variable names in code, add them to VM env file, and recreate only the app container to load them |

---

## 17. Recommended next improvements

The core deployment is working. These are improvements, not blockers:

1. **Make CD wait for successful CI.** Arrange the workflow so an image cannot be deployed when the relevant CI checks fail. Currently CI and CD are separate workflows triggered on `main`, so ordering is not guaranteed.
2. **Add deployment rollback.** Keep track of the previous working image and restore it if the new app fails its health check. The current script does not automatically roll back.
3. **Improve external access security.** For anything beyond controlled testing, use HTTPS and a suitable reverse proxy/domain setup rather than exposing the app's port directly.
4. **Keep resource use small.** The VM is an e2-micro with limited memory; avoid unnecessary services and duplicate app containers.
5. **Review cost and billing periodically.** A free-tier intention does not guarantee every resource or usage pattern costs zero.

---

## 18. Final state

At the end of this work:

- The project is stored in GitHub.
- CI runs automated unit tests and Ruff checks.
- CD builds and publishes a Docker image to GHCR.
- GitHub Actions can connect to the GCP VM over SSH.
- The deployment process pulls the image, initializes database tables, replaces the app container, and checks the storefront.
- The VM runs `ecommerce-app` and `ecommerce-mysql` on `ecommerce-network`.
- MySQL data is stored in the `ecommerce-mysql-data` named volume.
- The storefront responds locally on the VM at `http://localhost:5000/store/`.
- Browser access depends on the VM external IP, applicable VPC firewall configuration, and OS/network access.
- Admin credentials must be provided using the exact environment variable names expected by the application.

This document describes the setup and troubleshooting history as recorded. Re-check current image tags, firewall state, external IP, and environment variable names before reusing commands after future changes.
