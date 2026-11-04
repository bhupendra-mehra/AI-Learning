Lesson 17 is not fully completed yet. We have successfully implemented the introductory AI Agent and HTTP Request Tool integration, but the advanced tool-use capabilities that distinguish CAO-006 from CAO-003 are still outstanding.

We will finish Lesson 17 before moving to Lesson 18.

# Lesson 17 — Remaining implementation



Completed

&#x20;Introductory agent setup



| Component                   | Status    |
| --------------------------- | --------- |
| CAO-006 workflow created    | Completed |
| Gemini Chat Model connected | Completed |
| AI Agent configured         | Completed |
| Calculator tool tested      | Completed |
| HTTP Request Tool connected | Completed |
| Agent tool invocation       | Tested    |
| Dynamic tool parameters     | Pending   |
| Multiple tools              | Pending   |
| Multi-step investigation    | Pending   |
| Tool failure handling       | Pending   |
| Final test register         | Pending   |

## Next topic — Dynamic Tool Parameters

Currently, your HTTP Request Tool always calls:

`https://dummyjson.com/carts/1`

This is a fixed endpoint. The agent cannot dynamically choose which cart to retrieve.

We will change this so the agent can provide a parameter when calling the tool.

### 1. Understand the difference

Current implementation

Customer asks about cart 1.

AI Agent calls fixed URL.

/carts/1

Target implementation

Customer asks about cart 2.

AI Agent extracts cart ID.

HTTP Request Tool receives cart ID dynamically.

/carts/2

### 2. Update the HTTP Request Tool

Open the HTTP Request Tool connected to CAO-006.

Change its URL from:

```
https://dummyjson.com/carts/1
```

To this expression:

```
{{ 'https://dummyjson.com/carts/' + $fromAI('cart_id', 'Numeric mock cart ID to retrieve', 'number') }}
```

Keep:

- Method: GET
- Authentication: None

The `$fromAI()` expression allows the AI Agent to supply the parameter when it invokes the tool.

### 3. Update the tool description

Use:

```
Retrieve mock commerce cart information by numeric cart ID.

You must use this tool when the customer asks to
investigate a mock cart.

The cart_id parameter must be a numeric identifier.

Use the identifier explicitly supplied by the customer.
Do not invent or assume a cart ID.

The API returns mock cart data, not Magento orders
or real shipment tracking information.
```

### 4. Update the customer input

For this exercise, use:

```
{
  "customer_message": "Please investigate mock cart 2 and tell me its total amount and products.",
  "order_reference": "ORD-100045",
  "customer_email": "customer@example.com"
}
```

Notice that the customer reference and mock cart ID are different. Do not treat them as interchangeable.

### 5. Test dynamic tool execution

Run the workflow.

Expected:

- Agent identifies mock cart ID `2`.
- Agent invokes `lookup_order_details` with `cart_id = 2`.
- HTTP Request Tool calls `https://dummyjson.com/carts/2`.
- Agent reads the returned cart information.
- Agent reports the actual total and products from the response.

If the agent does not call the tool, inspect the execution logs and tool arguments.

## Lesson 17 remaining sequence

After this test, we will implement:

1. Multiple tools: Separate mock cart lookup and product lookup tools.
2. Dynamic tool selection: Agent chooses the relevant tool based on the request.
3. Multi-step investigation: Agent retrieves cart data and then looks up relevant product information.
4. Failure handling: Missing cart, invalid identifier and API failure.
5. Final validation: Verify that the agent never confuses mock data with real Magento orders.

Documentation

Filename: `lesson-17-agents-and-tools-for-order-investigation.md`

Location: `/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/`

Start with the dynamic URL configuration and share the HTTP Request Tool screenshot before executing it. We will verify the `$fromAI()` configuration against your n8n 2.45 interface.&#x20;