# Part 8 — Lesson 03: Triggers, Schedules, and Expressions

Lesson 03 of 30

Module 1 — Foundations

Project: Enterprise AI Commerce Operations Platform\
Existing workflow: `CAO-001 - Customer Request Intake`

We will continue with the same workflow. As requested, the lesson content here is your learning documentation—there is no separate Markdown file to copy.

## 1. What we are building

Currently, CAO-001 uses manually configured values. A real business automation system must accept changing customer requests rather than processing only one hard-coded example.

In this lesson, we will learn three concepts:

- Triggers: determine when a workflow starts.
- Schedules: start workflows at a recurring time or interval.
- Expressions: dynamically read and transform data instead of relying on fixed values.

Our immediate goal is to prepare the existing workflow to handle changing request data. We will introduce a real webhook as the next step in the roadmap, without breaking the working version.

## 2. Understand the three concepts

Trigger

Starts a workflow when a defined event occurs. Examples include a manual run, an incoming webhook, or a new email.

Schedule

Runs a workflow at a defined interval. For example, an operations workflow could periodically check for orders requiring attention.

Expression

Computes a value from incoming data. For example, a customer's email address can be read from the incoming request instead of being typed into the node configuration.

The distinction matters in enterprise automation: triggers determine when processing begins, schedules determine when recurring processing occurs, and expressions determine how values are derived during processing.

## 3. Practical exercise — Make CAO-001 dynamic

We will add two calculated fields to your existing `Set Intake Metadata` node.

The workflow will become:

Manual Trigger

Starts a test execution

Edit Fields

Creates the sample customer request

Set Intake Metadata

Preserves fields and adds dynamic values

Dynamic request metadata

Values calculated from incoming fields

### Step 3.1 — Add `routing_key`

Open `Set Intake Metadata`, keeping your existing fields and enabling Include Other Input Fields.

Add a new String field:

- Name: `routing_key`
- Value mode: Expression
- Expression:

```
{{ $json.request_type }}
```

In n8n, `$json` refers to the current input item's JSON data. The expression reads the request type from the preceding node.

For our sample request, the result should be:

```
{
  "routing_key": "order_status"
}
```

If the request type changes to `return_request`, the routing key changes automatically. Later, we will use this value to direct requests to the correct business workflow.

### Step 3.2 — Add `request_summary`

Add another String field:

- Name: `request_summary`
- Value mode: Expression
- Expression:

```
{{ "Order " + $json.order_reference + ": " + $json.message }}
```

Expected result:

```
Order ORD-100045: Please provide an update on my order.
```

This combines existing fields into a useful summary without writing a custom Python or JavaScript program.

Important: Enter the expressions in n8n's Expression mode, not as ordinary fixed text. Keep the original six fields, `processing_status`, and `workflow_version`.

## 4. Understand schedules without disrupting the workflow

A schedule is useful when a business process must run periodically rather than in response to an individual request.

For example, our commerce operations platform could eventually run a separate scheduled workflow to:

- Identify orders that have remained unfulfilled too long.
- Check for unresolved support cases.
- Generate a daily operations summary.
- Alert the team about failed automation executions.

We should not replace the Manual Trigger in CAO-001 with a Schedule Trigger. Customer intake is an event-driven process, while periodic order reviews are a separate business process. We can add that second workflow when the platform reaches the appropriate stage.

## 5. Test the dynamic expressions

Run these tests in your existing n8n workflow.

| Test   | Input change                            | Expected result                                 |
| ------ | --------------------------------------- | ----------------------------------------------- |
| TC-011 | Execute with the original request       | `routing_key` is `order_status`                 |
| TC-012 | Change request type to `return_request` | `routing_key` updates to `return_request`       |
| TC-013 | Change order reference to `ORD-100046`  | `request_summary` contains `ORD-100046`         |
| TC-014 | Change the message                      | `request_summary` reflects the new message      |
| TC-015 | Inspect the final node output           | All original fields and metadata remain present |

For each test, change the sample values in the original Edit Fields node, execute the workflow, and inspect the output of `Set Intake Metadata`. Restore the original sample values after testing.

### Troubleshooting

- Expression appears as literal text: switch the field to Expression mode.
- Value is undefined: check the spelling of the referenced field and inspect the preceding node's output.
- Original fields disappear: verify that Include Other Input Fields is enabled.
- Summary contains missing values: confirm that both `order_reference` and `message` are present in the incoming item.

## 6. Lesson 03 completion checklist

Added routing_key using an expression.

Added request_summary using an expression.

Verified that values change when input data changes.

Ran and recorded test cases TC-011 through TC-015.

4 of 4 verified

Lesson 03 complete

Continue to Lesson 04

Next lesson: Lesson 04 — Conditions, Branching, Loops, and Business Routing. We will use the request type and metadata we have just created to introduce real business routing rules.