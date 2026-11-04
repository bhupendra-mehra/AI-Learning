# Lesson 16 — Monitoring, Performance, and Operational Alerts

Roadmap: Version 2.3 → Part 8: AI Automation with n8n\
Project: Enterprise AI Commerce Operations Platform\
n8n version: 2.45

Markdown filename: `lesson-16-monitoring-performance-and-operational-alerts.md`

Documentation location:

`/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-16-monitoring-performance-and-operational-alerts.md`

## 1. Learning objectives

In this lesson, we will learn to:

1. Monitor workflow executions and identify failures.
2. Measure execution duration and identify slow nodes.
3. Monitor Gemini API performance.
4. Configure execution data retention.
5. Prepare operational alerts for workflow failures.
6. Establish basic operational health metrics.

We will use your existing CAO workflows rather than create duplicate business workflows.

## 2. Understand the monitoring architecture

Our target monitoring architecture will look like this:

```
Enterprise AI Commerce Operations
                |
        CAO-001 / CAO-003
                |
        Workflow Executions
                |
        Execution Monitoring
                |
        Performance Analysis
                |
        Operational Alerts
                |
        Monitoring Dashboard
```

We will initially use n8n's built-in execution history. Later, we can extend the monitoring workflow with external notifications and reporting.

## 3. Exercise A — Inspect workflow execution history

Open n8n and select `CAO-003 - AI Classification and Extraction`.

1. Open the Executions section.
2. Review your recent executions.
3. Open a successful execution.
4. Open a failed execution if available.
5. Inspect the execution details and individual node execution times.

Record the following information for at least five executions:

| Metric       | What to record              |
| ------------ | --------------------------- |
| Execution ID | Unique execution identifier |
| Workflow     | CAO-003                     |
| Status       | Success or Error            |
| Start time   | Execution start             |
| Duration     | Total execution time        |
| Failed node  | Node name, if applicable    |

Do not deliberately generate repeated Gemini failures just to collect data. Use existing execution history where possible.

## 4. Exercise B — Measure workflow performance

For each of the five executions, inspect these nodes:

- `Input - Customer Message`
- `Security - Prepare Safe AI Input`
- `Basic LLM Chain`
- `Data - Prepare Extracted Request`
- `Decision - Human Review Required?`

Pay particular attention to:

Basic LLM Chain

This is likely to be one of the most time-consuming operations because it involves an external AI API request.

Record its execution duration separately from the other nodes.

Create a small performance register in your project:

`enterprise-ai-commerce-ops/test-data/performance-baseline.md`

Use this table:

| Execution   | Total duration      | Gemini duration     | Status        |
| ----------- | ------------------- | ------------------- | ------------- |
| Execution 1 | Record actual value | Record actual value | Success/Error |
| Execution 2 | Record actual value | Record actual value | Success/Error |
| Execution 3 | Record actual value | Record actual value | Success/Error |
| Execution 4 | Record actual value | Record actual value | Success/Error |
| Execution 5 | Record actual value | Record actual value | Success/Error |

Use the actual durations displayed by n8n. Do not estimate missing values.

## 5. Exercise C — Configure execution data retention

Open the CAO-003 workflow.

1. Open Workflow Settings.
2. Inspect the execution-saving options.
3. Locate the settings for successful, failed and manual executions.
4. Review which execution data is currently saved.
5. Check whether execution data pruning is configured at the n8n instance level.

For this learning environment:

- Keep failed execution data available for debugging.
- Keep enough successful execution history for performance analysis.
- Avoid retaining unnecessary customer information.
- Do not disable all execution saving.

Important: Workflow-level execution-saving settings and instance-level pruning are different. Do not change global Docker environment variables or delete your `n8n_data` volume during this exercise.

## 6. Exercise D — Prepare operational alert records

We will reuse your existing `CAO-004 - Centralized Error Handler` workflow.

Remember that its invocation from CAO-003 is still under investigation from Lesson 13. We will not assume that issue has been fixed.

Open CAO-004 and locate:

`Error - Capture Execution Details`

Add the following fields if they are not already present:

\| Field | Expression |\
\|---|---|\
\| alert_type | `workflow_failure` |\
\| alert_severity | `high` |\
\| failed_workflow | `{{ $json.workflow?.name || "Unknown workflow" }}` |\
\| execution_id | `{{ $json.execution?.id || "Unknown execution" }}` |\
\| error_message | `{{ $json.execution?.error?.message || $json.error?.message || "Unknown error" }}` |\
\| execution_url | `{{ $json.execution?.url || "" }}` |\
\| alert_timestamp | `{{ $now.toISO() }}` |\
\| alert_status | `new` |

Enable Include Other Input Fields if you need to preserve the original error information.

Your alert record should contain enough information to identify:

- Which workflow failed.
- Which execution failed.
- What error occurred.
- When the failure happened.
- Where the execution can be inspected.

Do not include API keys, Bearer tokens, customer passwords or other secrets in alert messages.

## 7. Exercise E — Verify the operational alert payload

Use your already-tested `CAO-005 - Error Handler Verification` workflow to generate a controlled failure.

Check whether CAO-004 receives the error and produces the expected alert fields.

Expected structure:

```
{
  "alert_type": "workflow_failure",
  "alert_severity": "high",
  "failed_workflow": "CAO-005 - Error Handler Verification",
  "execution_id": "actual_execution_id",
  "error_message": "actual_error_message",
  "execution_url": "actual_execution_url",
  "alert_timestamp": "actual_timestamp",
  "alert_status": "new"
}
```

The values above are illustrative except for the field names. Verify the actual values in your execution.

If CAO-005 still invokes CAO-004 successfully, this confirms the alert payload works independently of the unresolved CAO-003 error-handler integration.

We will add an actual notification destination after confirming the payload. There is no need to configure an external email or messaging service yet.

## 8. Operational metrics

Our platform should eventually track these metrics:

| Metric                     | Purpose                   |
| -------------------------- | ------------------------- |
| Total executions           | Overall workflow activity |
| Successful executions      | Successful processing     |
| Failed executions          | Workflow reliability      |
| Average execution duration | Performance               |
| Gemini API duration        | AI response performance   |
| Human-review count         | Manual workload           |
| Validation failures        | AI output quality         |
| Alert count                | Operational incidents     |

For this lesson, focus on collecting actual execution data and understanding where the bottlenecks occur.

## 9. Completion checklist

Lesson 16 progress

# 8/8

Inspected CAO-003 execution history

Recorded at least five execution results

Identified the slowest workflow node

Created performance-baseline.md

Reviewed execution-saving and retention settings

Updated the CAO-004 operational alert payload

Verified alert payload using CAO-005

Recorded actual monitoring results

## Start with Exercise A

First, inspect the CAO-003 execution history and record five executions.

One question: Can you see execution duration and individual node execution times when you open a completed CAO-003 execution in your n8n 2.45 interface?

We will proceed based on what your interface actually displays.

Yes. Your n8n 2.45 interface displays exactly the information we need for Lesson 16.

From your screenshot, I can confirm:

- Overall execution duration is displayed at the top.
- Individual node execution results are available in the Logs panel.
- You can inspect each node's Input and Output.
- Token usage is displayed: 1,278 tokens for the selected execution.
- The selected execution succeeded in 4.206 seconds.

One important observation: your selected execution is a successful return-request classification, and the workflow correctly routed it to `Review - Pending Human Approval`.

## 1. Record your first five executions

Based on the execution history visible in your screenshot, we can already record these five actual durations.

| Execution time | Total duration | Status  |
| -------------- | -------------- | ------- |
| 22:47:45       | 4.206 sec      | Success |
| 20:25:11       | 4.522 sec      | Success |
| 20:21:44       | 4.296 sec      | Success |
| 20:18:39       | 12.339 sec     | Success |
| 20:18:04       | 4.301 sec      | Success |

Initial performance baseline

# 5.93 sec

Average execution duration across these five executions

Fastest execution

4.206 sec

Slowest execution

12.339 sec

Successful executions

5 / 5

The 12.339-second execution is worth investigating. It may have experienced a slower Gemini response, but we need its individual node timing to confirm.

## 2. Inspect Gemini execution duration

For the selected execution:

1. Click `Basic LLM Chain` in the Logs panel.
2. Inspect its execution details.
3. Check whether n8n displays the duration for this node or its nested Gemini operation.
4. Repeat for the execution that took 12.339 seconds.

Record the Gemini duration separately if available. Do not assume the entire Basic LLM Chain duration is exclusively Gemini API processing.

## 3. Create the performance baseline file

Location:

`enterprise-ai-commerce-ops/test-data/performance-baseline.md`

Record the five execution durations above. Leave Gemini duration blank until you inspect the node details.

## 4. Next exercise — Execution retention

I can also see a dropdown at the bottom-left of your screenshot:

Which executions is this workflow saving?

Click that dropdown and share what options are displayed.

We will use the settings actually available in your n8n 2.45 interface rather than assuming the configuration options.