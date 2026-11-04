Excellent! Lesson 09 — LLM Integration is complete. Your Google Gemini integration is working in n8n 2.45, and the `Basic LLM Chain` is successfully connected to the `Google Gemini Chat Model`.

We can now move from basic AI responses to reliable, structured AI output.

# Lesson 10 — Prompt Engineering and Structured AI Outputs

Part 8 · Module 3 · Roadmap Version 2.3

Next lesson

Markdown filename: `lesson-10-prompt-engineering-and-structured-outputs.md`

Learning documentation location:

`AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-10-prompt-engineering-and-structured-outputs.md`

## 1. Lesson objective

In Lesson 09, Gemini returned a natural-language classification. That is useful for understanding a request, but difficult for an automated business workflow to process consistently.

For example, these responses communicate the same result but have different formats:

```
This is an order status enquiry.
```

```
The customer wants to know where their parcel is.
Category: order_status
```

Our enterprise workflow needs a predictable JSON response that other n8n nodes can read.

Our target output:

```
{
  "category": "order_status",
  "confidence": 0.96,
  "reason": "The customer is asking about the delivery status of a parcel.",
  "requires_human_review": false
}
```

The confidence value above is illustrative, not a verified model score.

## 2. Update your existing CAO-003 workflow

Open:

`CAO-003 - AI Request Classification Test`

Keep your existing nodes:

- Manual Trigger
- Input - Customer Message
- Basic LLM Chain
- Google Gemini Chat Model

We will add a Structured Output Parser to the existing AI chain.

## 3. Add Structured Output Parser

1. Open `Basic LLM Chain`.
2. Enable Require Specific Output Format.
3. A new Output Parser connection should appear.
4. Add a Structured Output Parser node.
5. Connect it to the Output Parser input of Basic LLM Chain.

Input - Customer Message

Basic LLM Chain

Prompt and AI processing

Model

Google Gemini Chat Model

Output Parser

Structured Output Parser

## 4. Configure the Structured Output Parser

Open the parser node.

Choose Define using JSON Schema if that option is available.

Use this schema:

```
{
  "type": "object",
  "properties": {
    "category": {
      "type": "string",
      "enum": [
        "order_status",
        "return_request",
        "payment_issue",
        "other"
      ]
    },
    "confidence": {
      "type": "number"
    },
    "reason": {
      "type": "string"
    },
    "requires_human_review": {
      "type": "boolean"
    }
  },
  "required": [
    "category",
    "confidence",
    "reason",
    "requires_human_review"
  ],
  "additionalProperties": false
}
```

This schema defines exactly what fields the model should return and restricts the category to our four approved values.

## 5. Improve the Basic LLM Chain prompt

Replace your previous prompt with this:

```
You are an AI customer-support classification engine
for an e-commerce company.

Analyze the customer message and classify it into
exactly one of these categories:

1. order_status
2. return_request
3. payment_issue
4. other

Classification rules:

- order_status: Delivery updates, shipment tracking,
  delayed orders and order progress.
- return_request: Returns, exchanges, damaged products
  and wrong products.
- payment_issue: Failed payments, duplicate charges,
  refunds related to payment and payment discrepancies.
- other: Anything that does not clearly fit the categories.

Confidence:
Provide a number between 0 and 1 representing your
estimated confidence in the classification.

Human review:
Set requires_human_review to true if the request is
ambiguous, involves a sensitive financial issue, or
requires human judgement.

Do not:
- Invent order information.
- Claim to have accessed customer records.
- Promise refunds or order changes.
- Return categories outside the approved list.

Customer message:
{{ $json.customer_message }}

Follow the connected output schema exactly.
```

## 6. Execute the workflow

Use your existing test message:

```
My parcel hasn't arrived yet.
Can you tell me when it will be delivered?
```

Execute the entire workflow and inspect the Basic LLM Chain output.

You should receive a structured object containing:

- `category`
- `confidence`
- `reason`
- `requires_human_review`

The exact confidence and explanation may vary between executions.

## 7. Test different scenarios

Use these five test cases:

| Test ID | Customer message                                    | Expected category                      |
| ------- | --------------------------------------------------- | -------------------------------------- |
| TC-040  | My parcel hasn't arrived.                           | `order_status`                         |
| TC-041  | I received the wrong product and want to return it. | `return_request`                       |
| TC-042  | My payment was deducted twice.                      | `payment_issue`                        |
| TC-043  | What are your store opening hours?                  | `other`                                |
| TC-044  | I was charged twice and want an immediate refund.   | `payment_issue`, human review expected |

For TC-044, the important requirement is that the model identifies the payment issue and flags it for human review. The model's flag is advisory; actual refund approval must be enforced by workflow logic and authorization controls.

## 8. Lesson 10 completion checklist

Lesson progress

6/6

Enabled Require Specific Output Format in Basic LLM Chain

Added and connected Structured Output Parser

Configured the JSON schema

Updated the classification prompt

Received structured JSON output from Gemini

Passed test cases TC-040 through TC-044

Submit lesson results

What comes next: Lesson 11 — AI Classification and Information Extraction. We will use the structured AI output to extract useful customer and order-related information and prepare it for downstream business workflows.

Remember: keep `CAO-001` unchanged for now. We'll integrate the AI classification into the main commerce platform when the relevant AI components have been tested independently.