# Lesson 20 — Multi-step Orchestration and Recovery from Partial Failures

Roadmap: Version 2.3 → Part 8: AI Automation with n8n\
Project: Enterprise AI Commerce Operations Platform\
Workflow: `CAO-009 - Order Operations Orchestrator`

Documentation filename: `lesson-20-multi-step-orchestration-and-recovery-from-partial-failures.md`

Documentation location:

`/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-20-multi-step-orchestration-and-recovery-from-partial-failures.md`

## 1. What we will build

Until now, most of our workflows have performed individual tasks such as classification, validation, investigation and approval.

In a real e-commerce application, one customer request may require several operations.

For example, when investigating an order:

1. Retrieve order information.
2. Retrieve customer information.
3. Retrieve product information.
4. Verify the order details.
5. Generate an investigation summary.
6. Record the final result.
7. Handle failures if any operation fails.

We will create an orchestrator that coordinates these steps.

We will also introduce the concept of multi-agent systems without creating additional roadmap lessons.

## 2. Understand orchestration and multi-agent systems

Workflow orchestration: One main workflow coordinates multiple operations and controls their execution order.

Multi-agent systems: Different specialized AI agents or workers handle different responsibilities and collaborate through a coordinated process.

For our project, the responsibilities will be:

| Worker                | Responsibility                              |
| --------------------- | ------------------------------------------- |
| Order Investigation   | Retrieve and analyze order details          |
| Customer Context      | Retrieve relevant customer information      |
| Product Investigation | Retrieve product details                    |
| Decision Coordinator  | Combine results and determine the next step |
| Recovery Handler      | Handle failed operations and retries        |

These can be implemented as separate n8n workflows, AI agents, or ordinary workflow components. We will start with reliable workflow orchestration and then add AI-based coordination.

## 3. Architecture

Customer Request

CAO-009 — Main Orchestrator

Order Worker

Order information

Customer Worker

Customer information

Product Worker

Product information

Decision Coordinator

Combine results

Recovery and Error Handling

Final Investigation Result

## 4. Create the main orchestrator

Create a new workflow:

`CAO-009 - Order Operations Orchestrator`

### Step 1 — Add input data

Add Manual Trigger followed by Edit Fields.

Rename the Edit Fields node:

`Input - Order Investigation Request`

Add:

| Field               | Value                 |
| ------------------- | --------------------- |
| `request_id`        | `REQ-ORCH-001`        |
| `order_reference`   | `ORD-100045`          |
| `cart_id`           | `1`                   |
| `customer_id`       | `1`                   |
| `product_id`        | `1`                   |
| `request_type`      | `order_investigation` |
| `processing_status` | `started`             |

We are using DummyJSON test data for this lesson. These IDs are mock identifiers and are not associated with your real Magento orders.

### Step 2 — Retrieve order information

Add an HTTP Request node.

Rename it:

`Worker - Retrieve Order Details`

Configure:

- Method: `GET`
- URL:

```
https://dummyjson.com/carts/1
```

\- Authentication: None

Under Settings, enable Retry On Fail if available:

- Maximum tries: `3`
- Wait between tries: `1000 ms`

This demonstrates recovery from temporary API failures.

### Step 3 — Retrieve customer information

Add another HTTP Request node after the order node.

Rename it:

`Worker - Retrieve Customer Details`

Configure:

- Method: `GET`
- URL:

```
https://dummyjson.com/users/1
```

Enable Retry On Fail:

- Maximum tries: `3`
- Wait between tries: `1000 ms`

### Step 4 — Retrieve product information

Add another HTTP Request node.

Rename it:

`Worker - Retrieve Product Details`

Configure:

- Method: `GET`
- URL:

```
https://dummyjson.com/products/1
```

Enable Retry On Fail:

- Maximum tries: `3`
- Wait between tries: `1000 ms`

Your workflow should now look like:

Manual Trigger

Input - Order Investigation Request

Worker - Retrieve Order Details

Worker - Retrieve Customer Details

Worker - Retrieve Product Details

At this stage, we are deliberately using a sequential workflow. This ensures that the next operation runs only after the previous operation has completed successfully.

## 5. Combine the investigation results

After the Product Details node, add an Edit Fields node.

Rename it:

`Data - Combine Investigation Results`

Enable Include Other Input Fields if available.

Add these fields:

Investigation status

```
{{ "completed" }}
```

Order ID

```
{{ $('Worker - Retrieve Order Details').item.json.id }}
```

Order total

```
{{ $('Worker - Retrieve Order Details').item.json.total }}
```

Customer name

```
{{ $('Worker - Retrieve Customer Details').item.json.firstName + " " + $('Worker - Retrieve Customer Details').item.json.lastName }}
```

Product title

```
{{ $('Worker - Retrieve Product Details').item.json.title }}
```

Product price

```
{{ $('Worker - Retrieve Product Details').item.json.price }}
```

Processing summary

```
{{ "Investigation completed successfully. Order, customer and product information retrieved." }}
```

Run the workflow and inspect the output.

Expected result: one combined record containing the order, customer and product information.

## 6. Introduce failure recovery

This is one of the most important parts of the lesson.

Consider this scenario:

- Order retrieval succeeds.
- Customer retrieval succeeds.
- Product retrieval fails because the API is unavailable.

The workflow should not incorrectly report that the complete investigation succeeded.

We need to handle failures explicitly.

### Step 1 — Configure node-level retries

Open each of the three HTTP Request nodes.

Under Settings, configure:

- On Error: `Stop Workflow`
- Retry On Fail: Enabled
- Maximum tries: `3`
- Wait between tries: `1000 ms`

If your interface presents the retry settings differently, use the equivalent options available in your version.

### Step 2 — Add centralized error handling

We already created:

`CAO-004 - Centralized Error Handler`

Reuse that workflow rather than creating another error handler.

Set `CAO-009` to use CAO-004 as its Error Workflow.

In CAO-004, verify that the error capture node records:

- Failed workflow
- Execution ID
- Error message
- Execution URL
- Failure timestamp
- Failure status

This handles an execution that fails after retry attempts are exhausted.

### Step 3 — Understand partial failure

For example:

| Operation           | Result     |
| ------------------- | ---------- |
| Retrieve order      | Success    |
| Retrieve customer   | Success    |
| Retrieve product    | Failed     |
| Final investigation | Incomplete |

The workflow should report a failure or incomplete investigation, not a successful result.

For production systems, we will also need to decide whether successful earlier operations should be retained, retried, compensated, or resumed.

## 7. Add recovery status and retry tracking

Before the HTTP Request nodes, we can track the overall operation.

Add these fields to the initial input:

| Field                  | Value          |
| ---------------------- | -------------- |
| `retry_count`          | `0`            |
| `orchestration_status` | `in_progress`  |
| `failed_step`          | empty          |
| `recovery_status`      | `not_required` |

In production, update these values at each stage and persist them to a database. A simple Edit Fields node alone does not provide durable recovery state across separate executions.

## 8. Multi-agent systems — Practical understanding

We now have several specialized workers. The next step is to understand how AI agents could coordinate them.

Imagine this request:

"Investigate order 100045. Check the customer information, verify the products and explain whether anything requires manual review."

A coordinated system could work like this:

1. Order Investigation Agent: Determines which order information is needed.
2. Customer Investigation Agent: Retrieves customer context.
3. Product Investigation Agent: Checks product details.
4. Decision Agent: Combines the findings and prepares a recommendation.
5. Human Approval Workflow: Handles sensitive operations when necessary.

Important distinction:

- Multiple workflow nodes do not automatically mean multiple AI agents.
- Multiple AI agents should have distinct responsibilities and clearly defined inputs and outputs.
- The orchestrator controls the sequence, handoffs, retries and final result.
- Sensitive actions remain protected by the human approval gates built in Lesson 19.

We will use this design as the foundation for more advanced agent orchestration.

## 9. Test cases

Add these cases to:

`enterprise-ai-commerce-ops/test-data/workflow-test-cases.md`

| Test ID | Scenario                      | Expected result                    |
| ------- | ----------------------------- | ---------------------------------- |
| TC-124  | Retrieve order information    | Order data retrieved               |
| TC-125  | Retrieve customer information | Customer data retrieved            |
| TC-126  | Retrieve product information  | Product data retrieved             |
| TC-127  | Complete orchestration        | Combined result generated          |
| TC-128  | Temporary API failure         | Retry attempted                    |
| TC-129  | API continues failing         | Workflow failure captured          |
| TC-130  | Product retrieval fails       | Investigation not marked completed |
| TC-131  | All workers succeed           | Final status is completed          |
| TC-132  | Sensitive action identified   | Human approval remains required    |

For failure testing, temporarily use an invalid endpoint such as:

```
https://dummyjson.com/products/999999999
```

Restore the correct URL after testing.

A 404 is generally not a transient failure, so do not expect retries to make it successful. The test demonstrates how a failed operation is surfaced after the retry policy runs.

## 10. Lesson completion checklist

Lesson 20 progress

## 10/10

Created CAO-009 orchestrator

Configured order retrieval

Configured customer retrieval

Configured product retrieval

Combined results successfully

Configured retries on HTTP Request nodes

Connected CAO-004 error handler

Verified a failed operation is not reported as successful

Tested all TC-124 through TC-132

Documented actual results

Documentation reminder: Save the lesson using the filename and location at the beginning of this lesson.

Start with Steps 1–4: Create `CAO-009` and configure the three HTTP Request workers. Once those nodes are connected and the first execution succeeds, we can verify the combined output and proceed to failure recovery.