We will now build the complete integration in one pass, without stopping to verify every individual node. We will run the full workflow afterward and fix errors based on actual execution results.

The following connection plan includes the existing CAO-001 to CAO-003 connection and all the workflows we have built so far.

# Lesson 22 — Complete workflow integration

## 1. Final architecture

CAO-001 — Customer Request Intake

Webhook → Metadata → Normalize → Validate

CAO-003 — AI Classification and Extraction

Gemini → Extraction → AI output validation → Decision

CAO-009 — Order Operations Orchestrator

Parallel investigation and AI Decision Coordinator

CAO-010

Order Worker

CAO-011

Customer Worker

CAO-012

Product Worker

Decision and Business Rules

CAO-008

Human Approval

Automatic Response

Non-sensitive requests

Final Customer Response and Audit

## 2. Workflow connection list

| From workflow | Destination workflow | Purpose                                     |
| ------------- | -------------------- | ------------------------------------------- |
| CAO-001       | CAO-003              | Classify validated customer request         |
| CAO-003       | CAO-009              | Investigate order and retrieve related data |
| CAO-009       | CAO-010              | Retrieve order/cart information             |
| CAO-009       | CAO-011              | Retrieve customer information               |
| CAO-009       | CAO-012              | Retrieve product information                |
| CAO-003       | CAO-008              | Send sensitive requests for human approval  |
| CAO-009       | Final response       | Prepare order investigation response        |
| CAO-008       | Final response       | Prepare approved/rejected response          |

CAO-010, CAO-011 and CAO-012 are already called by CAO-009. We do not need to add those connections again.

## 3. CAO-001 — Customer Request Intake

Your existing connection is:

```
Webhook / Manual Trigger
        ↓
Edit Fields
        ↓
Intake Metadata
        ↓
Data - Normalize and Validate Request
        ↓
Validation - Is Request Valid?
        ├── True → Execute Sub-workflow: CAO-003
        └── False → Response - Reject Invalid Request
```

The true branch is already connected to an Execute Sub-workflow node.

Important: Your latest screenshot shows the workflow named `CAO-003 - AI Request Classification Test`. Our intended integration target is `CAO-003 - AI Classification and Extraction`. Make sure the Execute Sub-workflow node selects the latter, not the test workflow.

Keep the existing Switch and mock API path disconnected from this new integration path for now. We can reuse or remove the old path after the complete flow works.

## 4. CAO-003 — AI Classification and Extraction

Your existing workflow already has:

- `When Executed by Another Workflow`
- `Webhook`
- `Input - Customer Message`
- `Security - Prepare Safe AI Input`
- `Basic LLM Chain`
- `Data - Prepare Extracted Request`
- AI output validation
- Human review decision
- Automatic processing branch
- Error capture branch

The target connections should be:

```
When Executed by Another Workflow ─┐
                                   ├→ Input - Customer Message
Webhook ────────────────────────────┘
        ↓
Security - Prepare Safe AI Input
        ↓
Basic LLM Chain
        ├── Error → Error - Capture AI Failure → Stop And Error
        ↓
Data - Prepare Extracted Request
        ↓
Validation - Validate AI Output
        ↓
Validation - Is AI Output Valid?
        ├── False → Validation - Send Invalid Output to Review
        └── True → Decision - Human Review Required?
                    ├── True → Review - Pending Human Approval
                    │           ↓
                    │       Call CAO-008
                    │
                    └── False → Processing - Automatic Request
                                ↓
                            Call CAO-009
```

Add two Execute Sub-workflow nodes:

1. After `Processing - Automatic Request`, select `CAO-009 - Order Operations Orchestrator`.
2. After `Review - Pending Human Approval`, select `CAO-008 - Human Approval for Sensitive Actions`.

Keep the invalid AI output branch separate. It should not automatically execute the order or refund workflow.

## 5. CAO-009 — Order Operations Orchestrator

This workflow already contains the three worker calls and AI Decision Coordinator.

Its internal architecture should remain:

```
Trigger
  ↓
Prepare Investigation Input
  ├── Call CAO-010 — Order Investigation Worker
  ├── Call CAO-011 — Customer Investigation Worker
  └── Call CAO-012 — Product Investigation Worker
          ↓
    Combine Investigation Results
          ↓
    AI Decision Coordinator
          ↓
    Final Investigation Result
```

Keep the existing parallel execution, Merge nodes and worker configurations.

The parent workflow should receive the output from CAO-003, including the customer message, order reference and request ID. We will fix any field mapping issues during the full test.

## 6. CAO-008 — Human Approval for Sensitive Actions

This is your existing approval workflow. It needs to be callable as a sub-workflow.

Add a `When Executed by Another Workflow` trigger and connect it to the same `Edit Fields - Input Sensitive Action Request` node currently used by the Manual Trigger.

Target connections:

```
Manual Trigger ─────────────────────┐
                                    ├→ Input - Sensitive Action Request
When Executed by Another Workflow ──┘
        ↓
Decision - Approval Required?
        ├── True → Approval - Pending Review
        │           ↓
        │         Wait - Approval Form
        │           ↓
        │         Decision - Approval Granted?
        │           ├── True → Approval - Record Approved
        │           └── False → Approval - Record Rejected
        │
        └── False → Processing - Automatic Action
```

The Wait node should remain in place. The execution will wait until the approver submits the form.

For this learning environment, keep the approval form restricted to your test use. Production use requires authenticated approvers.

## 7. Final response and audit

We need a final response stage for both branches.

Create a new workflow:

`CAO-013 - Customer Response and Audit`

This will be the final reusable workflow.

Initial structure:

```
When Executed by Another Workflow
        ↓
Data - Prepare Customer Response
        ↓
Data - Prepare Audit Record
        ↓
Return Final Response
```

Connect:

- CAO-009 output → CAO-013
- CAO-008 approved output → CAO-013
- CAO-008 rejected output → CAO-013

The response should clearly distinguish:

- Order information retrieved
- Approval pending
- Approved action
- Rejected action
- Investigation failure

Do not claim a refund, cancellation or other real commerce action has occurred just because approval was granted. Actual commerce execution will be a separate controlled step.

## 8. CAO-009 and CAO-008: required trigger changes

Both workflows need to accept calls from other workflows.

For each one:

1. Open the workflow.
2. Add When Executed by Another Workflow.
3. Connect it to the same first processing node used by the existing Manual Trigger.
4. Keep the Manual Trigger connected for independent testing.

For CAO-009:

```
Manual Trigger ──────────────────────┐
When Executed by Another Workflow ───┴→ Existing first processing node
```

For CAO-008, use the same arrangement.

Do not delete the existing triggers.

## 9. Final response — keep it inside CAO-001

Rather than creating another workflow unnecessarily, use the existing CAO-001 as the main entry and response workflow.

After the CAO-003 Execute Sub-workflow node, add:

Edit Fields — `Response - Prepare Final Customer Response`

The final connection becomes:

```
CAO-001
   ↓
Call CAO-003
   ↓
Response - Prepare Final Customer Response
```

This works because CAO-003 will call CAO-009 or CAO-008 internally and return its result to CAO-001.

We will configure the final response fields after seeing the actual integrated output.

## 10. Execution order — build checklist

Use this order so you can make all the connections without repeatedly switching workflows.

Integration checklist

0/10

CAO-001: Select the correct CAO-003 workflow in Execute Sub-workflow.

CAO-003: Keep both incoming triggers connected to Input - Customer Message.

CAO-003: Connect Processing - Automatic Request to CAO-009.

CAO-003: Connect Review - Pending Human Approval to CAO-008.

CAO-009: Add When Executed by Another Workflow and connect it to the existing first node.

CAO-009: Keep CAO-010, CAO-011 and CAO-012 worker calls connected.

CAO-008: Add When Executed by Another Workflow and connect it to the existing first node.

CAO-008: Preserve the Wait, approval decision, approved and rejected branches.

CAO-001: Add Response - Prepare Final Customer Response after the CAO-003 call.

Save all modified workflows.

## 11. Full-flow test cases

After all connections are built, test these scenarios:

| Test | Customer request                     | Expected result                         |
| ---- | ------------------------------------ | --------------------------------------- |
| 1    | Please check my order status.        | CAO-009 investigates order              |
| 2    | I want to return my recent purchase. | CAO-008 requests human approval         |
| 3    | I want to cancel my order.           | Human approval required                 |
| 4    | I have a payment issue.              | Human approval required                 |
| 5    | What products are available?         | Classification and appropriate response |
| 6    | Missing order reference              | Validation/review handling              |
| 7    | Invalid webhook authentication       | Request rejected                        |

Use mock data only. No real refund, cancellation or payment action should be performed.

One important naming correction before you continue: your latest CAO-003 screenshot shows the title `CAO-003 - AI Request Classification Test`, whereas the intended workflow is `CAO-003 - AI Classification and Extraction`. Make sure the Execute Sub-workflow node selects the intended workflow, not the test workflow.

Build the connections in sections 3–9 first. You do not need to send screenshots after every connection. Once all connections are saved, share the CAO-001 full canvas screenshot and we will run the first end-to-end test, fixing any errors together.