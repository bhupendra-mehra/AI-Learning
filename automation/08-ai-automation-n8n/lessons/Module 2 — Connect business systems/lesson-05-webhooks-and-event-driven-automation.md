# Part 8 — Lesson 05: Webhooks and Event-Driven Automation

Lesson 05 of 30

Module 2 — APIs and Business Data

Project: Enterprise AI Commerce Operations Platform\
Existing workflow: `CAO-001 - Customer Request Intake`

Your first four lessons established the request structure, metadata, expressions, and business routing. Now we will move beyond manually entered test data and let another application submit customer requests to n8n.

## 1. What we are building

A real e-commerce platform needs to initiate automation when something happens—for example, a customer submits a request, an order changes status, or a support system sends an event.

A webhook provides an HTTP endpoint that an external application can call to trigger a workflow.

Customer or commerce application

Submits an order-related request

n8n Webhook Trigger

Receives the HTTP request

CAO-001 processing

Request fields → metadata → business routing

By the end of this lesson, you will be able to submit a JSON request to a local webhook and observe it enter your existing workflow.

### Important design decision

We will preserve the existing Manual Trigger workflow while building and testing the webhook version. Do not delete or replace the working workflow until the webhook has passed its tests.

For a clean implementation, create a second workflow named `CAO-001A - Webhook Intake Adapter`. It will receive HTTP requests and connect them to the same business-processing design. This keeps the intake mechanism separate from business routing, which is a maintainable enterprise architecture.

## 2. Understand the Webhook node

The n8n Webhook node exposes an HTTP endpoint that receives incoming requests and starts a workflow.

There are two URL types:

- Test URL: used during development. You activate the test listener before sending a request.
- Production URL: used after the workflow is activated. It is intended for integrations that need a persistent endpoint.

For this lesson, we will use the Test URL. We will not expose the endpoint publicly or connect a live Magento store.

## 3. Add webhook intake to CAO-001

Open `CAO-001 - Customer Request Intake` in n8n.

### Step 3.1 — Add the Webhook Trigger

1. Add a Webhook node to the existing workflow.
2. Rename it `Webhook - Customer Request Intake`.
3. Configure:
   - HTTP Method: `POST`
   - Path: `cao-001/customer-request`
   - Authentication: `None` for this localhost-only learning exercise
   - Respond: `Immediately`, or the equivalent immediate-response option in your n8n version.
4. Connect the Webhook node to the existing `Edit Fields` node.

Keep the Manual Trigger connected as well. Both triggers can start the same downstream workflow, but we must update the Edit Fields configuration so that it accepts either manually supplied defaults or incoming webhook data.

Security note: Do not use an unauthenticated webhook for a public or production deployment. We will cover authentication and access controls in later lessons.

### Step 3.2 — Update Edit Fields to accept dynamic input

Your current Edit Fields node contains fixed values. Those values would overwrite incoming customer data unless we change them.

For each of the six fields, switch the value to Expression and use the following expressions.

\| Field | Expression |\
\|---|---|\
\| `request_id` | `{{ $json.body?.request_id || $json.request_id || 'REQ-2026-0001' }}` |\
\| `request_type` | `{{ $json.body?.request_type || $json.request_type || 'order_status' }}` |\
\| `customer_email` | `{{ $json.body?.customer_email || $json.customer_email || 'customer@example.com' }}` |\
\| `order_reference` | `{{ $json.body?.order_reference || $json.order_reference || 'ORD-100045' }}` |\
\| `channel` | `{{ $json.body?.channel || $json.channel || 'web_form' }}` |\
\| `message` | `{{ $json.body?.message || $json.message || 'Please provide an update on my order.' }}` |

These expressions support three situations:

1. An incoming Webhook request, where fields are commonly available under `$json.body`.
2. Input fields already at the top level of the incoming item.
3. The existing sample values when running the Manual Trigger.

The fallback values are for learning and testing only. We will replace this permissive approach with strict validation in subsequent lessons so missing required data cannot silently become a sample request.

Keep `Set Intake Metadata` and `Switch - Request Routing` connected after Edit Fields. Your routing rules should continue to read the normalized `request_type` field.

## 4. Send a test request to the webhook

Now we will simulate a commerce application submitting a customer request.

### Step 4.1 — Start the webhook listener

1. Click the Webhook node.
2. Click Listen for test event or the equivalent option.
3. Copy the Test URL displayed by n8n.

The URL will usually resemble:

```
http://localhost:5678/webhook-test/cao-001/customer-request
```

Use the exact URL shown by your n8n instance.

### Step 4.2 — Submit a JSON request

Open a separate terminal and run the following command, replacing the URL with the one you copied.

```
curl -X POST "http://localhost:5678/webhook-test/cao-001/customer-request" \
  -H "Content-Type: application/json" \
  -d '{
    "request_id": "REQ-2026-0002",
    "request_type": "return_request",
    "customer_email": "customer@example.com",
    "order_reference": "ORD-100078",
    "channel": "web_form",
    "message": "I would like to return my recent order."
  }'
```

If you run this from a different machine or a remote environment, `localhost` refers to that machine, so use the appropriate reachable endpoint instead.

### Step 4.3 — Verify the result in n8n

After submitting the request:

1. Open the captured webhook execution.
2. Select the Webhook node and inspect its input.
3. Select Edit Fields and verify the normalized request fields.
4. Select `Set Intake Metadata` and verify that metadata is preserved.
5. Select `Switch - Request Routing` and inspect the Returns Team output.

Expected values:

### Webhook verification

Expected result

`request_id`

REQ-2026-0002

`request_type`

return_request

`order_reference`

ORD-100078

`processing_status`

received

`routing_key`

return_request

The Switch node should send the item to Returns Team, not Order Operations. The webhook's HTTP response only confirms receipt according to the configured response mode; it does not by itself prove that every downstream business action succeeded.

## 5. Troubleshooting

| Problem                                              | What to check                                                                                      |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `404 Not Found`                                      | Copy the current Test URL and ensure the listener is active.                                       |
| `ECONNREFUSED`                                       | Confirm the n8n container is running and port 5678 is accessible from the terminal.                |
| Webhook receives data but Edit Fields shows defaults | Inspect the Webhook output and confirm the JSON fields are under `body`.                           |
| Switch selects the wrong route                       | Check the normalized `request_type` value and Switch expressions.                                  |
| Webhook responds but no execution appears            | Check that you are inspecting the correct test execution and URL.                                  |
| Test URL stops working                               | Start the webhook test listener again; test endpoints are not intended for permanent integrations. |

## 6. Lesson 05 test cases

Run these tests and record the actual results in your project test documentation.

| Test ID | Scenario                            | Expected result                                    |
| ------- | ----------------------------------- | -------------------------------------------------- |
| TC-021  | Submit a valid order-status request | Request reaches Order Operations                   |
| TC-022  | Submit a return request             | Request reaches Returns Team                       |
| TC-023  | Submit a payment issue              | Request reaches Payments Team                      |
| TC-024  | Verify webhook input                | Submitted JSON is visible                          |
| TC-025  | Verify normalized output            | Submitted values are preserved                     |
| TC-026  | Send an invalid request type        | Request reaches the exception route, if configured |

For TC-026, remember that the fallback expressions in this lesson are not strict validation. An empty field may be replaced by a sample value. We will address this explicitly when we build the validation and exception-handling stages.

## 7. Lesson 05 completion checklist

Added the Webhook Trigger to CAO-001 and retained the Manual Trigger.

Updated Edit Fields to accept incoming webhook data.

Submitted a JSON request and inspected the webhook execution.

Verified the normalized data and correct Switch route.

Ran the relevant test cases and documented actual results.

5 of 5 verified

Lesson 05 complete

Continue to Lesson 06

Next lesson — Lesson 06: REST APIs, HTTP Request, JSON, and Expressions.

We will extend the same platform to retrieve business information from an API, understand request and response structures, and prepare CAO-001 for real commerce-system integrations.