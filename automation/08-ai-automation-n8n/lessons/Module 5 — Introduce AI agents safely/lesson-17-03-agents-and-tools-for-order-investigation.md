Yes. We can cover all five remaining topics in one complete practical session. There is no need to split Lesson 17 into multiple sessions because they are closely connected.

We will build and test the complete agent workflow in one go, using your existing CAO-006 workflow.

# Lesson 17 — Agents and Tools for Order Investigation

Final implementation session

Roadmap: Version 2.3 → Part 8\
Project: Enterprise AI Commerce Operations Platform\
Workflow: `CAO-006 - AI Order Investigation Agent`\
n8n version: 2.45

Markdown filename: `lesson-17-agents-and-tools-for-order-investigation.md`

Documentation location:

`/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/lesson-17-agents-and-tools-for-order-investigation.md`

## 1. What we will complete

| Topic                       | Practical implementation                          |
| --------------------------- | ------------------------------------------------- |
| 1. Dynamic tool parameters  | Agent dynamically supplies cart ID                |
| 2. Multiple tools           | Cart lookup and product lookup                    |
| 3. Dynamic tool selection   | Agent chooses the appropriate tool                |
| 4. Multi-step investigation | Agent retrieves cart and then product details     |
| 5. Failure handling         | Handle missing cart, invalid input and API errors |

## 2. Final architecture

Customer Query

CAO-006 — AI Agent

Google Gemini Chat Model

Available tools

&#x20;`lookup_cart_details`

&#x20;`lookup_product_details`

Verify API results and handle failures

Customer response

Human review

We will use DummyJSON mock data throughout. It is not connected to Magento or real customer orders.

## Part A — Dynamic tool parameters

### 3. Update the existing HTTP Request Tool

Open CAO-006 and select the existing HTTP Request Tool.

Rename it:

`lookup_cart_details`

Configure:

| Setting        | Value            |
| -------------- | ---------------- |
| Method         | GET              |
| URL            | Expression below |
| Authentication | None             |

Use this URL expression:

```
{{ 'https://dummyjson.com/carts/' + $fromAI('cart_id', 'Numeric DummyJSON cart ID. Must be explicitly supplied by the customer.', 'number') }}
```

The `$fromAI()` function allows the agent to supply a parameter when calling the tool.

Update the tool description:

```
Retrieve mock commerce cart information using a numeric cart ID.

Use this tool when a customer asks about a specific
DummyJSON cart.

The cart_id must be supplied by the customer.
Do not invent or assume a cart ID.

This API returns mock cart data, not real Magento orders
or shipment tracking information.
```

### 4. Update the System Message

Replace the old fixed-cart instructions with:

```
You are an AI commerce investigation assistant.

You can investigate mock commerce data using the
connected tools.

RULES:

1. Understand the customer's request.
2. Use the appropriate tool when data retrieval is required.
3. Never invent cart IDs or product IDs.
4. Use only the actual API response.
5. Clearly distinguish mock data from real orders.
6. Never claim that an actual Magento order was found.
7. Never approve refunds or modify orders.
8. Never claim that a task was escalated unless an
   actual workflow performed that action.
9. If required information is missing, ask the customer
   for clarification.
10. If an API fails, explain that the information
    could not be retrieved.
```

### 5. Test dynamic parameters

Use this input:

```
{
  "customer_message": "Please investigate mock cart 2 and tell me its total amount and products."
}
```

Expected tool execution:

```
Tool: lookup_cart_details
cart_id: 2

GET https://dummyjson.com/carts/2
```

The agent should report the total and products from the actual API response.

Important: Do not use `ORD-100045` as a cart ID. They are different identifiers.

## Part B — Multiple tools and dynamic tool selection

### 6. Add a second tool

Add another HTTP Request Tool connected to the AI Agent.

Rename it:

`lookup_product_details`

Configure:

| Setting        | Value            |
| -------------- | ---------------- |
| Method         | GET              |
| URL            | Expression below |
| Authentication | None             |

Use:

```
{{ 'https://dummyjson.com/products/' + $fromAI('product_id', 'Numeric DummyJSON product ID explicitly supplied by the customer or obtained from a verified cart response.', 'number') }}
```

Tool description:

```
Retrieve mock product details using a numeric product ID.

Use this tool when a customer requests information about
a product, such as its title, price, brand, category or rating.

The product ID must be supplied by the customer or obtained
from a verified cart response.

Never invent a product ID.
```

You should now have two connected tools:

- `lookup_cart_details`
- `lookup_product_details`

### 7. Test tool selection

Use these three inputs separately.

TC-096 — Cart enquiry

```
{
  "customer_message": "Investigate mock cart 2 and tell me its total and products."
}
```

Expected: Agent calls `lookup_cart_details`.

TC-097 — Product enquiry

```
{
  "customer_message": "Please retrieve details of DummyJSON product 1, including its title and price."
}
```

Expected: Agent calls `lookup_product_details`.

TC-098 — General question

```
{
  "customer_message": "What information can you retrieve from the available mock commerce tools?"
}
```

Expected: Agent explains its capabilities. It should not call an unnecessary tool.

## Part C — Multi-step investigation

### 8. Teach the agent to use multiple tools

Update the System Message by adding:

```
MULTI-STEP INVESTIGATION:

When a customer asks for cart details and information
about the products in that cart:

1. Call lookup_cart_details using the supplied cart ID.
2. Inspect the returned cart response.
3. Extract product IDs from the actual cart response.
4. Call lookup_product_details for products when
   additional product information is requested.
5. Use only product IDs returned by the verified cart.
6. Combine the cart and product information.
7. If any tool fails, clearly identify which information
   could not be retrieved.
8. Do not invent missing product information.
```

### 9. Execute a multi-step test

Use:

```
{
  "customer_message": "Please investigate mock cart 1. Tell me its total amount, list its products, and retrieve the product titles and prices."
}
```

Expected sequence:

```
AI Agent
   |
   |-- lookup_cart_details(cart_id=1)
   |       |
   |       +-- Returns cart and product IDs
   |
   |-- lookup_product_details(product_id=...)
   |       |
   |       +-- Returns product details
   |
   |-- lookup_product_details(product_id=...)
   |       |
   |       +-- Returns additional product details
   |
   +-- Combines verified information
```

The number of product-tool calls will depend on the products returned by the cart.

Important: The agent may make multiple tool calls, but this is still one AI Agent. It is not yet a multi-agent system.

## Part D — Tool failure handling

### 10. Test missing cart

Use:

```
{
  "customer_message": "Investigate DummyJSON cart 999999 and tell me its contents."
}
```

Expected:

- The agent attempts the cart lookup.
- The API returns a not-found response or an error.
- The agent explains that the cart could not be retrieved.
- No invented cart details.

### 11. Test invalid cart ID

Use:

```
{
  "customer_message": "Investigate mock cart ABC123."
}
```

Expected:

- Agent should not invent or silently convert the ID.
- It should request a valid numeric cart ID.
- It should not make an inappropriate API request.

### 12. Test API failure

For a controlled failure test, create a temporary test copy of the cart tool and change its URL to:

```
https://dummyjson.com/carts/999999999
```

Run the agent with a request to retrieve that cart.

Expected:

- Tool execution fails or returns a not-found response.
- Agent does not fabricate information.
- Agent explains that the lookup was unsuccessful.

Do not replace the working production-learning tool with the failing test URL. Restore or discard the temporary test copy after verification.

### 13. Error-handling rules

Add this to the System Message:

```
TOOL FAILURE HANDLING:

1. Never fabricate data when a tool fails.
2. Do not claim that a failed lookup succeeded.
3. Explain when an API is unavailable or a record
   cannot be found.
4. Do not repeatedly call a failing tool without
   a valid reason.
5. If required information is missing, ask the customer.
6. Sensitive or unresolved cases require human review.
```

## Part E — Final integration and validation

### 14. Final CAO-006 structure

Your workflow should contain:

| Component                    | Configuration                     |
| ---------------------------- | --------------------------------- |
| Manual Trigger               | Starts test execution             |
| Input - Customer Order Query | Receives customer message         |
| AI Agent                     | Investigates customer requests    |
| Google Gemini Chat Model     | Reasoning and response generation |
| lookup_cart_details          | Dynamic cart lookup               |
| lookup_product_details       | Dynamic product lookup            |

No separate Calculator tool is required in the final workflow.

### 15. Final test register

Add these test cases to:

`enterprise-ai-commerce-ops/test-data/workflow-test-cases.md`

| ID     | Scenario                                     | Expected result                      |
| ------ | -------------------------------------------- | ------------------------------------ |
| TC-096 | Dynamic cart ID                              | Correct cart ID supplied             |
| TC-097 | Product enquiry                              | Product tool selected                |
| TC-098 | General question                             | No unnecessary tool call             |
| TC-099 | Cart and product investigation               | Multiple tools used correctly        |
| TC-100 | Unknown cart                                 | No fabricated information            |
| TC-101 | Invalid cart ID                              | Requests valid identifier            |
| TC-102 | API not-found response                       | Safe failure response                |
| TC-103 | Product details from cart                    | Product IDs taken from verified cart |
| TC-104 | Tool failure during multi-step investigation | Partial results clearly identified   |
| TC-105 | Prompt injection                             | System instructions preserved        |

Record actual results, not just expected results.

## 16. Final completion checklist

Lesson 17 progress

# 10/10

Configured dynamic cart ID using $fromAI()

Tested lookup_cart_details with cart 2

Added lookup_product_details

Tested independent cart and product tool selection

Tested a request requiring multiple tools

Verified product IDs come from the cart response

Tested missing cart and invalid cart ID

Tested controlled API failure

Verified the agent never fabricates tool results

Updated TC-096 through TC-105 in the test register

## 17. What you will be able to demonstrate after Lesson 17

You will have an AI Agent that:

- Dynamically supplies API parameters.
- Selects from multiple tools.
- Executes multi-step investigations.
- Combines information from different APIs.
- Handles missing records and API failures.
- Avoids presenting fabricated information as verified results.

This is a meaningful progression beyond CAO-003's classification and predefined routing.

One technical note: The `$fromAI()` expressions and multi-tool behaviour must be verified in your n8n 2.45 execution logs. The agent's final answer alone is not proof that the tools were called or that their results were used.

Next roadmap lesson

Lesson 18 — Context, Memory, and Conversation State

That lesson will build on CAO-006 by teaching the agent to retain relevant context across customer interactions, rather than investigating every message in isolation.

Start with Part A, then continue through the remaining parts in the same session. If an n8n 2.45 configuration behaves differently, share the relevant screenshot and we'll adapt the implementation without restarting the lesson.