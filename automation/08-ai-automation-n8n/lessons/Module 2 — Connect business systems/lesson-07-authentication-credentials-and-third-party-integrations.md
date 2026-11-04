Great! Lesson 06 — REST APIs, HTTP Requests, JSON, and Expressions is now working. Your new Edit Fields node successfully evaluates `{{ $json.total }}` and returns the correct response data.

This confirms that your n8n workflow can call an external API, read its JSON response, and extract values for downstream processing. The community-edition registration certificate issue is separate and does not need to block our learning.

# Lesson 07 — Authentication, Credentials, and Third-Party Integrations

[Generate and Send PDF Invoice with n8n - HTML2PDF.app](https://images.openai.com/static-rsc-4/S7jIIa-sM6EPgeyCwlGOX8prRZ3xOnzekMo1TrXfMVZ8bgMTuq9Ih20CwrgPPw_NZYyRG8QcbnPJSLkn6pzL_fb2Pq8fIPcvZ0E_6vB-0X6MBm2xap9gGbi1b4vOjuVq-OTqMM4Vd5TmJKSO3s_fWP8_YwPH2w27wD0B_pMis6A?purpose=inline)

Part 8: AI Automation with n8n

Next lesson

Goal: Learn to connect external services securely using API credentials, authentication methods, and reusable integrations in our existing Enterprise AI Commerce Operations Platform.

## 1. What you will learn

- The difference between API keys, Bearer tokens, Basic Auth, and OAuth2.
- How to configure credentials in n8n instead of hardcoding secrets.
- How to authenticate an HTTP Request node.
- How to inspect authentication errors such as `401 Unauthorized` and `403 Forbidden`.
- How to keep API secrets out of workflow exports, logs, and project files.

## 2. Where this fits into our project

Our existing workflow, `CAO-001 - Customer Request Intake`, already accepts customer requests and routes them based on request type. The Order Operations branch calls a mock commerce API.

We will now add a safe, simulated authenticated integration so you can learn the credential workflow without connecting to a real store, using real customer data, or changing your Magento environment.

## 3. Practical exercise: Create a reusable API credential

We will use `httpbin.org`, a public testing service, to verify that n8n sends a Bearer token correctly. This is a test credential, not a real commerce API key.

### Step 1 — Create a separate test workflow

Keep `CAO-001` unchanged while we test authentication.

1. In n8n, create a new workflow.
2. Name it `CAO-002 - Authenticated Integration Test`.
3. Add a Manual Trigger node.
4. Add an HTTP Request node and rename it `API - Test Bearer Authentication`.

### Step 2 — Configure the HTTP Request

Set the following values:

| Setting           | Value                        |
| ----------------- | ---------------------------- |
| Method            | `GET`                        |
| URL               | `https://httpbin.org/bearer` |
| Authentication    | `Generic Credential Type`    |
| Generic Auth Type | `Header Auth`                |

After selecting Header Auth, you should see an option to create a new credential.

### Step 3 — Create the credential

Create a credential with these values:

| Credential field | Value                            |
| ---------------- | -------------------------------- |
| Credential name  | `CAO Test Bearer Token`          |
| Name             | `Authorization`                  |
| Value            | `Bearer cao-learning-test-token` |

Save the credential and select it in the HTTP Request node.

Security rule

The token above is only for this public test endpoint. Never use real customer credentials, production API keys, or Magento secrets in this exercise. Store credentials in n8n's credential manager rather than directly in workflow fields.

### Step 4 — Execute the workflow

Connect the nodes:

Manual Trigger

API - Test Bearer Authentication

Execute the workflow and inspect the HTTP Request node's output. A successful response should resemble:

```
{
  "authenticated": true,
  "token": "cao-learning-test-token"
}
```

The endpoint echoes the test token to confirm that authentication was sent; it does not validate a real user account.

If you receive an authentication error, check the credential type, the `Authorization` header name, and the `Bearer ` prefix. If you get a network or certificate error, report the exact error rather than disabling TLS verification.

## 4. Lesson 07 completion checklist

Your progress

5 of 5

Created CAO-002 without modifying CAO-001

Configured Header Auth in the HTTP Request node

Saved and selected the reusable n8n credential

Executed the workflow and received authenticated: true

Confirmed that no real secrets were hardcoded in the workflow

Submit progress

Your next action: Complete Steps 1–4 and tell me whether you received `authenticated: true`. We will then handle the next lesson based on your actual result.