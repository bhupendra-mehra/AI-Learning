# Part 8 — Lesson 04: Conditions, Branching, Loops, and Business Routing

Lesson 04 of 30

Module 1 — Foundations

Project: Enterprise AI Commerce Operations Platform\
Workflow: `CAO-001 - Customer Request Intake`

In this lesson, we will make the workflow behave like a business system. Instead of treating every customer request the same way, we will validate its type, route it to the appropriate processing path, and handle unsupported requests explicitly.

We will extend your existing workflow, preserving its previous nodes and expressions.

## 1. What we are building

Imagine the e-commerce company receives these requests:

- “Where is my order?” → Order Operations
- “I want to return my item.” → Returns Team
- “My payment failed.” → Payments Team
- An unknown or missing request type → Exception Handling

These are business rules, not AI decisions. We should implement deterministic routing first, then introduce AI where it adds value.

Customer Request

Existing CAO-001 input

Validate Request Type

Check the supported business categories

Order Operations

order_status

Returns Team

return_request

Payments Team

payment_issue

Exception Handling

Unknown or invalid

## 2. Understand the concepts

| Concept            | Purpose in our product                                     |
| ------------------ | ---------------------------------------------------------- |
| Condition          | Checks whether a request meets a rule.                     |
| Branching          | Sends the request down different paths.                    |
| Loop               | Processes multiple items individually or in batches.       |
| Business routing   | Assigns a request to the correct team or process.          |
| Exception handling | Prevents unsupported inputs from being silently processed. |

n8n provides nodes such as IF and Switch for branching. We will use Switch for the supported request categories because it makes multiple routes easier to maintain.

## 3. Practical implementation — Add business routing to CAO-001

We will add a Switch node after your existing `Set Intake Metadata` node.

### Step 3.1 — Add the Switch node

1. Open `CAO-001 - Customer Request Intake`.
2. Add a node named `Switch - Request Routing`.
3. Connect it after `Set Intake Metadata`.
4. Select the Switch node and choose Rules mode.

Your workflow will now look like this:

Manual Trigger

Starts the test

Edit Fields

Creates the request

Set Intake Metadata

Preserves data and adds metadata

Switch - Request Routing

Selects the business route

### Step 3.2 — Configure the routing rules

Configure each rule to compare the `request_type` field against a supported value.

Use the expression below as the value to evaluate:

Your Switch node configuration is mostly correct. From your screenshot, I can see that:

- The input contains `request_type = order_status`.
- Your first rule compares `request_type` with `order_status`.
- The three routing rules and output names are configured.
- The incoming data includes all the fields from the previous nodes.

The likely issue is that the Switch node has not been executed yet, or the left panel is showing input data rather than the Switch node's output.

## 1. Verify the first rule

In `Switch - Request Routing`, the first rule should be configured as follows:

Value 1

Expression

```
{{ $json.request_type }}
```

Operation

is equal to

Value 2

order_status

Output Name

Order Operations

Value 1 appears to show `request_type` without the expression markers. Make sure the field is in Expression mode and contains the complete expression:

```
{{ $json.request_type }}
```

If you entered only `request_type` as a literal value, the comparison will not match.

Apply the same expression to all three rules, changing only Value 2:

| Rule | Value 2          | Output name      |
| ---- | ---------------- | ---------------- |
| 1    | `order_status`   | Order Operations |
| 2    | `return_request` | Returns Team     |
| 3    | `payment_issue`  | Payments Team    |

## 2. Execute the Switch node

1. Click Execute step in the top-right corner of the Switch node panel.
2. Wait for execution to finish.
3. Look for the output panel or output selector on the right.
4. Select Order Operations.

Because your input is currently `order_status`, the first output should contain one item with the original request fields and metadata.

The expected routing result is:

### Order Operations

Expected: 1 item

`request_type`

order_status

`order_reference`

ORD-100045

`processing_status`

received

## 3. If the output is still empty

Check these in order:

- Confirm that Value 1 uses the expression `{{ $json.request_type }}`.
- Confirm the incoming value is exactly `order_status`, with no extra spaces.
- Execute the Switch node again.
- Check the node's output selector; an output with no matching items will be empty.


### Step 3.3 — Understand the business behavior

The Switch node evaluates the request type and sends the item to the matching output. It does not itself send an email, create a support ticket, or contact the relevant team.

At this stage, routing means selecting the correct execution path. We will connect real business applications in later lessons.

## 4. Test the routing logic

Execute the workflow with each test value by changing `request_type` in the original Edit Fields node. Keep the rest of the request data unchanged.

| Test ID | `request_type`         | Expected route                                       |
| ------- | ---------------------- | ---------------------------------------------------- |
| TC-016  | `order_status`         | Order Operations                                     |
| TC-017  | `return_request`       | Returns Team                                         |
| TC-018  | `payment_issue`        | Payments Team                                        |
| TC-019  | `unknown_request`      | Exception Handling                                   |
| TC-020  | Empty or missing value | Exception Handling, provided the fallback catches it |

For each execution:

1. Execute the workflow.
2. Select `Switch - Request Routing`.
3. Inspect the output corresponding to the matched rule.
4. Verify that the request reaches only the intended route.
5. Confirm that the original request fields and metadata remain available in the routed output.

Restore `request_type` to `order_status` after testing.

### Troubleshooting

- No route matches: Check the spelling and capitalization of the request type.
- The wrong output is selected: Verify the rule's comparison value and expression.
- The request disappears: Inspect the Switch execution output and confirm the configured fallback behavior.
- Fields are missing: Inspect the output of `Set Intake Metadata` before the Switch node.
- The fallback output is unavailable: Use an explicit IF-based fallback rather than silently dropping unsupported requests.

## 5. Understand loops and batch processing

Not every workflow needs an explicit loop. n8n nodes generally process incoming items, while the Loop Over Items node is useful when you need to process records in controlled batches—for example, to avoid overwhelming an external API.

Consider a future daily order review:

Fetch pending orders

An API returns multiple order records

Loop Over Items

Process one record or a configured batch at a time

Check each order

Identify delayed orders and apply business rules

For example, a company might retrieve 100 orders but want to make API calls in batches of 10. A loop can help control the processing rate.

Why we are not adding Loop Over Items to CAO-001 yet: customer intake normally handles an individual request. Adding a loop without a real batch-processing requirement would complicate the workflow unnecessarily. We will implement batch processing when our platform introduces multi-record API operations.

## 6. Business routing versus AI classification

It is important to distinguish these responsibilities:

- Business rules: determine what actions are allowed and which destination receives a request.
- AI classification: infer the likely category of an unstructured message when the request type is not explicitly supplied.
- Validation: ensure the data is complete and acceptable before processing.
- Exception handling: capture unsupported or ambiguous requests for investigation.

For example, AI may infer that “I was charged twice” relates to payments. The workflow should still validate the request and apply the company's rules before allowing any consequential action.

This separation makes the product easier to test, maintain, and audit.

## 7. Lesson 04 completion checklist

Added Switch - Request Routing to the existing CAO-001 workflow.

Configured order_status, return_request, and payment_issue routes.

Configured and tested an exception route for unsupported requests.

Executed and verified test cases TC-016 through TC-020.

Confirmed that original request data is preserved and restored the default test request.

5 of 5 verified

Lesson 04 complete

Continue to Lesson 05

Next lesson — Lesson 05: Webhooks and Event-Driven Automation.

We will introduce a real webhook trigger so CAO-001 can receive dynamically submitted customer requests instead of relying on manually configured test values. We'll test the webhook locally before connecting any external commerce system.