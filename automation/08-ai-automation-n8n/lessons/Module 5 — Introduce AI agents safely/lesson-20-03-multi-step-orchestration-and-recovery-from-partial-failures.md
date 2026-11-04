We will continue with Lesson 20, Steps 2–5, keeping your customer-name fix and parallel Merge implementation intact.

The target is to make CAO-009 a proper parent orchestrator that calls three reusable workflows, combines their results and passes the findings to an AI Decision Coordinator.

We will not delete the existing HTTP Request nodes until the replacement workers have been tested successfully.

## Step 2 — Verify the three reusable worker workflows

We need three independent workflows, each with its own trigger, API request and standardized output.

### 2.1 CAO-010 — Order Investigation Worker

Expected workflow structure

```
Execute Sub-workflow Trigger
          ↓
HTTP Request - Retrieve Cart
          ↓
Edit Fields - Prepare Order Result
```

Verify the following:

Trigger input

| Field     | Type   |
| --------- | ------ |
| `cart_id` | Number |

HTTP Request

- Method: GET
- URL:

```
{{ 'https://dummyjson.com/carts/' + $json.cart_id }}
```

Edit Fields output

| Field                 | Expression                  |
| --------------------- | --------------------------- |
| `order_id`            | `{{ $json.id }}`            |
| `order_total`         | `{{ $json.total }}`         |
| `order_user_id`       | `{{ $json.userId }}`        |
| `order_product_count` | `{{ $json.totalProducts }}` |

### 2.2 CAO-011 — Customer Investigation Worker

Structure:

```
Execute Sub-workflow Trigger
          ↓
HTTP Request - Retrieve Customer
          ↓
Edit Fields - Prepare Customer Result
```

Trigger input

| Field         | Type   |
| ------------- | ------ |
| `customer_id` | Number |

HTTP Request URL

```
{{ 'https://dummyjson.com/users/' + $json.customer_id }}
```

Edit Fields output

| Field                 | Expression              |
| --------------------- | ----------------------- |
| `customer_first_name` | `{{ $json.firstName }}` |
| `customer_last_name`  | `{{ $json.lastName }}`  |
| `customer_email`      | `{{ $json.email }}`     |

### 2.3 CAO-012 — Product Investigation Worker

Structure:

```
Execute Sub-workflow Trigger
          ↓
HTTP Request - Retrieve Product
          ↓
Edit Fields - Prepare Product Result
```

Trigger input

| Field        | Type   |
| ------------ | ------ |
| `product_id` | Number |

HTTP Request URL

```
{{ 'https://dummyjson.com/products/' + $json.product_id }}
```

Edit Fields output

| Field              | Expression             |
| ------------------ | ---------------------- |
| `product_title`    | `{{ $json.title }}`    |
| `product_price`    | `{{ $json.price }}`    |
| `product_category` | `{{ $json.category }}` |

For each workflow, save it and test the trigger with its sample input.

Expected sample values:

- Cart ID: `1`
- Customer ID: `1`
- Product ID: `1`

Confirm that each worker returns its standardized output.

## Step 3 — Replace direct HTTP Request nodes in CAO-009

Once all three workers have passed their individual tests, update:

`CAO-009 - Order Operations Orchestrator`

### 3.1 Add three Execute Sub-workflow nodes

Search for the node named Execute Sub-workflow (sometimes displayed as Execute Workflow).

Add:

1. `Execute - Order Investigation Worker`
2. `Execute - Customer Investigation Worker`
3. `Execute - Product Investigation Worker`

For each node, select its corresponding workflow.

Configure the inputs:

| Execute node    | Input field   | Value                                                                  |
| --------------- | ------------- | ---------------------------------------------------------------------- |
| Order Worker    | `cart_id`     | `{{ $('Input - Order Investigation Request').item.json.cart_id }}`     |
| Customer Worker | `customer_id` | `{{ $('Input - Order Investigation Request').item.json.customer_id }}` |
| Product Worker  | `product_id`  | `{{ $('Input - Order Investigation Request').item.json.product_id }}`  |

If the node offers an option to wait for the sub-workflow to finish, enable it.

### 3.2 Connect the parent workflow

Use this structure:

Input - Order Investigation Request

Execute Order Worker

Execute Customer Worker

Execute Product Worker

Merge 1 — Order + Customer

Merge 2 — All Results

Data - Combine Investigation Results

Keep your existing Merge nodes configured as:

- Mode: Combine
- Combine By: Position

The order of the inputs must match the corresponding branches.

### 3.3 Test the parent workflow

Use these inputs:

| Field         | Value |
| ------------- | ----- |
| `cart_id`     | `1`   |
| `customer_id` | `1`   |
| `product_id`  | `1`   |

Verify:

- All three Execute Sub-workflow nodes complete.
- Each child workflow returns its standardized output.
- Both Merge nodes execute.
- The final Edit Fields node receives all three results.
- `customer_name` displays the correct first and last name.

### 3.4 Remove the old HTTP Request nodes

After the new parent workflow passes:

- Remove the old direct `Worker - Retrieve Order Details` node.
- Remove the old direct `Worker - Retrieve Customer Details` node.
- Remove the old direct `Worker - Retrieve Product Details` node.

Keep the HTTP Request nodes inside CAO-010, CAO-011 and CAO-012. Those are now the reusable implementations.

Also update the final result expressions to read from the standardized merged fields:

```
{{ $json.order_id }}
```

```
{{ $json.order_total }}
```

```
{{ $json.customer_first_name + " " + $json.customer_last_name }}
```

```
{{ $json.product_title }}
```

```
{{ $json.product_price }}
```

## Step 4 — Implement multi-agent coordination

Now we will introduce an AI Decision Coordinator that consumes the findings from our three specialist workers.

The distinction is important:

- CAO-010, CAO-011 and CAO-012 are specialist workflow workers.
- Gemini will act as the AI Decision Coordinator.
- CAO-009 remains responsible for orchestration and business rules.

We are implementing a coordinated AI workflow, not three autonomous agents independently making business decisions.

### 4.1 Add the AI Decision Coordinator

After `Data - Combine Investigation Results`, add a Basic LLM Chain node.

Rename it:

`AI - Decision Coordinator`

Connect your existing Google Gemini Chat Model to its Model input.

Set the prompt source to Define below.

Use this prompt in Expression mode:

```
{{ "Review the following e-commerce investigation results:\n\n" + JSON.stringify($json, null, 2) + "\n\nPrepare a concise investigation summary. Identify the order, customer and product information. Highlight any missing or inconsistent information. Do not invent delivery status, payment status, refund status or other facts that are not present in the supplied data. Do not approve or execute refunds or cancellations. Recommend human review whenever a sensitive action is requested." }}
```

### 4.2 Configure the AI coordinator instructions

If your Basic LLM Chain interface supports a separate system message or system prompt, use:

```
You are the Decision Coordinator for an
enterprise e-commerce operations platform.

Your responsibilities:
1. Review results received from specialist workers.
2. Summarize verified order information.
3. Identify missing or inconsistent information.
4. Clearly distinguish verified facts from assumptions.
5. Recommend the next business step.

Rules:
- Never invent missing information.
- Do not claim that an order has shipped or been delivered
  unless the provided data confirms it.
- Do not independently approve refunds or cancellations.
- Always recommend human approval for sensitive actions.
- If a worker result is missing, report incomplete
  investigation instead of claiming success.
```

### 4.3 Test the coordinator

Execute CAO-009 again.

Expected:

- The three workers return their information.
- The Merge nodes combine their results.
- The final Edit Fields node creates the investigation record.
- Gemini receives the complete investigation record.
- The AI generates a summary based on the supplied information.

Example of an acceptable summary:

```
Investigation completed.

Order ID: 1
Customer: Emily Johnson
Order total: 13037.88
Product: Essence Mascara Lash Princess
Product price: 9.99

Order, customer and product information were
successfully retrieved.

Delivery and payment status were not available
in the retrieved data and require further verification.
```

This is a decision-support component. The AI summary must not override business rules or the human approval workflow.

## Step 5 — Final Lesson 20 verification

Update your test register:

`enterprise-ai-commerce-ops/test-data/workflow-test-cases.md`

Add these test cases:

| Test ID | Scenario                              | Expected result                        |
| ------- | ------------------------------------- | -------------------------------------- |
| TC-133  | Execute order worker independently    | Standardized order output              |
| TC-134  | Execute customer worker independently | Standardized customer output           |
| TC-135  | Execute product worker independently  | Standardized product output            |
| TC-136  | Merge all three worker outputs        | Complete combined record               |
| TC-137  | Execute CAO-010 from CAO-009          | Order worker returns results           |
| TC-138  | Execute CAO-011 from CAO-009          | Customer worker returns results        |
| TC-139  | Execute CAO-012 from CAO-009          | Product worker returns results         |
| TC-140  | Execute all workers through parent    | All three workers complete             |
| TC-141  | Verify worker response structure      | Standardized fields preserved          |
| TC-142  | AI Decision Coordinator               | Generates findings from worker results |
| TC-143  | Sensitive action recommendation       | Human approval remains mandatory       |

Also verify these architecture requirements:

- CAO-009 contains no duplicate direct HTTP Request nodes.
- Each child workflow can execute independently.
- Parent workflow passes the correct IDs.
- All three workers can execute in parallel.
- Merge nodes combine the expected results.
- AI Decision Coordinator receives the complete result.
- No sensitive operation is executed by the AI coordinator.

## Lesson 20 — What remains deferred?

We are deliberately leaving these items for the complete integration milestone:

| Topic                                                      | Status                  |
| ---------------------------------------------------------- | ----------------------- |
| Retry verification                                         | Deferred                |
| CAO-004 centralized error handling                         | Deferred                |
| Partial failure recovery                                   | Deferred                |
| Resume failed operations without repeating successful work | Deferred                |
| Production-grade multi-agent autonomy                      | Advanced implementation |

These are not completed or passed yet.

## Final architecture

CAO-009 — Main Orchestrator

CAO-010

Order Worker

CAO-011

Customer Worker

CAO-012

Product Worker

Merge and Aggregate Results

AI Decision Coordinator

Business Rules and Human Approval

Final Customer Response

Documentation filename: `lesson-20-multi-step-orchestration-and-recovery-from-partial-failures.md`

Documentation location:

`/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/`

Append the new implementation sections to the existing Lesson 20 document rather than creating another file.

Implementation order: Finish and test CAO-010, CAO-011 and CAO-012 first. Then replace the old HTTP Request nodes in CAO-009, verify the Merge output, and finally add the AI Decision Coordinator.

We will mark the newly implemented topics complete only after their tests pass.