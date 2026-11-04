Lesson 12 — AI Workflows and Human Review is complete! All six checklist items passed, including the business rules that enforce human review for payment and return requests.

Your platform now distinguishes between requests that can proceed automatically and requests that require human intervention.

12 lessons completed

Roadmap Version 2.3 · Module 3 complete

# Lesson 13 — Error Handling, Retries, and Failure Recovery

Part 8 · Module 4 · Enterprise AI Commerce Operations Platform

Markdown filename: `lesson-13-error-handling-retries-and-failure-recovery.md`

Learning documentation location:

`AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-13-error-handling-retries-and-failure-recovery.md`

## 1. Lesson objective

So far, our workflows have worked when the inputs and APIs behaved correctly. Real production workflows must also handle failures.

Consider these situations:

| Scenario                           | Expected system behaviour               |
| ---------------------------------- | --------------------------------------- |
| Gemini API temporarily unavailable | Retry the request                       |
| API rate limit exceeded            | Wait and retry                          |
| Invalid AI response                | Stop automatic processing               |
| Missing customer email             | Reject the request                      |
| External commerce API unavailable  | Retry and record failure                |
| Repeated failure                   | Capture error details for investigation |

We'll implement these behaviours in n8n without changing your existing Magento environment.

## 2. Practical workflow architecture

We'll enhance the existing `CAO-003 - AI Classification and Extraction` workflow.

Input - Customer Message

Gemini AI Classification and Extraction

Structured Output Parser

Data - Prepare Extracted Request

Existing business decision and human-review routing

We will focus on three failure-handling capabilities:

1. Retry temporary API failures.
2. Handle permanent errors safely.
3. Record errors for investigation.

## 3. Configure retry behaviour for Gemini

Open your `Basic LLM Chain` node.

Depending on your n8n node version, the retry options may be under Settings.

Configure:

| Setting                 | Value   |
| ----------------------- | ------- |
| Retry On Fail           | Enabled |
| Max Tries               | `3`     |
| Wait Between Tries (ms) | `2000`  |

This means n8n can retry a failed execution up to three attempts, waiting two seconds between attempts.

Important

A retry does not guarantee success. Authentication errors, invalid credentials, unavailable models, and quota exhaustion may persist. We will distinguish temporary failures from permanent failures in our handling strategy.

## 4. Configure the Error Output behaviour

Open the same node's Settings.

Look for On Error.

For now, select:

`Continue (using error output)`

If your version exposes a separate error output, we can connect it to a dedicated failure-handling branch. If it does not, do not force a different setting; tell me what options you see.

The purpose is to keep a failed AI request from being mistaken for a successful classification.

## 5. Add a failure-handling branch

If the Basic LLM Chain exposes an error output:

1. Add an Edit Fields node.
2. Name it `Error - Capture AI Failure`.
3. Enable Include Other Input Fields.
4. Add the following fields:

\| Field | Expression |\
\|---|---|\
\| `processing_status` | `failed` |\
\| `error_stage` | `gemini_classification` |\
\| `error_message` | `{{ $json.error?.message || $json.message || "AI processing failed" }}` |\
\| `requires_human_review` | `true` |

Connect the error output to this node.

If the error output is not available, we'll use a dedicated n8n error workflow in the next step instead.

## 6. Create a dedicated error workflow

This is a useful production capability in n8n.

1. Create a new workflow.
2. Name it `CAO-004 - Centralized Error Handler`.
3. Add an Error Trigger node.
4. Add an Edit Fields node named `Error - Capture Execution Details`.
5. Enable Include Other Input Fields.
6. Execute a controlled test after configuring the error workflow.

The Error Trigger receives information about workflow execution failures when an associated workflow has been configured as the error workflow.

You need to configure `CAO-004 - Centralized Error Handler` as the error workflow for CAO-003 - AI Classification and Extraction.

You do not need to add CAO-004 as a normal node inside CAO-003. n8n executes it separately when the configured workflow encounters an unhandled error.

## 1. First, activate CAO-004

Open `CAO-004 - Centralized Error Handler`.

Check the following:

1. It contains an Error Trigger node.
2. The Error Trigger is the starting node.
3. Connect it to `Error - Capture Execution Details` (Edit Fields).
4. Save the workflow.
5. Activate or publish the workflow, depending on the controls shown in your n8n 2.45 interface.



Important

&#x20;The error workflow must be active before you can select it for another workflow.



## 2. Configure CAO-003

Now open:

`CAO-003 - AI Classification and Extraction`

Go to:

Workflow Settings → Error Workflow

Select:

`CAO-004 - Centralized Error Handler`

It should no longer be disabled once CAO-004 is active and saved.

## 3. What about CAO-001 and CAO-002?

For now, configure only CAO-003.

| Workflow                                   | Error handler           |
| ------------------------------------------ | ----------------------- |
| CAO-001 — Customer Request Intake          | Not configured yet      |
| CAO-002 — Authenticated Integration Test   | Not configured          |
| CAO-003 — AI Classification and Extraction | CAO-004                 |
| CAO-004 — Centralized Error Handler        | No error handler needed |

We can configure CAO-001 later when we integrate the AI workflow into the complete commerce platform.

## 4. Verify the configuration

After selecting CAO-004 in CAO-003:

- Save CAO-003.
- Confirm CAO-004 is active.
- Run a controlled failure test in a separate temporary workflow configured to use CAO-004.
- Verify that the Error Trigger receives the failed execution details.

One important distinction: The Error Trigger handles workflow execution failures; it does not automatically capture every unsuccessful business outcome. For example, a customer request rejected by validation is not necessarily an execution error.

Your next step: Activate `CAO-004` first. If it is still disabled in CAO-003's Error Workflow dropdown, tell me whether you see an Activate or Publish button in CAO-004.

For the initial test, add a temporary node with a deliberate failure in a separate test workflow. Do not deliberately break your working Gemini classification path.

## 7. Testing scenarios

| Test ID | Scenario                                           | Expected result                                         |
| ------- | -------------------------------------------------- | ------------------------------------------------------- |
| TC-055  | Normal Gemini execution                            | Successful classification                               |
| TC-056  | Temporary API/network failure                      | Retry attempted                                         |
| TC-057  | Invalid API credential in a separate test workflow | Error captured                                          |
| TC-058  | Failed execution with configured Error Workflow    | Error Trigger receives execution details                |
| TC-059  | Repeated failure                                   | Execution marked failed and available for investigation |

Do not repeatedly send invalid requests to Gemini. One controlled failure test is sufficient.

## 8. Lesson 13 completion checklist

Lesson progress

6/6

Configured retry behaviour for Gemini

Reviewed and configured the Basic LLM Chain error behaviour

Created CAO-004 - Centralized Error Handler

Configured the main workflow to use the error workflow

Tested a controlled failure and verified error details

Confirmed failed AI requests cannot enter successful business processing

Submit lesson results

Next lesson: Lesson 14 — Workflow Testing, Debugging, and Troubleshooting. We'll build a repeatable test approach for the platform, inspect execution data, and diagnose failures systematically.

Start with Step 3: Configure the Gemini retry settings and tell me which options you see under the Basic LLM Chain's Settings → On Error. We will adapt the remaining steps to your actual n8n 2.45 interface.