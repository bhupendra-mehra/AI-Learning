Agreed. We will continue Lesson 20 and cover the remaining topics that we can implement and verify now, rather than spending more time troubleshooting the retry and centralized error-handling issues.

We will preserve the original roadmap and avoid creating additional lesson numbers.

## Lesson 20 — Remaining implementation

We have already covered:

- Sequential workflow orchestration.
- Order, customer and product retrieval.
- Combining investigation results.
- Basic retry configuration.
- The concepts of specialized workers and multi-agent systems.

We will now complete three practical areas:

1. Parallel execution: Retrieve independent information simultaneously.
2. Reusable sub-workflows: Separate business operations into independent workflows and coordinate them from CAO-009.
3. Multi-agent coordination design: Define specialist responsibilities, handoffs, shared results and a central coordinator.

We will leave the problematic retry verification, CAO-004 integration and partial-failure recovery tests deferred. We will not mark them as completed.

## Part A — Parallel execution

Currently, CAO-009 retrieves information sequentially:

Order → Customer → Product.

However, these three API calls are independent. We can run them simultaneously and reduce overall execution time.

### 1. Update CAO-009

Open:

`CAO-009 - Order Operations Orchestrator`

Keep the existing input node:

`Input - Order Investigation Request`

Disconnect the sequential connections between the three HTTP Request nodes.

Create three independent connections from the input node:

Input - Order Investigation Request

Order API

/carts/1

Customer API

/users/1

Product API

/products/1

Use your existing HTTP Request nodes:

| Node                               | Method | URL                                |
| ---------------------------------- | ------ | ---------------------------------- |
| Worker - Retrieve Order Details    | GET    | `https://dummyjson.com/carts/1`    |
| Worker - Retrieve Customer Details | GET    | `https://dummyjson.com/users/1`    |
| Worker - Retrieve Product Details  | GET    | `https://dummyjson.com/products/1` |

All three should receive connections directly from the input node.

### 2. Combine the parallel results

Add a Merge node.

Rename it:

`Merge - Order and Customer Results`

Configure:

- Mode: `Combine`
- Combine By: `Position`

Connect:

- Input 1: Order Details
- Input 2: Customer Details

Add another Merge node:

`Merge - All Investigation Results`

Configure the same settings:

- Mode: `Combine`
- Combine By: `Position`

Connect:

- Input 1: `Merge - Order and Customer Results`
- Input 2: Product Details

The final architecture:

Customer Investigation Input

Order

Customer

Product

Merge 1 — Order + Customer

Merge 2 — Combined Results

Data - Combine Investigation Results

Important: The Merge node combines items by their position. This exercise uses one item per branch. For production, we will need to handle different item counts and matching identifiers explicitly.

### 3. Test parallel execution

Execute CAO-009.

Verify:

- All three HTTP Request nodes execute.
- Both Merge nodes execute.
- The final node receives the combined result.
- The output contains order, customer and product information.

Compare the execution duration with your earlier sequential execution. Parallel execution should reduce the total time when the API calls are independent, although actual results depend on network and service latency.

## Part B — Reusable sub-workflows

A good enterprise workflow should not contain every operation inside one enormous workflow.

Instead, we can create reusable workers and let CAO-009 coordinate them.

### 1. Create three worker workflows

Create these workflows:

| Workflow                                  | Responsibility                  |
| ----------------------------------------- | ------------------------------- |
| `CAO-010 - Order Investigation Worker`    | Retrieve order/cart information |
| `CAO-011 - Customer Investigation Worker` | Retrieve customer information   |
| `CAO-012 - Product Investigation Worker`  | Retrieve product information    |

Each workflow should have this structure:

Execute Sub-workflow Trigger

Accept input from parent workflow

HTTP Request

Retrieve the relevant information

Edit Fields

Prepare standardized worker response

### 2. Configure the Order Investigation Worker

Open `CAO-010 - Order Investigation Worker`.

Add the Execute Sub-workflow Trigger node. Depending on the n8n node label, it may appear as `When Executed by Another Workflow`.

Configure its input:

| Field     | Type   |
| --------- | ------ |
| `cart_id` | Number |

Add an HTTP Request node.

- Method: GET
- URL:

```
{{ 'https://dummyjson.com/carts/' + $json.cart_id }}
```

Add an Edit Fields node after it.

Create:

| Field                 | Expression                  |
| --------------------- | --------------------------- |
| `order_id`            | `{{ $json.id }}`            |
| `order_total`         | `{{ $json.total }}`         |
| `order_user_id`       | `{{ $json.userId }}`        |
| `order_product_count` | `{{ $json.totalProducts }}` |

Save the workflow.

### 3. Configure the Customer Investigation Worker

Create `CAO-011 - Customer Investigation Worker`.

Trigger input:

| Field         | Type   |
| ------------- | ------ |
| `customer_id` | Number |

HTTP Request:

```
{{ 'https://dummyjson.com/users/' + $json.customer_id }}
```

Add Edit Fields after the HTTP Request:

| Field                 | Expression              |
| --------------------- | ----------------------- |
| `customer_first_name` | `{{ $json.firstName }}` |
| `customer_last_name`  | `{{ $json.lastName }}`  |
| `customer_email`      | `{{ $json.email }}`     |

Save.

### 4. Configure the Product Investigation Worker

Create `CAO-012 - Product Investigation Worker`.

Trigger input:

| Field        | Type   |
| ------------ | ------ |
| `product_id` | Number |

HTTP Request:

```
{{ 'https://dummyjson.com/products/' + $json.product_id }}
```

Add Edit Fields:

| Field              | Expression             |
| ------------------ | ---------------------- |
| `product_title`    | `{{ $json.title }}`    |
| `product_price`    | `{{ $json.price }}`    |
| `product_category` | `{{ $json.category }}` |

Save.

These workers now have defined inputs and standardized outputs. They can be reused by other workflows.

### 5. Call the workers from CAO-009

Return to `CAO-009`.

Add three Execute Sub-workflow nodes:

- `Execute - Order Investigation Worker`
- `Execute - Customer Investigation Worker`
- `Execute - Product Investigation Worker`

For each node:

1. Select the corresponding workflow.
2. Select the option to define workflow inputs.
3. Map the input values from `Input - Order Investigation Request`.

| Parent field  | Worker input                                                           |
| ------------- | ---------------------------------------------------------------------- |
| `cart_id`     | `{{ $('Input - Order Investigation Request').item.json.cart_id }}`     |
| `customer_id` | `{{ $('Input - Order Investigation Request').item.json.customer_id }}` |
| `product_id`  | `{{ $('Input - Order Investigation Request').item.json.product_id }}`  |

Configure the sub-workflow execution to wait for completion before returning its result, if that option is displayed.

Connect the three Execute Sub-workflow nodes to the two Merge nodes using the same pattern from Part A.

You now have a parent workflow coordinating three independent child workflows.

Reusable orchestration implemented

## Part C — Multi-agent coordination

We need to distinguish three concepts:

| Concept         | Meaning                                                       |
| --------------- | ------------------------------------------------------------- |
| Workflow worker | Performs a predefined business operation                      |
| AI agent        | Uses an LLM to reason and select tools or actions             |
| Orchestrator    | Coordinates workers or agents and manages the overall process |

Our CAO-010, CAO-011 and CAO-012 are currently specialized workflow workers, not autonomous AI agents.

We will now define how the AI agents would collaborate in the enterprise platform.

### 1. Define the specialist responsibilities

| Specialist                  | Input                     | Output            |
| --------------------------- | ------------------------- | ----------------- |
| Order Investigation Agent   | Order reference           | Order findings    |
| Customer Context Agent      | Customer ID               | Customer findings |
| Product Investigation Agent | Product IDs               | Product findings  |
| Decision Coordinator Agent  | All investigation results | Recommendation    |
| Approval Workflow           | Sensitive action request  | Approval decision |

### 2. Define the coordination process

For example, a customer asks:

"Please investigate my order and tell me whether there is any issue with the products."

The coordinator follows this process:

1. Understand the request.
2. Identify the required order reference.
3. Call the Order Investigation Worker.
4. Identify the customer and products from the returned data.
5. Call the Customer and Product Investigation Workers.
6. Combine the results.
7. Send the findings to the Decision Coordinator.
8. If a sensitive action is requested, route it to CAO-008.
9. Generate the final customer response.

### 3. Define the agent response contract

All specialist agents should return structured data rather than arbitrary text.

Example:

```
{
  "agent_name": "order_investigation",
  "status": "success",
  "findings": {
    "order_id": 1,
    "total_amount": 479,
    "product_count": 5
  },
  "requires_human_review": false,
  "reason": "Order information retrieved successfully."
}
```

The coordinator should be able to consume this output without depending on the agent's conversational wording.

### 4. Define coordination rules

- An agent must not claim information it has not retrieved.
- Agents must not independently execute refunds or cancellations.
- Agents must return structured results.
- The coordinator must track which workers have completed.
- Failed workers must not be treated as successful.
- The final recommendation must be based on verified worker outputs.
- Human approval remains mandatory for sensitive actions.

Important: This completes the multi-agent architecture and coordination design. We are not claiming to have deployed five autonomous AI agents. That implementation will be part of the complete business integration in Lesson 22.

## Part D — Add Lesson 20 test cases

Add these new cases to:

`enterprise-ai-commerce-ops/test-data/workflow-test-cases.md`

| Test ID | Scenario                            | Expected result                           |
| ------- | ----------------------------------- | ----------------------------------------- |
| TC-133  | Parallel order retrieval            | Order worker executes                     |
| TC-134  | Parallel customer retrieval         | Customer worker executes                  |
| TC-135  | Parallel product retrieval          | Product worker executes                   |
| TC-136  | Merge parallel results              | All three results combined                |
| TC-137  | Order sub-workflow                  | Returns standardized order output         |
| TC-138  | Customer sub-workflow               | Returns standardized customer output      |
| TC-139  | Product sub-workflow                | Returns standardized product output       |
| TC-140  | Parent orchestrator calls workers   | All three workers return results          |
| TC-141  | Worker response contract            | Output follows the defined structure      |
| TC-142  | Coordinator receives worker results | Coordinator has all investigation results |
| TC-143  | Sensitive action detected           | Approval remains mandatory                |

Do not mark any test as passed until you have executed it.

## Part E — Lesson 20 final coverage

## Lesson 20 completion tracker

Check each item only after completing or confirming its implementation.

Sequential orchestration

Covered

Parallel execution

To implement

Merge and aggregate results

To implement

Reusable sub-workflows

To implement

Specialized workflow workers

To implement

Multi-agent coordination architecture

To implement

Structured worker response contracts

To implement

Retry and centralized error handling

Deferred

Deferred

Partial failure recovery and resume

Deferred

Deferred

Remaining implementation items

## 7

Documentation: Update the existing file:

`/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-20-multi-step-orchestration-and-recovery-from-partial-failures.md`

Preserve the original sections and append the parallel execution, reusable sub-workflow and multi-agent coordination sections.

Recommended implementation order: Complete Part A first, then Part B, and finally Part C. This gives us a working parallel orchestrator, reusable workers and a defined coordination model without getting blocked by the error-handling issues.

After these additions, Lesson 20 will have its major orchestration and multi-agent topics covered. The deferred failure-recovery objectives will remain explicitly open for the later integration milestone.