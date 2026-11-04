Your observation is correct. In fact, you have identified an important gap in how we implemented Lesson 17.

CAO-003 already performs AI classification, information extraction, decision-making, business routing and human-review handling. So far, CAO-006 has not demonstrated enough new functionality to justify building another workflow that simply receives a customer message, calls Gemini and returns a response.

We need to distinguish the two properly.

## 1. CAO-003 vs CAO-006

| Capability                   | CAO-003 — AI Classification        | CAO-006 — AI Agent                         |
| ---------------------------- | ---------------------------------- | ------------------------------------------ |
| Understand customer messages | Yes                                | Yes                                        |
| AI classification            | Yes                                | Can do                                     |
| Information extraction       | Yes                                | Can do                                     |
| Structured output            | Yes                                | Optional                                   |
| Business-rule decisions      | Yes, predefined rules              | Can reason and select tools                |
| Workflow routing             | Switch and IF nodes                | Agent selects tools dynamically            |
| API integration              | HTTP Request node                  | HTTP Request Tool                          |
| Tool selection               | Predetermined workflow connections | Agent decides which tool to invoke         |
| Multiple tools               | Predetermined connections          | Can choose among available tools           |
| Multi-step investigation     | Explicit workflow steps            | Can decide and execute multiple tool calls |
| Human approval               | Explicit IF-based routing          | Can request or trigger a review workflow   |

The biggest difference is not that one uses Gemini and the other uses an AI Agent.

It is who decides what happens next.

## 2. Example: How the two workflows behave differently

Consider this customer message:

> My order ORD-100045 has not arrived. Can you check its status and tell me whether payment was successful?

### CAO-003 — Classification-based workflow

Customer message

Gemini classification and extraction

Order status

Payment issue

Predefined IF/Switch routing

Automatic processing or human review

CAO-003 follows the business logic we explicitly configured.

### CAO-006 — Agent-based investigation

Customer message

AI Agent understands the task

Agent decides which tools are needed

Shipment lookup

Payment lookup

Order lookup

Agent combines the actual tool results

Customer response or human review

The agent decides whether it needs one tool or several, executes them, evaluates their responses and prepares a combined answer.

That is the additional capability we need to learn.

## 3. What is missing from our current Lesson 17 implementation?

Our current CAO-006 has:

- Gemini Chat Model.
- AI Agent.
- HTTP Request Tool.
- Fixed DummyJSON endpoint.
- Basic tool-use instructions.

This proves that an agent can call a tool, but it does not yet demonstrate a meaningful autonomous investigation.

We still need to implement:

| Missing capability       | What we should build                                         |
| ------------------------ | ------------------------------------------------------------ |
| Dynamic parameters       | Agent passes the actual order reference to the API           |
| Multiple tools           | Separate order, shipment and payment lookup tools            |
| Tool selection           | Agent chooses tools according to customer intent             |
| Multi-step investigation | Agent uses results from one tool to decide the next action   |
| Result aggregation       | Agent combines information from multiple APIs                |
| Error recovery           | Agent handles missing data and API failures                  |
| Controlled escalation    | Agent sends unresolved cases to a real human-review workflow |

## 4. How I recommend changing the remaining roadmap

Rather than repeating the work already completed in CAO-003, we should make the remaining lessons progressively more advanced.

| Stage             | Learning focus           | Practical outcome                                   |
| ----------------- | ------------------------ | --------------------------------------------------- |
| Lesson 17         | AI Agents and Tools      | Single agent with dynamic tool selection            |
| Lesson 18         | Multi-Agent Systems      | Specialized Order, Payment and Returns Agents       |
| Lesson 19         | Agent Orchestration      | Coordinate multiple agents and workflows            |
| Lesson 20         | Agent Memory and Context | Maintain useful conversation context                |
| Lesson 21 onwards | Advanced automation      | Build reliable, production-oriented agent workflows |

These are proposed refinements to the learning approach; we should preserve the original roadmap titles and numbering unless we explicitly revise them.

## 5. What we should do with CAO-006

I recommend keeping CAO-006, but upgrading it instead of considering the current implementation complete.

The target should be:

Enterprise AI Order Investigation Agent

A customer should be able to ask:

> My order ORD-100045 has not arrived. Please check the shipment status and payment details.

The agent should independently:

1. Extract `ORD-100045`.
2. Call the order lookup tool.
3. Determine whether shipment information is available.
4. Call the shipment lookup tool if necessary.
5. Check payment information if requested.
6. Compare the results.
7. Explain the findings.
8. Escalate unresolved issues through an actual human-review workflow.

All tools should initially be read-only.

My recommendation: Do not mark Lesson 17 complete yet. The current Calculator and fixed DummyJSON tests are introductory exercises, not the complete agent implementation we need.

We should now turn CAO-006 into a genuinely tool-using investigation agent, while retaining CAO-003 as the classification and business-routing workflow.

This will also make the next multi-agent lessons substantially more meaningful, rather than repeating the same Gemini prompting and IF/Switch concepts.