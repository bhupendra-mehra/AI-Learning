Excellent — Lesson 07 is complete. Your `CAO-002 - Authenticated Integration Test` workflow successfully authenticated with the Bearer token, and you stored the credential in n8n instead of hardcoding it. You also kept `CAO-001` unchanged.

We’ll continue with the next lesson in the existing Version 2.3 roadmap, keeping all practical work inside your current project and leaving Magento untouched.

# Lesson 08 — Data Extraction, Validation, Cleaning, Transformation, and Routing

Goal: Turn incoming customer requests and external API responses into consistent, validated data that the commerce operations workflow can safely process.

## 1. Where this lesson fits

We will enhance your existing `CAO-001 - Customer Request Intake` workflow.

Webhook / Manual Trigger

Edit Fields → Set Intake Metadata

NEW: Normalize and Validate

Clean fields and check required data

IF — Request Valid?

True

Switch — Request Routing

False

Rejected Request

Keep your existing Switch outputs and commerce API branch. We are adding validation before the Switch so invalid requests do not reach business processing.

## 2. Add the normalization node

Open `CAO-001 - Customer Request Intake`.

1. Add an Edit Fields (Set) node after `Set Intake Metadata`.
2. Name it `Data - Normalize and Validate Request`.
3. Ensure Include Other Input Fields is enabled so the existing request fields are preserved.
4. Add the following fields. Select Expression for each value.

\| Field name | Expression |\
\|---|---|\
\| `normalized_customer_email` | `{{ ($json.customer_email || "").trim().toLowerCase() }}` |\
\| `normalized_request_type` | `{{ ($json.request_type || "").trim().toLowerCase() }}` |\
\| `normalized_order_reference` | `{{ ($json.order_reference || "").trim().toUpperCase() }}` |\
\| `is_valid_request` | See below |\
\| `validation_message` | See below |

For `is_valid_request`, use:

```
{{ 
  !!($json.customer_email || "").trim() &&
  !!($json.order_reference || "").trim() &&
  ["order_status", "return_request", "payment_issue"]
    .includes(($json.request_type || "").trim().toLowerCase())
}}
```

For `validation_message`, use:

```
{{
  !($json.customer_email || "").trim()
    ? "Missing customer email"
    : !($json.order_reference || "").trim()
      ? "Missing order reference"
      : !["order_status", "return_request", "payment_issue"]
          .includes(($json.request_type || "").trim().toLowerCase())
        ? "Unsupported request type"
        : "Validation passed"
}}
```

Why this matters: incoming data is not always consistent. An email might contain uppercase letters or accidental spaces, and request types may use inconsistent casing. Normalization creates consistent values before routing.

> These checks are a learning example, not complete production validation. They check that the email is non-empty, not that it is a valid email address or belongs to the customer. Production workflows also need schema validation, authorization and order-ownership checks.

## 3. Add the IF node

1. Add an IF node after `Data - Normalize and Validate Request`.
2. Name it `Validation - Is Request Valid?`.
3. Configure a Boolean condition:
   - Value 1: `{{ $json.is_valid_request }}`
   - Operation: `is true`
4. Connect the true output to your existing `Switch - Request Routing`.
5. Connect the false output to a new Edit Fields node named `Response - Reject Invalid Request`.

In the rejection node, enable Include Other Input Fields and add:

| Field               | Value                            |
| ------------------- | -------------------------------- |
| `processing_status` | `rejected`                       |
| `response_message`  | `{{ $json.validation_message }}` |

This gives invalid requests an explicit result rather than allowing them into order processing. The rejection node is an internal workflow result for now; it does not automatically send a response to the original webhook caller.

## 4. Update the Switch node

Because we now have a normalized request type, update the value used by the existing Switch rules.

Change the Value 1 expression in each rule to:

```
{{ $json.normalized_request_type }}
```

Keep the existing comparisons:

- `order_status` → Order Operations
- `return_request` → Returns Team
- `payment_issue` → Payments Team

Do not change the other branch connections.

## 5. Test the workflow

Run these tests using your Manual Trigger test data or the Webhook test URL. Execute the whole workflow, not only an individual node.

| Test   | Input change                          | Expected result                                            |
| ------ | ------------------------------------- | ---------------------------------------------------------- |
| TC-033 | Existing valid `order_status` request | Validation passes; Order Operations                        |
| TC-034 | `request_type = " RETURN_REQUEST "`   | Normalized to `return_request`; Returns Team               |
| TC-035 | `customer_email = ""`                 | Rejected: Missing customer email                           |
| TC-036 | `request_type = "unknown_type"`       | Rejected: Unsupported request type                         |
| TC-037 | Inspect output fields                 | Original fields and new normalized fields remain available |

For TC-034, temporarily change the request type in your test input to include spaces and uppercase letters. Restore your usual input after testing.

## 6. What success looks like

For a valid request, your normalized data should contain fields similar to:

```
{
  "normalized_customer_email": "customer@example.com",
  "normalized_request_type": "order_status",
  "normalized_order_reference": "ORD-100045",
  "is_valid_request": true,
  "validation_message": "Validation passed"
}
```

For an invalid request, `is_valid_request` should be `false`, and the IF node should route the data to `Response - Reject Invalid Request`.

## 7. Lesson 08 completion checklist

Added Data - Normalize and Validate Request

Preserved original input fields

Added IF validation and an invalid-request branch

Updated Switch rules to use normalized_request_type

Passed tests TC-033 through TC-037

Submit lesson results

Once these tests pass, Lesson 08 will be complete and we can move to Lesson 09 — LLM Integration, where the platform will begin using an AI model to interpret customer requests rather than relying only on predefined rules.