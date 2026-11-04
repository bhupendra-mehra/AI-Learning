# Lesson 09 — LLM Integration for Customer Operations

Part 8: AI Automation with n8n · Roadmap Version 2.3 · Module 3

Markdown filename: `lesson-09-llm-integration.md`

Learning documentation location:\
`AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-09-llm-integration.md`

I’ll include the Markdown filename and documentation location in every lesson going forward, using lowercase kebab-case and zero-padded lesson numbers.

## 1. Lesson objective

Until now, your `CAO-001 - Customer Request Intake` workflow has used predefined rules to route requests. In this lesson, we’ll introduce a Large Language Model (LLM) so the platform can interpret a customer's message and classify the request.

For example, the customer might write:

> “My parcel hasn't arrived yet, and I need to know when it will be delivered.”

An AI model should identify this as an order-status enquiry, even though the customer never used the exact phrase `order_status`.

By the end of this lesson, you will have a working LLM integration in n8n using a test workflow, with structured output that we can later integrate into the enterprise commerce platform.

## 2. Architecture for this lesson

We'll create a separate workflow called `CAO-003 - AI Request Classification Test`. This lets us test the AI safely without disrupting your existing `CAO-001` workflow or `CAO-002` authentication test.

Manual Trigger

Start a test

Edit Fields — Customer Message

Provide sample customer text

LLM — Classify Request

Interpret the message using an AI model

Inspect Structured Result

Review classification and reasoning

## 3. Prepare the test workflow

In n8n:

1. Create a new workflow named `CAO-003 - AI Request Classification Test`.
2. Add a Manual Trigger node.
3. Add an Edit Fields (Set) node named `Input - Customer Message`.
4. Enable the option to include other input fields if needed.
5. Add these fields:

| Field                | Test value                                                                 |
| -------------------- | -------------------------------------------------------------------------- |
| `request_id`         | `REQ-2026-0009`                                                            |
| `customer_message`   | `My parcel hasn't arrived yet. Can you tell me when it will be delivered?` |
| `allowed_categories` | `order_status, return_request, payment_issue, other`                       |

Execute the first two nodes and verify that the input data appears correctly.

## 4. Choose the LLM provider

To connect an actual language model, n8n needs credentials for the provider you choose. Do not paste your API key into this chat. You will enter it directly into n8n's credential manager.

Your screenshot shows the correct AI node combination for n8n 2.45. The additional nodes are normal: n8n uses a Basic LLM Chain to manage the prompt and a separate Google Gemini Chat Model node to provide the actual AI model.

There is just one important connection to fix before configuring them.

## 1. Correct the workflow connections

For this lesson, we are testing with a Manual Trigger, so we don't need the Chat Trigger.

Use this structure

When clicking 'Execute workflow'

Input - Customer Message

Basic LLM Chain

Model connection

Google Gemini Chat Model

Make these changes:

1. Connect the output of `Input - Customer Message` directly to the main input of `Basic LLM Chain`.
2. Keep `Google Gemini Chat Model` connected to the diamond-shaped Model input of Basic LLM Chain. Your screenshot already shows this connection.
3. Delete the unused `When chat message received` node, or leave it disconnected.

The Chat Trigger is useful when you want users to interact through a chat interface. We can learn that separately later.

## 2. Configure Google Gemini Chat Model

Click the Google Gemini Chat Model node.

Configure:

| Setting                  | Value                                   |
| ------------------------ | --------------------------------------- |
| Credential               | Your saved Google Gemini API credential |
| Model                    | Select an available free-tier model     |
| Maximum number of tokens | `300`                                   |
| Sampling Temperature     | `0.2`                                   |

For the model, select a lightweight Flash model if it is available to your account. The model list is loaded dynamically from the Gemini API, so choose from the models actually displayed in your n8n instance.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



If you haven't created the credential:

1. Click the credential dropdown.
2. Select Create New Credential.
3. Enter your Google AI Studio API key.
4. Save it.

Do not paste the key into the workflow or chat. [Google AI Studio API keys](https://aistudio.google.com/apikey?utm_source=chatgpt.com).

## 3. Configure Basic LLM Chain

Click Basic LLM Chain.

You should see a parameter called:

Source for Prompt (User Message)

Select:

`Define below`

This is important because our workflow receives `customer_message` from Edit Fields, not `chatInput` from a Chat Trigger.

A prompt field should now appear. Paste this complete prompt:

```
You are an AI customer-support classifier for an
e-commerce business.

Your task is to classify the customer message into
exactly one of these categories:

- order_status
- return_request
- payment_issue
- other

Customer message:
{{ $json.customer_message }}

Instructions:
1. Select only one category.
2. Do not invent order information.
3. Do not claim to have checked an order.
4. If the customer's intent is unclear, select other.
5. Explain your classification in one sentence.

Return the category and explanation.
```

Keep Require Specific Output Format disabled for now. We'll introduce structured JSON output in Lesson 10.

The Basic LLM Chain supports defining a prompt using expressions from previous nodes, while the Gemini model supplies the language model itself.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://app.unpkg.com\&sz=32)

UNPKG+1



## 4. Execute your first AI classification

Your input node should contain:

| Field              | Value                                                                      |
| ------------------ | -------------------------------------------------------------------------- |
| `request_id`       | `REQ-2026-0009`                                                            |
| `customer_message` | `My parcel hasn't arrived yet. Can you tell me when it will be delivered?` |

Now:

1. Click Execute workflow.
2. Wait for the Basic LLM Chain to finish.
3. Open its output.
4. Check the generated response.

Expected classification:

Expected AI result

order_status

The customer is asking for an update about a delayed parcel and its expected delivery date.

This is an expected result, not a claim that your workflow has executed successfully.

## 5. Test two more customer messages

After the first test succeeds, change the `customer_message` value and execute again.

| Test   | Customer message                                       | Expected category |
| ------ | ------------------------------------------------------ | ----------------- |
| TC-038 | I received the wrong product and want to return it.    | `return_request`  |
| TC-039 | My payment was deducted, but the order was not placed. | `payment_issue`   |

## 6. Lesson 09 progress

- Connected Edit Fields to Basic LLM Chain.
- Configured Google Gemini credentials and model.
- Set the prompt source to Define below.
- Executed the first classification successfully.
- Verified TC-038 and TC-039.

Markdown filename: `lesson-09-llm-integration.md`

Learning documentation: `AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-09-llm-integration.md`

Next action: First fix the connection between `Input - Customer Message` and `Basic LLM Chain`, then configure the two nodes. Share the Basic LLM Chain output or the exact error if it fails, and we'll troubleshoot from your actual n8n configuration.