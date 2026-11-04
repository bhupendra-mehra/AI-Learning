# Lesson 21 — Product Requirements, Architecture, and Acceptance Criteria



Roadmap Version 2.3

Lesson 21 of 30



Project: Enterprise AI Commerce Operations Platform

Documentation filename: `lesson-21-product-requirements-architecture-and-acceptance-criteria.md`

Documentation location:

`/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/`

## 1. Lesson objective

So far, we have built individual workflows and reusable workers. Now we need to approach the project as a Product Owner, Solution Architect and AI Automation Engineer.

By the end of this lesson, we will have:

1. Defined the actual business problem.
2. Identified users and their requirements.
3. Defined the functional and non-functional requirements.
4. Designed the complete solution architecture.
5. Defined workflow responsibilities and integrations.
6. Created acceptance criteria for the final project.
7. Established a clear scope for Lesson 22 integration.

We will use the existing n8n workflows. No need to recreate them.

## 2. Define the business problem

Our platform addresses a common e-commerce operations problem.

Customers contact an e-commerce business through forms, email or other channels for:

- Order status enquiries.
- Return and refund requests.
- Order cancellation.
- Payment issues.
- Product information.
- General customer support.

These requests are often handled manually by support teams. This creates delays, repetitive work, inconsistent responses and limited visibility into request processing.

Proposed solution:

An AI-powered automation platform that receives customer requests, validates the information, classifies the request, retrieves relevant commerce data, investigates the issue, applies business rules and routes sensitive operations for human approval.

### Business objectives

| Objective                        | Expected benefit                       |
| -------------------------------- | -------------------------------------- |
| Automate customer request intake | Reduce manual data entry               |
| AI-based classification          | Improve request routing                |
| Automated data retrieval         | Reduce investigation time              |
| Reusable workflow workers        | Improve maintainability                |
| Human approval                   | Prevent unauthorized sensitive actions |
| Centralized monitoring           | Improve operational visibility         |
| Standardized responses           | Improve customer experience            |

## 3. Identify system users

Our platform will have four primary user types.

| User                   | Responsibility                                       |
| ---------------------- | ---------------------------------------------------- |
| Customer               | Submits enquiries and receives updates               |
| Customer Support Agent | Reviews investigation results and handles exceptions |
| Operations Manager     | Reviews escalations and sensitive actions            |
| System Administrator   | Manages credentials, workflows and monitoring        |

### Example user stories

Customer

As a customer, I want to submit an order enquiry so that I can receive relevant information without waiting for manual investigation.

Customer Support Agent

As a support agent, I want AI-generated investigation summaries so that I can understand customer issues quickly.

Operations Manager

As an operations manager, I want refund and cancellation requests to require human approval so that sensitive actions cannot be executed automatically.

System Administrator

As an administrator, I want execution logs and failure alerts so that I can identify and resolve workflow problems.

## 4. Define functional requirements

These are the capabilities our completed project must provide.

| ID    | Functional requirement                         | Existing workflow              |
| ----- | ---------------------------------------------- | ------------------------------ |
| FR-01 | Accept customer requests through webhook       | CAO-001                        |
| FR-02 | Authenticate incoming requests                 | CAO-001                        |
| FR-03 | Validate and normalize customer data           | CAO-001                        |
| FR-04 | Classify customer requests using AI            | CAO-003                        |
| FR-05 | Extract relevant order and request information | CAO-003                        |
| FR-06 | Apply predefined business rules                | CAO-003 / CAO-008              |
| FR-07 | Retrieve commerce data through API             | CAO-006 / CAO-010–012          |
| FR-08 | Coordinate multiple investigation workers      | CAO-009                        |
| FR-09 | Generate AI investigation summaries            | CAO-009                        |
| FR-10 | Require human approval for sensitive actions   | CAO-008                        |
| FR-11 | Handle workflow failures and retries           | CAO-004 and relevant workflows |
| FR-12 | Record execution and operational information   | Monitoring workflows           |
| FR-13 | Generate a standardized customer response      | To be integrated               |
| FR-14 | Maintain an auditable processing history       | To be integrated               |

Note: Existing workflow IDs are mapped to their current responsibilities. We will verify and finalize the mapping during Lesson 22.

## 5. Define non-functional requirements

Functional requirements describe what the system does. Non-functional requirements describe how reliably and securely it should operate.

| ID     | Requirement     | Target                                                                       |
| ------ | --------------- | ---------------------------------------------------------------------------- |
| NFR-01 | Security        | Credentials must be stored using n8n credentials                             |
| NFR-02 | Authentication  | Protected webhook endpoints                                                  |
| NFR-03 | Data protection | Avoid sending unnecessary personal information to AI                         |
| NFR-04 | Reliability     | Retry transient API failures                                                 |
| NFR-05 | Recovery        | Preserve successful results when another operation fails                     |
| NFR-06 | Maintainability | Use reusable workflows                                                       |
| NFR-07 | Scalability     | Support multiple product records dynamically                                 |
| NFR-08 | Auditability    | Record request and execution identifiers                                     |
| NFR-09 | Accuracy        | Never invent order, payment or delivery information                          |
| NFR-10 | Human oversight | Require approval for refunds, cancellations and sensitive payment operations |

We will measure actual performance during testing rather than promise arbitrary response-time guarantees.

## 6. Define the complete solution architecture

This is the target architecture for our project.

## Enterprise AI Commerce Operations Platform

Customer Request Channels

Webhook · Customer Form · Email · Commerce Events

CAO-001 — Customer Request Intake

Authentication · Validation · Normalization

CAO-003 — AI Classification and Extraction

Gemini · Structured Output · Business Routing

CAO-009

Main Orchestrator

CAO-008

Human Approval

CAO-010

Order Worker

CAO-011

Customer Worker

CAO-012

Product Worker

AI Decision Coordinator

Investigation Summary · Missing Information · Recommendations

Final Response and Audit Record

CROSS-CUTTING SERVICES

CAO-004

Error Handling

Monitoring

Execution and Alerts

This is the target design, not a claim that every connection is already implemented. In particular, Lesson 22 will complete the end-to-end integration and resolve the deferred error-handling work.

## 7. Define business processing flows

We need three main processing paths.

### Flow A — Order status enquiry

1. Customer submits an order enquiry.
2. CAO-001 authenticates and validates it.
3. CAO-003 classifies the request.
4. CAO-009 coordinates the investigation.
5. CAO-010 retrieves order information.
6. CAO-011 retrieves customer information.
7. CAO-012 retrieves relevant product information.
8. AI Decision Coordinator prepares the investigation summary.
9. System generates the customer response.

### Flow B — Refund or cancellation request

1. Customer submits a refund or cancellation request.
2. CAO-003 identifies the request type.
3. Business rules mark it as sensitive.
4. CAO-008 requests human approval.
5. If rejected, the operation stops and records the decision.
6. If approved, the workflow proceeds through the authorized business operation.
7. The outcome is recorded and communicated.

Important: Approval is not the same as execution. An approved request must still pass the relevant business and API checks.

### Flow C — Payment issue

1. Customer submits a payment-related issue.
2. AI identifies the payment issue.
3. Business rules route it for human review.
4. Relevant order and payment information is investigated.
5. The responsible team reviews the findings.
6. The customer receives an appropriate response.

## 8. Define acceptance criteria

Acceptance criteria determine when the complete project can be considered ready.

Create a new file:

`enterprise-ai-commerce-ops/test-data/project-acceptance-criteria.md`

Add these criteria:

| ID    | Acceptance criterion             | Expected result                                 |
| ----- | -------------------------------- | ----------------------------------------------- |
| AC-01 | Valid customer request submitted | Request accepted                                |
| AC-02 | Invalid request submitted        | Clear validation error                          |
| AC-03 | Unauthorized webhook request     | Rejected                                        |
| AC-04 | Order-status request classified  | Correct category                                |
| AC-05 | Refund request classified        | Human review required                           |
| AC-06 | Payment issue classified         | Human review required                           |
| AC-07 | Order investigation executed     | Relevant order data retrieved                   |
| AC-08 | Customer investigation executed  | Relevant customer data retrieved                |
| AC-09 | Multiple products investigated   | All requested product records retrieved         |
| AC-10 | Investigation results combined   | Complete structured result                      |
| AC-11 | AI summary generated             | Only verified facts included                    |
| AC-12 | Refund approval rejected         | No refund operation executed                    |
| AC-13 | Refund approval granted          | Authorized execution path only                  |
| AC-14 | Temporary API failure            | Retry and recovery behaviour verified           |
| AC-15 | Permanent API failure            | Failure recorded and surfaced                   |
| AC-16 | Execution monitoring checked     | Execution status and relevant details available |
| AC-17 | Customer response generated      | Correct response based on actual result         |
| AC-18 | Audit record created             | Request and execution trace available           |

These are project-level acceptance criteria. They are not all passed yet.

## 9. Create the project requirements documentation

Inside the existing project directory, create:

```
enterprise-ai-commerce-ops/
│
├── README.md
│
├── docs/
│   ├── product-requirements.md
│   ├── solution-architecture.md
│   └── workflow-inventory.md
│
├── workflows/
│
├── test-data/
│   ├── workflow-test-cases.md
│   └── project-acceptance-criteria.md
│
└── screenshots/
```

Do not recreate the existing folders or move your current workflows. Add only the new documents that do not already exist.

Suggested document responsibilities:

| File                             | Content                                                                           |
| -------------------------------- | --------------------------------------------------------------------------------- |
| `product-requirements.md`        | Business problem, users, user stories, functional and non-functional requirements |
| `solution-architecture.md`       | Architecture, components, data flow, integrations and security                    |
| `workflow-inventory.md`          | CAO workflow IDs, responsibilities, dependencies and status                       |
| `project-acceptance-criteria.md` | Final project acceptance criteria                                                 |

## 10. Lesson 21 completion checklist

Implementation tracker

# 11/11

Business problem and objectives defined

Primary users and user stories documented

Functional requirements FR-01 to FR-14 documented

Non-functional requirements NFR-01 to NFR-10 documented

Target solution architecture documented

Three business processing flows documented

Project acceptance criteria AC-01 to AC-18 documented

Product requirements document created

Solution architecture document created

Workflow inventory created

Acceptance criteria document created

Lesson 21 documentation filename: `lesson-21-product-requirements-architecture-and-acceptance-criteria.md`

Documentation directory: `/var/www/html/AI-Learning/automation/08-ai-automation-n8n/lessons/`

## What comes next?

After Lesson 21, we move to Lesson 22 — Integrate Complete Business Workflow.

That is where we will connect the existing workflows into one complete customer journey, including:

- Customer intake to final response.
- AI classification to investigation.
- Dynamic multi-product retrieval.
- Human approval and authorized action execution.
- Centralized error handling and recovery.
- Execution monitoring and audit records.

For now, complete Section 9 by creating the four project documents. We can then verify your workflow inventory and use it as the baseline for Lesson 22.