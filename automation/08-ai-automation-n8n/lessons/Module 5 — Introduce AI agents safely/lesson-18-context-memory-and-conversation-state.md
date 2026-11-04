# Lesson 18 — Context, Memory, and Conversation State

Roadmap: Version 2.3 → Part 8: AI Automation with n8n\
Project: Enterprise AI Commerce Operations Platform\
Workflow: `CAO-007 - Conversation Context and Memory`

Documentation filename: `lesson-18-context-memory-and-conversation-state.md`

Documentation location:\
`/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-18-context-memory-and-conversation-state.md`

## 1. Learning objectives

In this lesson, we will make the AI workflow remember previous customer messages so that customers don't need to repeat information.

For example:

| Conversation   | Customer message                                  |
| -------------- | ------------------------------------------------- |
| First message  | My order number is ORD-100045.                    |
| Second message | I want to know its delivery status.               |
| Third message  | Can you also tell me which products are included? |

Without memory, the AI may not know what "its" refers to. With memory, it can use the previous conversation to understand the request.

We will implement:

1. Conversation context.
2. Session-based memory.
3. Customer-specific conversation isolation.
4. Context-aware responses.
5. Conversation history testing.
6. Memory limitations and production considerations.

## 2. Create the workflow

Create a new workflow:

`CAO-007 - Conversation Context and Memory`

Use this initial structure:

Manual Trigger

Edit Fields — Customer Conversation Input

AI Agent

Connected to Gemini Chat Model and Simple Memory

Chat Model

Gemini

Memory

Simple Memory

### Step 1 — Configure customer conversation input

Add an Edit Fields node after Manual Trigger.

Rename it:

`Input - Customer Conversation`

Add these fields:

| Field              | Value                            |
| ------------------ | -------------------------------- |
| `session_id`       | `customer-1001`                  |
| `customer_message` | `My order number is ORD-100045.` |
| `customer_id`      | `CUST-1001`                      |
| `channel`          | `web_chat`                       |

For this exercise, use fixed test data. Later, we will use a real session ID supplied by a webhook or chat interface.

### Step 2 — Add the AI Agent

Add an AI Agent node after the Edit Fields node.

Connect your existing Google Gemini Chat Model to the Agent's Chat Model input.

Use the following system message:

```
You are an AI customer support assistant for an
e-commerce platform.

Your responsibilities:
1. Understand the customer's current message.
2. Use previous conversation context when relevant.
3. Remember order references and customer-provided details.
4. Do not ask customers to repeat information already
   provided in the same conversation.
5. If the context does not contain the required
   information, ask the customer for clarification.
6. Never invent order status, payment status,
   delivery information, or refund confirmation.
7. Clearly distinguish remembered information from
   information retrieved from external systems.

Maintain a helpful and professional tone.
```

Set the Agent's user prompt to:

```
{{ $json.customer_message }}
```

### Step 3 — Add Simple Memory

This is the main part of the lesson.

1. Add the Simple Memory node.
2. Connect it to the AI Agent's Memory input.
3. Configure its session ID using the input field:

```
{{ $json.session_id }}
```

4\. Set the context window length to `10` if that option is available.

For the Session ID setting, select the option that allows you to define the ID manually rather than using a Chat Trigger session.

Important

The session ID separates one customer's conversation from another. Two customers must never share the same session ID.

Simple Memory is suitable for this learning exercise. It is not our final production storage solution; later we can consider persistent memory backed by a database.

## 3. Test conversation memory

Run the workflow three times, keeping the same `session_id` each time.

Test 1 — Store customer information

```
My order number is ORD-100045.
```

Expected: The AI acknowledges the order reference.

Test 2 — Use previous context

Change only `customer_message`:

```
Can you tell me its delivery status?
```

Expected: The AI understands that "its" refers to `ORD-100045`. It must not invent a delivery status.

Test 3 — Recall previous context

```
Which order number did I provide earlier?
```

Expected: The AI responds with `ORD-100045`.

## 4. Test customer isolation

Change the session ID to:

```
customer-1002
```

Then send:

```
What is my order number?
```

Expected: The AI should not know `ORD-100045`, because this is a different conversation session.

## 5. Test register

Create or update this file:

`enterprise-ai-commerce-ops/test-data/workflow-test-cases.md`

Add these test cases:

| Test ID | Scenario                    | Expected result                              |
| ------- | --------------------------- | -------------------------------------------- |
| TC-106  | Store order reference       | AI remembers order reference                 |
| TC-107  | Follow-up question          | AI uses previous context                     |
| TC-108  | Recall previous information | AI retrieves the correct order reference     |
| TC-109  | New session                 | Previous customer's context is not available |
| TC-110  | Missing context             | AI asks for clarification                    |
| TC-111  | Unknown delivery status     | AI does not invent delivery information      |

## 6. Production considerations

Understand these distinctions:

- Context: Information required to understand the current request.
- Memory: Information retained from earlier conversation messages.
- Session: A logical conversation belonging to a particular customer.
- Persistent memory: Memory stored in a database or other durable storage so it can survive restarts and be shared safely across executions.

For a production e-commerce system, we will need persistent storage, session expiration, customer identity verification, and strict separation of customer data.

## Completion checkpoint

Do not mark Lesson 18 complete yet. First, configure the workflow and run Test 1.

What should I verify first? The screenshot of your Simple Memory node configuration, including its Session ID setting, will help me check that the memory is connected correctly before you run the remaining tests.