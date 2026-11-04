# Part 8 — Lesson 02: Workflow Architecture, Nodes, Connections, and Execution

Lesson 02 of 30

Module 1 — Foundations

Practical project: Enterprise AI Commerce Operations Platform

We will extend your existing `CAO-001 — Customer Request Intake` workflow. No new practice project, no repeated setup, and no changes to Magento.

## 1. Lesson objectives

By the end of this lesson, you will understand:

- How n8n passes data from one node to another.
- The difference between a node's configuration and its execution output.
- How to inspect input and output data to troubleshoot a workflow.
- How to structure a workflow so that future validation, APIs, AI classification, and exception handling can be added safely.
- How to document and test changes in your enterprise project.

## 2. Update your learning files

From your AI-Learning repository, open:

```
automation/08-ai-automation-n8n/lessons/lesson-02-workflow-architecture.md
```

Keep the hands-on work in your existing `enterprise-ai-commerce-ops/` directory. The learning file records the concepts, steps, expected results, and test evidence.

## 3. Understand the architecture

Your current workflow has two nodes:

Manual Trigger

Starts a test execution

Edit Fields

Creates six customer-request fields

Each component has a specific responsibility:

- Workflow: the complete automation.
- Node: one processing step.
- Connection: the path through which execution and data move.
- Input: the data a node receives.
- Output: the data a node produces.
- Execution: one run of the workflow, including its node results.

In a business workflow, these distinctions matter. If an order reference disappears between two nodes, inspecting the relevant input and output helps identify where the problem occurred.

## 4. Practical exercise — Extend CAO-001

We will add a second processing step that marks a request as received. This is a small but realistic foundation for the processing stages we will add later.

### Step 4.1 — Add a new node

Open `CAO-001 - Customer Request Intake` in n8n.

1. Select the connection after your existing Edit Fields node.
2. Add another Edit Fields (Set) node.
3. Rename it `Set Intake Metadata`.
4. Confirm the connection order is:

Manual Trigger

Starts the workflow

Edit Fields

Creates the customer request

Set Intake Metadata

Adds processing metadata

### Step 4.2 — Configure the metadata

Inside `Set Intake Metadata`, use Manual Mapping and add these fields:

| Field name          | Type   | Value      |
| ------------------- | ------ | ---------- |
| `processing_status` | String | `received` |
| `workflow_version`  | String | `1.0`      |

Find the option called Include Other Input Fields or the equivalent option in your n8n version. Enable it so that the six fields from the previous node remain in the output.

This setting is important: without it, the new node may output only the two fields you just created, dropping the customer request information.

Do not modify the original Edit Fields node.

## 5. Execute and inspect the data

Click Execute Workflow, then select `Set Intake Metadata`.

The output should now contain eight fields:

### Expected output

8 fields

Six original request fields plus two metadata fields.

`request_id`

REQ-2026-0001

`request_type`

order_status

`customer_email`

customer\@example.com

`order_reference`

ORD-100045

`channel`

web_form

`message`

Please provide an update on my order.

`processing_status`

received

`workflow_version`

1.0

The node output is the source of truth. If you see fewer than eight fields, inspect the Include Other Input Fields setting and the previous node's output.

### Why this matters in enterprise automation

Imagine that we later add an AI classification node. It might return a category such as `delivery_issue`. If that node accidentally discards the order reference or customer email, subsequent integrations may not know which order or customer to process.

Learning to preserve and inspect data now prevents these problems as the workflow becomes more complex.

## 6. Test the workflow

Add these results to your existing test documentation. Run each test in n8n before marking it as passed.

| Test ID | Test                                 | Expected result                              |
| ------- | ------------------------------------ | -------------------------------------------- |
| TC-006  | Execute the three-node workflow      | Successful execution                         |
| TC-007  | Inspect `Set Intake Metadata` output | Eight fields                                 |
| TC-008  | Verify the original order reference  | `ORD-100045` is preserved                    |
| TC-009  | Verify metadata                      | `received` and `1.0`                         |
| TC-010  | Inspect node execution results       | Results are available for each executed node |

If a test fails, inspect the node immediately before the failure and compare its output with the next node's input.

## 7. Update the learning documentation

Save the following content in `AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-02-workflow-architecture.md`.

# Lesson 02 — Workflow Architecture, Nodes, Connections, and Execution

## Objective

Understand node responsibilities, data flow, connections, and execution inspection by extending CAO-001 — Customer Request Intake.

## Concepts Learned

- A workflow combines multiple processing nodes.
- Connections determine execution flow.
- Each node has configuration, input, and output.
- Execution results help isolate failures.
- Include Other Input Fields helps preserve incoming data when adding fields through Edit Fields.

## Practical Implementation

Extended CAO-001 with the following nodes:

1. Manual Trigger
2. Edit Fields — creates six request fields.
3. Set Intake Metadata — adds processing_status and workflow_version.

## Expected Result

One item containing eight fields, including the original customer request and the two new metadata fields.

## Test Cases

- TC-006: Workflow execution succeeds.
- TC-007: Eight output fields are present.
- TC-008: Original order reference is preserved.
- TC-009: Metadata values are correct.
- TC-010: Node execution results can be inspected.

Record PASS or FAIL only after running each test.

## Business Relevance

Preserving data across nodes is essential when integrating commerce APIs, databases, AI classification, notifications, and approval workflows.

## Next Lesson

Lesson 03 — Triggers, Schedules, and Expressions.

Keep the actual workflow in your existing enterprise project directory. Export it to `workflows/` when you have finished the lesson and verified the workflow.

## 8. Lesson 02 completion checklist

Added Set Intake Metadata to the existing CAO-001 workflow.

Preserved all six original request fields.

Executed the workflow and verified all eight fields.

Ran and documented test cases TC-006 through TC-010.

Updated the Lesson 02 learning notes.

5 of 5 verified

Lesson 02 complete

Continue to Lesson 03

Next lesson: Lesson 03 — Triggers, Schedules, and Expressions. We will evolve CAO-001 from manually configured test data toward dynamic business inputs, preparing it for real webhook and API integrations.