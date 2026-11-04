# Lesson 19 — Approval Gates for Refunds, Cancellations, and Sensitive Actions

Roadmap: Version 2.3 → Part 8: AI Automation with n8n\
Project: Enterprise AI Commerce Operations Platform\
Workflow: `CAO-008 - Human Approval for Sensitive Actions`

Documentation filename: `lesson-19-approval-gates-for-refunds-cancellations-and-sensitive-actions.md`

Documentation location:

`/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-19-approval-gates-for-refunds-cancellations-and-sensitive-actions.md`

Starting Lesson 19

Lesson 18 remains incomplete and can be revisited later. We will continue with the original roadmap sequence.

## 1. What we will build

In an e-commerce platform, AI should not independently perform sensitive operations.

For example:

| Customer request        | Expected handling                          |
| ----------------------- | ------------------------------------------ |
| Check order status      | Automatic processing                       |
| Request a refund        | Human approval                             |
| Cancel an order         | Human approval                             |
| Report a payment issue  | Human review                               |
| Change delivery address | Apply business rules; approval if required |

Our workflow will ensure that sensitive actions cannot proceed without explicit human approval.

## 2. Workflow architecture

Customer Request

Validate Request

Check Approval Requirement

No approval

Automatic Processing

Approval required

Human Approval

Approved / Rejected

## 3. Create the workflow

Create a new workflow:

`CAO-008 - Human Approval for Sensitive Actions`

Add these nodes:

1. Manual Trigger
2. Edit Fields — `Input - Sensitive Action Request`
3. IF — `Decision - Approval Required?`
4. Edit Fields — `Approval - Pending Review`
5. Edit Fields — `Processing - Automatic Action`

### Step 1 — Configure the input

In Edit Fields, add these fields:

| Field              | Value         |
| ------------------ | ------------- |
| `request_id`       | `REQ-APP-001` |
| `customer_id`      | `CUST-1001`   |
| `order_reference`  | `ORD-100045`  |
| `action_type`      | `refund`      |
| `requested_amount` | `1500`        |
| `currency`         | `INR`         |
| `approval_status`  | `pending`     |

### Step 2 — Add approval decision logic

Add an IF node.

Rename it:

`Decision - Approval Required?`

Configure a Boolean condition:

Value 1:

```
{{ ["refund", "cancel_order", "payment_issue"].includes($json.action_type) }}
```

Operation: Is true

This means refunds, order cancellations and payment issues always require human approval.

### Step 3 — Configure the approval branch

Connect the IF node's true output to an Edit Fields node.

Rename it:

`Approval - Pending Review`

Add these fields:

| Field               | Value                                           |
| ------------------- | ----------------------------------------------- |
| `processing_status` | `pending_human_approval`                        |
| `approval_required` | `true`                                          |
| `approval_status`   | `pending`                                       |
| `approval_reason`   | `Sensitive action requires human authorization` |

Enable Include Other Input Fields so the original request details are preserved.

Important: This branch must not connect to any refund, cancellation, or payment execution node.

### Step 4 — Configure automatic processing

Connect the IF node's false output to another Edit Fields node.

Rename it:

`Processing - Automatic Action`

Add:

| Field               | Value                            |
| ------------------- | -------------------------------- |
| `processing_status` | `ready_for_automatic_processing` |
| `approval_required` | `false`                          |
| `approval_status`   | `not_required`                   |

Enable Include Other Input Fields.

## 4. Test the workflow

Run these tests by changing `action_type` in the input node.

| Test   | Action type           | Expected result        |
| ------ | --------------------- | ---------------------- |
| TC-112 | `refund`              | Pending human approval |
| TC-113 | `cancel_order`        | Pending human approval |
| TC-114 | `payment_issue`       | Pending human approval |
| TC-115 | `order_status`        | Automatic processing   |
| TC-116 | `product_information` | Automatic processing   |

For now, we are building the approval gate and verifying that sensitive requests are stopped before execution. The actual human approval and rejection mechanism, including recording the approver and decision, will be implemented as the next stage of this lesson.

## 5. Practical safety rule

Even if Gemini returns:

```
{
  "requires_human_review": false
}
```

a refund must still go for human approval.

Business rules must override AI decisions for sensitive operations.

Start with Step 1: Create `CAO-008` and configure the Manual Trigger and input Edit Fields node. Share a screenshot when those are ready, and we will configure the approval decision together.

TC-112 to TC-116 passed

All five approval-routing test cases are now confirmed:

| Test   | Action type           | Result                 |
| ------ | --------------------- | ---------------------- |
| TC-112 | `refund`              | Pending human approval |
| TC-113 | `cancel_order`        | Pending human approval |
| TC-114 | `payment_issue`       | Pending human approval |
| TC-115 | `order_status`        | Automatic processing   |
| TC-116 | `product_information` | Automatic processing   |

The approval decision logic is working correctly.

## Lesson 19 — Next: Implement actual human approval

Currently, your workflow marks requests as pending, but it does not yet allow a person to approve or reject them.

We will extend the true branch:

Approval - Pending Review

Wait - Human Approval

Wait for an approval form submission

IF - Request Approved?

Approved

Record approval

Rejected

Record rejection

### Step 1 — Add the Wait node

1. Open `CAO-008 - Human Approval for Sensitive Actions`.
2. Add a Wait node after `Approval - Pending Review`.
3. Select On Form Submitted as the resume condition, if available in your node.
4. Set the form title to:

`Sensitive Action Approval`

5\. Set the form description to:

`Review the customer request and approve or reject this action.`

We will configure the approval decision, approver name and comments in the form next.

Stop after adding the Wait node. Share its configuration screenshot so I can guide you through the exact form settings in your n8n 2.45 interface.

Your Wait node is configured correctly.&#x20;

Configuration verified


I can see:

- Resume: On Form Submitted
- Authentication: None
- Form Title: Sensitive Action Approval
- Form Description: Correctly configured.

Let's add the approval decision field.

## Step 2 — Add approval decision to the form

Click Add Form Element.

Configure the first field:

| Setting      | Value               |
| ------------ | ------------------- |
| Field Label  | Approval Decision   |
| Field Name   | `approval_decision` |
| Element Type | Dropdown            |
| Required     | Yes                 |
| Options      | `approve`, `reject` |

If the dropdown element doesn't support these options in your interface, use a Radio Button element instead.

## Step 3 — Add approver information

Add another form element:

| Setting      | Value           |
| ------------ | --------------- |
| Field Label  | Approver Name   |
| Field Name   | `approver_name` |
| Element Type | Text            |
| Required     | Yes             |

Add a third element:

| Setting      | Value               |
| ------------ | ------------------- |
| Field Label  | Approval Comments   |
| Field Name   | `approval_comments` |
| Element Type | Textarea            |
| Required     | No                  |

The approval form should contain three fields:

1. Approval Decision
2. Approver Name
3. Approval Comments

Do not execute the workflow yet. Configure these fields and share a screenshot of the completed Form Elements section.

# Lesson 19 — Approval Gates for Refunds, Cancellations, and Sensitive Actions

We can complete the remaining implementation in one go. Your existing workflow and tests TC-112 to TC-116 are already in place. Continue building on `CAO-008`; do not create another workflow.

## 1. Complete the approval form

In your existing Wait node, keep:

- Resume: `On Form Submitted`
- Form Title: `Sensitive Action Approval`
- Form Description: `Review the customer request and approve or reject this action.`

Under Form Elements, add these three fields.

| Field             | Element type | Field name          | Required |
| ----------------- | ------------ | ------------------- | -------- |
| Approval Decision | Dropdown     | `approval_decision` | Yes      |
| Approver Name     | Text         | `approver_name`     | Yes      |
| Approval Comments | Textarea     | `approval_comments` | No       |

For the Approval Decision dropdown, configure two options:

- `approve`
- `reject`

If your dropdown allows separate display labels and values, use Approve / `approve` and Reject / `reject`.

## 2. Connect the approval decision

After the Wait node, add an IF node.

Rename it:

`Decision - Approval Granted?`

Configure the condition:

\- Value 1:

```
{{ $json.approval_decision }}
```

- Operation: `is equal to`
- Value 2: `approve`

The workflow should now look like this:

Approval - Pending Review

Wait - Human Approval

Decision - Approval Granted?

True

Approval - Record Approved

False

Approval - Record Rejected

## 3. Configure the approved branch

Connect the IF node's true output to an Edit Fields node.

Rename it:

`Approval - Record Approved`

Add the following fields:

| Field                | Value                           |
| -------------------- | ------------------------------- |
| `processing_status`  | `approved_by_human`             |
| `approval_required`  | `true`                          |
| `approval_status`    | `approved`                      |
| `approver_name`      | `{{ $json.approver_name }}`     |
| `approval_comments`  | `{{ $json.approval_comments }}` |
| `approval_timestamp` | `{{ $now.toISO() }}`            |

Enable Include Other Input Fields to preserve the original request information, if that option is available.

This branch records authorization only. It must not execute an actual refund or cancellation.

## 4. Configure the rejected branch

Connect the IF node's false output to another Edit Fields node.

Rename it:

`Approval - Record Rejected`

Add:

| Field                | Value                           |
| -------------------- | ------------------------------- |
| `processing_status`  | `rejected_by_human`             |
| `approval_required`  | `true`                          |
| `approval_status`    | `rejected`                      |
| `approver_name`      | `{{ $json.approver_name }}`     |
| `approval_comments`  | `{{ $json.approval_comments }}` |
| `approval_timestamp` | `{{ $now.toISO() }}`            |

Enable Include Other Input Fields if available.

The rejected branch must terminate without connecting to any action-execution node.

## 5. Understand how to test the Wait form

The Wait node pauses the workflow until someone submits its generated form.

1. Save the workflow.
2. Execute it using `action_type = refund`.
3. Confirm that it reaches the Wait node and pauses.
4. Retrieve the generated form URL using the Wait node's resume form URL, available through `$execution.resumeFormUrl`.
5. Open that URL in a browser.
6. Submit the approval form.
7. Check the resumed execution and inspect the IF node and final output.

Important: The Wait node's URL is generated at runtime. You need a way to deliver that URL to the approver before the workflow reaches the Wait node, such as an email or notification node placed before it. For a local learning test, you can inspect the paused execution and its available form URL. Do not assume the URL is a permanent link.

If your n8n interface does not expose the URL in the execution details, use the Wait node's documented form URL mechanism rather than inventing a URL.

## 6. Execute approval and rejection tests

Use the following test cases.

| Test ID | Action type     | Form decision | Expected result          |
| ------- | --------------- | ------------- | ------------------------ |
| TC-117  | `refund`        | `approve`     | `approved_by_human`      |
| TC-118  | `refund`        | `reject`      | `rejected_by_human`      |
| TC-119  | `cancel_order`  | `approve`     | `approved_by_human`      |
| TC-120  | `cancel_order`  | `reject`      | `rejected_by_human`      |
| TC-121  | `payment_issue` | `approve`     | `approved_by_human`      |
| TC-122  | `payment_issue` | `reject`      | `rejected_by_human`      |
| TC-123  | `refund`        | No submission | Workflow remains waiting |

For each approval or rejection test, verify:

- Correct branch executes.
- Approver name is recorded.
- Comments are recorded when provided.
- Approval timestamp is populated.
- Original request reference and amount are preserved.
- No actual refund or cancellation is performed.

For TC-123, leave the form unsubmitted and confirm that the workflow remains paused. You can configure a timeout later as an additional production safeguard.

## 7. Add audit information

The approval decision should be traceable. Your final output should contain:

```
{
  "request_id": "REQ-APP-001",
  "customer_id": "CUST-1001",
  "order_reference": "ORD-100045",
  "action_type": "refund",
  "requested_amount": 1500,
  "currency": "INR",
  "approval_required": true,
  "approval_status": "approved",
  "approver_name": "Test Approver",
  "approval_comments": "Verified the request.",
  "processing_status": "approved_by_human",
  "approval_timestamp": "2026-11-01T..."
}
```

The timestamp above is illustrative; use the actual execution timestamp.

## 8. Security requirements

Important for production

Your current Wait node screenshot shows Authentication: None. This is acceptable only for a controlled local exercise.

Before using an approval form in production:

1. Enable suitable authentication for the approver.
2. Verify the approver's identity and authorization on the server side.
3. Do not rely on the typed `approver_name` field as proof of identity.
4. Restrict access to approval URLs.
5. Record the request ID, authenticated approver, decision and timestamp.
6. Prevent duplicate or expired approvals.
7. Ensure pending and rejected requests cannot reach sensitive action nodes.

A human approval is not merely a form submission. It must be an authenticated, auditable authorization.

## 9. Update your test register

Add TC-117 through TC-123 to:

`enterprise-ai-commerce-ops/test-data/workflow-test-cases.md`

Record the actual outcome for each test.

## 10. Lesson 19 completion checklist

Completion progress

## 8/8

Configured the approval form with decision, approver name and comments

Connected Wait node to the approval decision IF node

Configured approved and rejected branches

Verified original request information is preserved

Passed TC-117 through TC-122

Verified pending behavior with TC-123

Recorded results in workflow-test-cases.md

Confirmed no sensitive operation executes without approval

Lesson 19 is complete when all implementation and test cases pass. Do not connect real commerce refund or cancellation APIs in this learning workflow.

Next roadmap lesson: Lesson 20 — Multi-step Orchestration and Recovery from Partial Failures. This will build on our existing workflows and introduce coordinated multi-step processing, recovery strategies and multi-agent concepts without changing the original roadmap sequence.