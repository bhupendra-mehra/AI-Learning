Lesson 05 is complete. Your webhook successfully receives the customer request, passes it through the existing processing nodes, and routes `return_request` to the Returns Team.

We can now move to Lesson 06 and extend the same Enterprise AI Commerce Operations Platform with a real API integration.

# Part 8 — Lesson 06: REST APIs, HTTP Request, JSON, and Expressions

Lesson 05 completed

Lesson 06 of 30

Project: Enterprise AI Commerce Operations Platform\
Existing workflow: `CAO-001 - Customer Request Intake`

Your webhook now works, and `return_request` correctly reaches the Returns Team. We will preserve that working flow and add our first external API integration.

## 1. What we are building

An e-commerce automation platform needs to retrieve information from other systems. For example, when a customer asks about an order, the workflow may need to retrieve the order's status, items, and total before responding.

Today, we'll learn how to make an HTTP request and inspect a JSON response. We'll use a public mock commerce API for practice rather than connecting to a real store or using production customer data.

Customer Request

Your existing webhook and request intake

Order Operations route

Selected by the Switch node

HTTP Request node

Calls the mock commerce API

JSON response

Order-like data available for inspection

## 2. Understand the fundamentals

### REST API

A REST API lets one application request or modify resources managed by another application using HTTP.

| Method   | Typical purpose                  | Example               |
| -------- | -------------------------------- | --------------------- |
| `GET`    | Retrieve information             | Fetch an order        |
| `POST`   | Create a resource or submit data | Create a support case |
| `PUT`    | Replace a resource               | Replace a record      |
| `PATCH`  | Update selected fields           | Change an order note  |
| `DELETE` | Delete a resource                | Remove a test record  |

For this lesson, we will use `GET` only. We won't modify or delete any data.

### JSON

JSON is a common format for exchanging structured information between applications.

For example, an API might return:

```
{
  "id": 1,
  "userId": 5,
  "total": 100,
  "totalProducts": 2,
  "totalQuantity": 3
}
```

Each key identifies a field, and its associated value provides the data.

### HTTP Request node

n8n's HTTP Request node allows you to configure the URL, method, query parameters, headers, authentication, and response handling without writing a custom API client.

Business relevance: Most automation jobs involve integrating existing systems. Knowing how to configure requests, inspect responses, and handle errors is essential even when you use low-code tools.

## 3. Practical implementation — Add your first API call

We will add the API call to the Order Operations output of your existing Switch node. This keeps the API exercise on the relevant business route and leaves Returns Team and Payments Team unchanged.

### Step 3.1 — Add the HTTP Request node

1. Open `CAO-001 - Customer Request Intake`.
2. Find the `Order Operations` output on `Switch - Request Routing`.
3. Click the `+` beside that output.
4. Add an HTTP Request node.
5. Rename it `API - Fetch Mock Commerce Data`.

Your existing routing remains intact:

- Order Operations → HTTP Request
- Returns Team → unchanged
- Payments Team → unchanged

This first integration uses mock data to teach API mechanics. In a later lesson, we'll introduce credentials and more realistic business-system integration.

### Step 3.2 — Configure the HTTP Request node

Use these settings:

| Setting               | Value                           |
| --------------------- | ------------------------------- |
| Method                | `GET`                           |
| URL                   | `https://dummyjson.com/carts/1` |
| Authentication        | `None`                          |
| Send Query Parameters | Off                             |
| Send Headers          | Off                             |
| Send Body             | Off                             |

DummyJSON provides sample commerce-related data, so this is suitable for practicing retrieval without accessing a real customer's order.

Click Execute step with a valid input from the Order Operations route.

If the public endpoint is unavailable from your environment, check connectivity and retry later rather than changing your existing workflow.

### Step 3.3 — Inspect the response

A successful response should include a cart object with fields such as `id`, `products`, `total`, `totalProducts`, and `totalQuantity`. Exact sample values may vary with the API's data.

Example response structure:

```
{
  "id": 1,
  "products": [
    {
      "id": 144,
      "quantity": 1,
      "title": "Sample product",
      "price": 100
    }
  ],
  "total": 100,
  "totalProducts": 1,
  "totalQuantity": 1
}
```

This is an illustrative example, not a guarantee of the endpoint's exact live response.

Important: The mock API's cart ID is not your request's order reference. We are using it to learn the HTTP Request node, not to claim that `ORD-100045` has been looked up. Connecting a customer order reference to a genuine commerce API is a separate integration task.

## 4. Read fields from the API response using expressions

Once the HTTP Request node succeeds, inspect its output and use expressions to read response fields.

For example, if the response contains `total`:

```
{{ $json.total }}
```

For the number of products:

```
{{ $json.totalProducts }}
```

For the first product's title:

```
{{ $json.products[0].title }}
```

These expressions assume that the response has the structure shown. If your actual response differs, inspect its JSON before selecting a field.

Expressions are useful because later workflow nodes can use API results to prepare customer responses, evaluate business rules, or create support tickets.

## 5. Understand a critical integration issue: preserving data

The HTTP Request node normally outputs the API response. This means the original request fields, such as `request_id` and `customer_email`, may no longer be present in that node's output.

In an enterprise workflow, losing the original request context can cause problems when you need to connect an API result back to the customer case.

We will address this in a subsequent integration exercise by explicitly preserving and combining the original request with the API response. For now, keep the HTTP Request node on the Order Operations branch so the successful webhook and routing flow remain available.

## 6. Troubleshooting

| Problem                             | What to check                                                                |
| ----------------------------------- | ---------------------------------------------------------------------------- |
| HTTP 404                            | Verify the endpoint URL.                                                     |
| Connection or DNS error             | Check internet access from the n8n environment.                              |
| HTTP 429                            | The service may be rate-limiting requests; wait before retrying.             |
| Output has unexpected fields        | Inspect the actual response in JSON view.                                    |
| Original request fields are missing | The HTTP Request node may have replaced the incoming item with its response. |
| HTTP Request node does not run      | Verify that the input reaches the Order Operations output.                   |

## 7. Lesson 06 test cases

Run these tests and record the actual results.

| Test ID | Scenario                         | Expected result                                                 |
| ------- | -------------------------------- | --------------------------------------------------------------- |
| TC-027  | Submit an `order_status` request | Order Operations route is selected                              |
| TC-028  | Execute the HTTP Request node    | Successful HTTP response                                        |
| TC-029  | Inspect response JSON            | Cart fields are visible                                         |
| TC-030  | Evaluate `{{ $json.total }}`     | Returns the response's total value                              |
| TC-031  | Submit a `return_request`        | Returns Team still works without calling this API branch        |
| TC-032  | Inspect the HTTP Request output  | Identify which original request fields are retained or replaced |

## 8. Lesson 06 completion checklist

Added the HTTP Request node to the Order Operations branch.

Configured the GET request to the mock commerce API.

Executed the request and inspected the actual JSON response.

Verified at least one response field using an expression.

Confirmed that the Returns Team route still works and documented the test results.

5 of 5 verified

Lesson 06 complete

Continue to Lesson 07

Next lesson — Lesson 07: Authentication, Credentials, and Third-Party Integrations. We'll learn how API keys, bearer tokens, and managed credentials work, and how to protect secrets instead of placing them directly into workflow fields.