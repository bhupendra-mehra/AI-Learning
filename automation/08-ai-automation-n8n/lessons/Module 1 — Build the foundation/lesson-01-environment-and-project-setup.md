# Part 8 · Lesson 01 — Enterprise AI Commerce Operations Platform

Lesson 01 of 30

Module 1: Foundations

Objective: Establish the requirements for a client-ready e-commerce automation platform, set up an isolated n8n environment, and build the first working workflow.

We will treat this as a real software delivery project. Each lesson will extend the same product, and we will maintain its requirements, workflow designs, test cases, and documentation as it evolves.

## Step 1 — Define the product requirements

Our fictional client is a growing e-commerce business that receives customer requests about orders, payments, deliveries, returns, and invoices.

The client wants to reduce repetitive manual work while ensuring that AI cannot independently perform sensitive actions such as issuing refunds.

## Product requirements — v1.0

Business objective

Reduce manual handling of customer requests and improve response consistency, routing accuracy, and operational visibility.

Users

Customer support agents, e-commerce operations staff, team supervisors, and system administrators.

Initial inputs

Customer requests received through a webhook, form, or later an email integration.

Initial automated processing

Validate required fields, normalize request data, assign a request identifier, and route valid requests for further processing.

Safety requirements

Reject invalid inputs, avoid duplicate processing where possible, protect credentials, log execution outcomes, and require approval before consequential business actions.

### Our first release scope

We will not build every integration at once. The initial version will accept a sample order-related request and return a validated result. Later, we will add commerce APIs, database storage, LLM processing, support integrations, and approval workflows.

This is the same incremental delivery approach used on larger software projects: establish a working foundation, then add capabilities without breaking earlier functionality.

## Step 2 — Create the project workspace

Keep the project separate from Magento and your existing AI Learning repository's application code.

Create this folder structure in a new directory:

```
enterprise-ai-commerce-ops/
├── README.md
├── docs/
│   ├── 01-business-requirements.md
│   ├── 02-workflow-design.md
│   └── 03-test-cases.md
├── workflows/
├── test-data/
│   └── sample-order-request.json
└── screenshots/
```

Each folder has a purpose:

| Folder         | Purpose                                            |
| -------------- | -------------------------------------------------- |
| `docs/`        | Requirements, workflow diagrams, and test evidence |
| `workflows/`   | Exported n8n workflows in JSON format              |
| `test-data/`   | Fictional orders and customer requests for testing |
| `screenshots/` | Evidence that the workflows run correctly          |

You can create this structure using your terminal:

```
mkdir -p enterprise-ai-commerce-ops/{docs,workflows,test-data,screenshots}
cd enterprise-ai-commerce-ops
```

Create `README.md` and `docs/01-business-requirements.md` using your preferred editor.

### Initial business requirements

Add the following content to `docs/01-business-requirements.md`:

# Enterprise AI Commerce Operations Platform

## 1. Business Problem

E-commerce operations teams spend significant time processing customer requests related to orders, payments, deliveries, returns, and invoices. Manual processing can cause delays, inconsistent routing, and avoidable errors.

## 2. Product Objective

Build a workflow automation platform using n8n, APIs, and AI to validate customer requests, retrieve relevant business information, classify cases, route work, and support controlled business actions.

## 3. Initial Scope

- Receive an order-related customer request.
- Validate required input fields.
- Normalize request data.
- Prepare a consistent request record.
- Route valid requests for further processing.
- Identify invalid requests for exception handling.

## 4. Future Scope

- Commerce platform and REST API integration.
- Database persistence and duplicate detection.
- LLM-based classification and document extraction.
- Customer support and notification integrations.
- Human approval for sensitive actions.
- Monitoring, audit logging, and deployment.

## 5. Non-Functional Requirements

- Protect credentials and customer information.
- Handle invalid input without silently losing requests.
- Make workflow executions observable and testable.
- Avoid unintended duplicate business actions.
- Document setup, operation, recovery, and maintenance.

## 6. Initial Acceptance Criteria

- A sample customer request can be processed successfully.
- Required fields are validated.
- Valid requests produce predictable output.
- Invalid requests can be identified.
- Workflow execution results can be inspected.

This document is our initial baseline. We will update it as the client requirements evolve instead of creating a new project specification for each lesson.

## Step 3 — Start the isolated n8n environment

First, check whether you already have the `n8n-learning` container from the previous setup.

```
docker ps -a --filter "name=n8n-learning"
```

If it exists, start it if necessary:

```
docker start n8n-learning
docker logs --tail 50 n8n-learning
```

If it does not exist, create the dedicated volume and start the container using the earlier Lesson 01 Docker command. Keep the port bound to `127.0.0.1:5678` so the editor is accessible locally only.

## Step 3 — Create the n8n learning environment from scratch

Since `n8n-learning` does not exist, we'll create a fresh, isolated n8n container using Docker. This setup will be separate from your Magento environment and dedicated to the Enterprise AI Commerce Operations Platform.

### 3.1 Check that Docker is running

Open your terminal and execute:

```
docker --version
docker compose version
docker info
```

If these commands work, continue. If `docker info` cannot connect to the Docker daemon, start Docker Desktop first.

### 3.2 Create a dedicated Docker volume

Run:

```
docker volume create n8n_data
```

This volume stores n8n's configuration and workflow data separately from the container. If the volume already exists, Docker will reuse it.

Verify it:

```
docker volume ls
```

Look for `n8n_data`.

### 3.3 Download and start n8n

Run this command in your terminal:

```
docker run -d \
  --name n8n-learning \
  -p 127.0.0.1:5678:5678 \
  -e TZ=Asia/Kolkata \
  -e GENERIC_TIMEZONE=Asia/Kolkata \
  -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

What this does:

| Setting                    | Purpose                                      |
| -------------------------- | -------------------------------------------- |
| `--name n8n-learning`      | Gives the container a recognizable name      |
| `-p 127.0.0.1:5678:5678`   | Makes n8n accessible locally on port 5678    |
| `TZ=Asia/Kolkata`          | Sets the container timezone to India         |
| `n8n_data:/home/node/.n8n` | Preserves n8n data across container restarts |
| `docker.n8n.io/n8nio/n8n`  | Uses the official n8n Docker image           |

The first run may take a few minutes because Docker needs to download the image.

### 3.4 Verify that the container is running

Run:

```
docker ps
```

You should see a container named `n8n-learning` with port `127.0.0.1:5678->5678/tcp`.

If it doesn't appear, check:

```
docker ps -a
docker logs --tail 100 n8n-learning
```

### 3.5 Open n8n

Open this URL in your browser:

[http://localhost:5678](http://localhost:5678?utm_source=chatgpt.com)

Create your local owner account when prompted.

### 3.6 Verify persistence

After n8n opens successfully, test that the container can restart without losing its configuration:

```
docker restart n8n-learning
```

Wait a few seconds, then reopen `http://localhost:5678`.

### Troubleshooting

| Problem                       | Solution                                                                                                                |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Port 5678 already in use      | Check `docker ps` before stopping anything; don't interrupt unrelated containers.                                       |
| Container exits immediately   | Inspect `docker logs n8n-learning`.                                                                                     |
| Docker daemon unavailable     | Start Docker Desktop and retry.                                                                                         |
| Page won't open               | Verify the container is running and check the browser URL.                                                              |
| Container name already exists | Run `docker ps -a --filter "name=n8n-learning"` and inspect the existing container before deciding whether to reuse it. |

Important: Don't delete the `n8n_data` volume when troubleshooting. It contains your saved workflows and configuration. Keep this environment separate from Magento.

### Step 3 completion checklist

Docker and Docker Compose are working.

The n8n_data volume exists.

The n8n-learning container is running.

The n8n editor opens at localhost:5678.

Environment ready

Open [http://localhost:5678](http://localhost:5678?utm_source=chatgpt.com) and sign in to your local n8n instance.

The separate Docker volume preserves your n8n data when the container is stopped and started again. For a production deployment, we will later review a more complete Docker Compose setup, security, backups, and database options.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



Environment checkpoint: Do not continue to the workflow configuration until the n8n editor loads successfully.

## Step 4 — Create the first business workflow

Our first workflow will accept a fictional customer request for an order investigation.

01 · Manual Trigger

Starts a test execution

02 · Edit Fields (Set)

Creates the initial request record

Expected output

One item containing the customer request

### Configure the workflow

1. In n8n, create a new workflow.
2. Name it `CAO-001 - Customer Request Intake`.
3. Add a Manual Trigger node.
4. Add an Edit Fields (Set) node and connect it to the trigger.
5. In the Edit Fields node, choose Manual Mapping and add the fields below.

Use fictional data only.

| Field             | Type   | Sample value                            |
| ----------------- | ------ | --------------------------------------- |
| `request_id`      | String | `REQ-2026-0001`                         |
| `request_type`    | String | `order_status`                          |
| `customer_email`  | String | `customer@example.com`                  |
| `order_reference` | String | `ORD-100045`                            |
| `channel`         | String | `web_form`                              |
| `message`         | String | `Please provide an update on my order.` |

Keep the fields in Fixed mode for now. We will introduce expressions and dynamic input in Lesson 03.

The workflow should look like this:

Manual Trigger

Edit Fields

Workflow ID: CAO-001 · Initial product capability: request intake

### Execute and verify

Click Execute Workflow and inspect the output of the Edit Fields node. n8n lets you manually execute a workflow while you are building and testing it. Keep it unpublished for now.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



Your expected output should contain one item with all six fields and the exact values above.

Save the workflow when you have confirmed the result.

## Step 5 — Create reusable test data

Create `test-data/sample-order-request.json` in your project folder:

```

{
  "request_id": "REQ-2026-0001",
  "request_type": "order_status",
  "customer_email": "customer@example.com",
  "order_reference": "ORD-100045",
  "channel": "web_form",
  "message": "Please provide an update on my order."
}

```

This JSON file becomes our baseline test fixture. As we add webhook intake and API integrations, we can use it to verify that the same business request continues to work.

Notice that the Edit Fields node currently contains a manually configured copy of the data. We have not connected the JSON file directly to n8n; that is intentional. Later, we will accept dynamic inputs through a webhook.

## Step 6 — Document the first workflow

Add the following to `docs/02-workflow-design.md`:

# CAO-001 — Customer Request Intake

## Purpose

Establish the initial workflow for the Enterprise AI Commerce Operations Platform.

## Trigger

Manual Trigger for development and testing.

## Nodes

1. Manual Trigger — starts a test execution.
2. Edit Fields — creates the initial customer request record.

## Input

A fictional order-status request with request ID, request type, customer email, order reference, channel, and message.

## Expected Output

One item containing all six configured fields with the expected values.

## Current Limitations

- Input is manually configured.
- No external commerce API is connected.
- No database persistence is implemented.
- Validation, deduplication, AI classification, and routing are planned for subsequent lessons.

## Operational Notes

Keep the workflow unpublished during initial development. Use fictional data and inspect execution output after each test run.

## Step 7 — Test the initial workflow

Create `docs/03-test-cases.md` and record these test cases.

| Test ID | Scenario                  | Expected result               |
| ------- | ------------------------- | ----------------------------- |
| TC-001  | Execute the workflow      | Successful execution          |
| TC-002  | Inspect the output        | Exactly one item              |
| TC-003  | Verify field names        | All six expected fields exist |
| TC-004  | Verify request reference  | `ORD-100045`                  |
| TC-005  | Restart the n8n container | Workflow remains saved        |

For each test, record whether it passed and any error encountered. TC-005 can be performed after the initial execution is saved.

## Lesson 01 completion tracker

## Acceptance checklist

0/6

Created the enterprise project folder structure and requirements document.

Started the isolated n8n environment without changing Magento.

Created CAO-001 with Manual Trigger and Edit Fields.

Executed the workflow and verified all six fields.

Saved the workflow and created the sample JSON fixture.

Documented the workflow and recorded test results.

Complete the relevant steps in your local environment before marking them verified.

Review progress and continue

## What we will build in Lesson 02

We will extend CAO-001 rather than create a separate exercise. You will learn how n8n passes data between nodes, how to inspect execution results, and how to preserve or transform request fields as the workflow grows.

The next product capability will be to establish a consistent request-processing structure that later lessons can extend with validation, deduplication, business rules, and AI classification.