Lesson 14 completed

Your Lesson 14 checklist is fully complete. We can mark Workflow Testing, Debugging, and Troubleshooting as completed in Roadmap Version 2.3.

The next lesson is Lesson 15. We will continue using your existing n8n environment and the Enterprise AI Commerce Operations Platform project. The Lesson 13 error-handler investigation remains deferred; we won't block the roadmap on it.

# Lesson 15 — Security, Credentials, and Data Protection

Roadmap: Version 2.3 → Part 8: AI Automation with n8n\
Project: Enterprise AI Commerce Operations Platform\
Workflow: CAO-003 — AI Classification and Extraction

Markdown filename: `lesson-15-security-credentials-and-data-protection.md`

Documentation location:\
`/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-15-security-credentials-and-data-protection.md`

## 1. Learning objectives

By the end of this lesson, you will be able to:

- Store API keys and tokens securely using n8n credentials.
- Avoid exposing credentials in workflow data and execution logs.
- Minimize customer information sent to AI services.
- Protect webhook endpoints.
- Identify sensitive actions that require human approval.

## 2. Practical exercise A — Review existing credentials

Open n8n:

`http://localhost:5678`

1. Open Credentials.
2. Locate your Gemini credential.
3. Open it and verify that the API key is stored in the credential configuration.
4. Do not copy the API key into any workflow field, prompt, or Edit Fields node.
5. Check CAO-002 and confirm the Bearer token is stored in its Header Auth credential.

Expected result: Both integrations use n8n credentials rather than hardcoded secrets.

## 3. Practical exercise B — Protect customer data before AI processing

In CAO-003, locate `Input - Customer Message` and the connection to `Basic LLM Chain`.

Add an Edit Fields node between the input and Basic LLM Chain.

Rename it:

`Security - Prepare Safe AI Input`

Enable Include Other Input Fields if you want to preserve the original request for downstream processing.

Add these fields:

\| Field | Expression |\
\|---|---|\
\| ai_customer_message | `{{ $json.customer_message || "" }}` |\
\| ai_customer_email | `{{ $json.customer_email ? "[REDACTED]" : "" }}` |\
\| ai_order_reference | `{{ $json.order_reference ? "[REDACTED]" : "" }}` |

For this exercise, update the Basic LLM Chain prompt to use only:

```
{{ $json.ai_customer_message }}
```

Do not include customer email, phone number, payment details, or authentication tokens in the AI prompt unless there is a clear business requirement.

Important: This is a demonstration of data minimization, not a complete anonymization system. The customer message itself could contain personal information. Review what is sent to Gemini before using real customer data.

## 4. Practical exercise C — Secure the customer webhook

Open CAO-001 and inspect its Webhook node.

1. Check the available Authentication options.
2. If Header Auth is available, configure a credential for the webhook.
3. Use a dedicated test token stored as an n8n credential.
4. Test the webhook with a request that includes the correct authentication header.
5. Test again without the header.

Expected result:

- Valid authentication: request reaches the workflow.
- Missing or invalid authentication: request is rejected.

Use a dummy token for this learning exercise. Do not use a production secret.

## 5. Practical exercise D — Review sensitive actions

Review the current business routing and approval rules.

Confirm these rules remain in place:

| Request category   | Processing policy                 |
| ------------------ | --------------------------------- |
| Order status       | Eligible for automatic processing |
| Return request     | Human review                      |
| Payment issue      | Human review                      |
| Refund approval    | Human approval required           |
| Order cancellation | Human approval required           |

AI classification must never independently approve refunds, authorize payments, or bypass business approval rules.

## 6. Security test cases

Add these test cases to your existing `test-data/workflow-test-cases.md`.

| ID     | Test                                      | Expected result               |
| ------ | ----------------------------------------- | ----------------------------- |
| TC-070 | Gemini credential is used                 | No hardcoded API key          |
| TC-071 | Bearer token integration                  | Token stored in credential    |
| TC-072 | Customer email sent to AI                 | Email redacted                |
| TC-073 | Customer order reference sent to AI       | Reference redacted            |
| TC-074 | Webhook request without authentication    | Rejected                      |
| TC-075 | Webhook request with valid authentication | Accepted                      |
| TC-076 | AI suggests automatic refund approval     | Human approval still required |

## 7. Completion checklist

Lesson 15 progress

# 6/6

Verified Gemini and Bearer token credentials

Added Security - Prepare Safe AI Input to CAO-003

Updated the AI prompt to use the safe input field

Configured and tested webhook authentication

Verified sensitive actions still require human approval

Recorded actual results for TC-070 through TC-076

Do not mark Lesson 15 complete until you have tested the relevant changes. If a setting is unavailable in your n8n 2.45 interface, share a screenshot and we'll adapt the steps rather than assume the option exists.

After you finish, send the actual results for TC-070 through TC-076.