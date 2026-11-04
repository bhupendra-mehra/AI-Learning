Lesson 11 — AI Classification and Information Extraction is complete! All six checklist items passed, including structured extraction, downstream field preparation, and test cases TC-045 through TC-049.

Your Enterprise AI Commerce Operations Platform can now interpret customer messages, classify requests, extract order information, and prepare structured data for subsequent automation.

Roadmap progress: 11 of 30 lessons completed.

# Lesson 12 — AI Workflows and Human Review

Part 8 · Module 3 · Roadmap Version 2.3

Markdown filename: `lesson-12-ai-workflows-and-human-review.md`

Learning documentation location:

`AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-12-ai-workflows-and-human-review.md`

## 1. Lesson objective

In the previous lessons, Gemini classified and extracted information from customer messages.

Now we will introduce business decision-making around the AI results.

Not every customer request should be processed automatically.

For example:

| Customer request                | Workflow decision                 |
| ------------------------------- | --------------------------------- |
| Where is my order?              | Automatic processing can continue |
| I want to return my product     | Human review or policy validation |
| I was charged twice             | Human review                      |
| I want an immediate refund      | Mandatory human approval          |
| What are your delivery options? | Automatic response can continue   |

Important principle: AI can recommend an action, but business rules and authorization controls must decide whether sensitive operations are permitted.

## 2. Workflow architecture

We'll extend your existing `CAO-003 - AI Classification and Extraction` workflow.

Input - Customer Message

Basic LLM Chain + Gemini + Structured Output Parser

Data - Prepare Extracted Request

IF — Human Review Required?

True

Pending Human Review

False

Automatic Processing

## 3. Add business rules before human review

Open `Data - Prepare Extracted Request`.

Add two new fields in Expression mode.

Field: `business_review_required`

```
{{
  $json.output.requires_human_review === true ||
  $json.output.category === "payment_issue" ||
  $json.output.category === "return_request"
}}
```

Field: `processing_decision`

```
{{
  (
    $json.output.requires_human_review === true ||
    ["payment_issue", "return_request"].includes($json.output.category)
  )
    ? "human_review"
    : "automatic_processing"
}}
```

These are conservative learning rules: all return and payment requests go to human review. We can refine them later based on company policy and verified order data.

## 4. Add the IF node

Add an IF node after `Data - Prepare Extracted Request`.

Name it:

`Decision - Human Review Required?`

Configure:

| Setting   | Value                                  |
| --------- | -------------------------------------- |
| Value 1   | `{{ $json.business_review_required }}` |
| Condition | `is true`                              |

Connect the outputs:

- True → `Review - Pending Human Approval`
- False → `Processing - Automatic Request`

For each output, add an Edit Fields node.

### True branch — Pending Human Approval

Add these fields:

| Field               | Value                       |
| ------------------- | --------------------------- |
| `processing_status` | `pending_human_review`      |
| `review_reason`     | `{{ $json.output.reason }}` |
| `approval_required` | `true`                      |

Enable Include Other Input Fields.

### False branch — Automatic Processing

Add:

| Field               | Value                            |
| ------------------- | -------------------------------- |
| `processing_status` | `ready_for_automatic_processing` |
| `approval_required` | `false`                          |

Enable Include Other Input Fields.

For now, the automatic branch only marks a request as ready. It must not initiate refunds, cancellations, or other sensitive operations.

## 5. Test the workflow

Run the following scenarios:

| Test ID | Customer message                    | Expected outcome     |
| ------- | ----------------------------------- | -------------------- |
| TC-050  | Where is order ORD-100350?          | Automatic processing |
| TC-051  | I want to return my damaged laptop. | Human review         |
| TC-052  | My payment was deducted twice.      | Human review         |
| TC-053  | I need an immediate refund.         | Human review         |
| TC-054  | What are your store opening hours?  | Automatic processing |

Check both the AI output and the final business decision.

Even if Gemini returns `requires_human_review: false` for a payment or return request, the business rules must still route it to human review.

## 6. Lesson 12 completion checklist

Lesson progress

6/6

Added business_review_required and processing_decision fields

Added the IF node for human-review routing

Configured the pending human-review branch

Configured the automatic-processing branch

Verified payment and return requests always require review

Passed test cases TC-050 through TC-054

Submit lesson results

Next lesson: Lesson 13 — Error Handling, Retries, and Failure Recovery. We'll make the workflows resilient to API failures, model errors, invalid responses, and temporary service interruptions.