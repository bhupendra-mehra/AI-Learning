Agreed. We should build one enterprise-grade automation product from Lesson 01 through the final lesson, not a collection of disconnected exercises or a student-level demonstration.

The project should resemble something a company would commission from an AI Automation Engineer: it needs real business requirements, multiple integrations, operational safeguards, measurable outcomes, documentation, and a deployment plan. Every lesson will develop one part of the same product, and later lessons will improve the work we already built.

We will also remove the Student Management API from this roadmap. Your completed FastAPI work remains part of your learning history, but it will not be a dependency for this project.

# Updated AI Learning Roadmap — Version 2.3

# Enterprise AI Commerce Operations Platform

Project selected

A single client-oriented product developed progressively across all six modules of Part 8.

## 1. The product we will build

[Order Management System (OMS) — EDIconnect | EDIconnect](https://images.openai.com/static-rsc-4/6jlUGYXGKOs4McOfCOQ8IenPiUMMteBtBE59S0WhhdKHZht3TJYJ5ql_1XlNoXlJtSs8faYZfXt79cfLqlL6N3gqbslOY1WI-IQ-jv9JMUDZK63ftiDjUIOHf51OIkTp_qqi3Hlc6a0ROfU5CANplsyqHVdR1rnyUk5kszGrXzA?purpose=inline)

[ediconnect.ro](https://www.ediconnect.ro/order-management?utm_source=chatgpt.com)

Product concept: An AI-powered e-commerce operations platform that automates order-related customer requests, document processing, exception handling, and business-team routing.

This is a realistic business solution for an e-commerce company using Magento or a similar commerce platform. We will build it as a separate learning product, without modifying your existing Magento installation.

### Business problems it will solve

- Customer support teams manually investigate order-status and delivery questions.
- Employees repeatedly copy information between e-commerce, CRM, ticketing, and ERP systems.
- Invoices, customer messages, and return requests require manual data extraction.
- Important orders and complaints can be delayed or routed incorrectly.
- Refunds and other consequential actions need validation, authorization, and an audit trail.
- Managers lack a consistent view of automation performance and failure rates.

### Target product architecture

Business channels

Web forms · Webhooks · Email · Commerce events

n8n automation layer

Validation · Data transformation · Business rules · Routing

AI intelligence layer

LLM classification · Structured extraction · Bounded AI agents

Commerce systems

Orders and fulfillment

Support systems

Tickets and notifications

Data and audit

Records and execution history

Human oversight

Approvals and exceptions

We will start with sample business data and local integrations. Later, we will introduce real APIs and appropriate sandbox or staging systems. No live customer data, production credentials, or real refunds will be used during practice.

## 2. How every module contributes to the same product

| Module                         | What we will build into the product                                         |
| ------------------------------ | --------------------------------------------------------------------------- |
| 1. n8n Foundations             | The initial workflow, request intake, and routing logic                     |
| 2. APIs and Business Data      | Commerce integrations, webhooks, databases, and data validation             |
| 3. Practical AI Integration    | Customer-message classification, document extraction, and AI decisions      |
| 4. Reliability and Production  | Retries, logging, security, monitoring, and performance improvements        |
| 5. AI Agents and Orchestration | Controlled agents, tool calling, approval gates, and exception recovery     |
| 6. Portfolio and Deployment    | Integrated product, testing, deployment, documentation, and client handover |

The rule for every lesson: we will add a capability to the same product, test it, and preserve it for subsequent lessons. No unrelated practice projects.

## 3. Updated Part 8 lesson plan

The original 30 lessons remain in place. Their exercises and deliverables will now all use the commerce operations platform.

## Module 1 — Build the foundation

Lessons 01–04

- 01\. Product requirements, isolated n8n setup, and the first business workflow
- 02\. Workflow architecture, nodes, connections, and execution data
- 03\. Request intake, triggers, schedules, and expressions
- 04\. Business rules, branching, loops, and order-request routing

Deliverable: A working order-request intake and routing workflow.

## Module 2 — Connect business systems

Lessons 05–08

- 05\. Order-event webhooks and request intake
- 06\. REST APIs, JSON, and commerce order lookups
- 07\. Authentication, credentials, and application connectors
- 08\. Order-data validation, normalization, deduplication, and routing

Deliverable: A validated integration workflow with reliable data exchange.

## Module 3 — Add AI intelligence

Lessons 09–12

- 09\. LLM integration for customer operations
- 10\. Prompt design and structured outputs
- 11\. Classify requests and extract invoice or return information
- 12\. AI-assisted case handling with human review

Deliverable: AI-assisted classification and document processing.

## Module 4 — Make it production-ready

Lessons 13–16

- 13\. Retries, exceptions, and failed integration recovery
- 14\. Testing, debugging, and execution analysis
- 15\. Credentials, permissions, data privacy, and security
- 16\. Monitoring, performance, and operational alerts

Deliverable: An observable, tested, and secure workflow.

## Module 5 — Introduce AI agents safely

Lessons 17–20

- 17\. Agents and tools for order investigation
- 18\. Context, memory, and conversation state
- 19\. Approval gates for refunds, cancellations, and other sensitive actions
- 20\. Multi-step orchestration and recovery from partial failures

Deliverable: A bounded AI agent that investigates cases and proposes controlled actions.

## Module 6 — Deliver the client solution

Lessons 21–24

- 21\. Product requirements, architecture, and acceptance criteria
- 22\. Integrate the complete business workflow
- 23\. Deploy, secure, test, and document the solution
- 24\. Final acceptance testing, portfolio presentation, and interview preparation

Deliverable: An end-to-end portfolio product with documentation and a deployment plan.

## Advanced extensions — Lessons 25–30

- 25\. Business process analysis and ROI measurement
- 26\. Database and enterprise application integrations
- 27\. Advanced document processing and validation
- 28\. Targeted Python/JavaScript and AI coding-agent assistance
- 29\. Cloud deployment and enterprise operations
- 30\. Comparing n8n, Make, Zapier, and Power Automate

Deliverable: An expanded enterprise solution with measurable business value and maintainable operations.

## 4. Lesson 01 starts with the product, not just Docker

Your first lesson will now establish the project foundation before building the workflow.

Step 1 — Define the business requirements

Document the business problem, users, request types, expected behavior, and acceptance criteria.

Step 2 — Create an isolated learning environment

Run n8n in its separate Docker container and volume. Keep Magento untouched.

Step 3 — Build the first product workflow

Create the initial request-intake workflow using a sample order-related request and validate its output.

Step 4 — Document and test

Record the workflow purpose, sample input, expected output, test result, and outstanding requirements.

### Project acceptance criteria

By the end of the roadmap, the product should demonstrate:

- Multiple business request types handled by a coherent workflow architecture.
- API and database integrations with appropriate validation.
- AI extraction and classification with structured outputs.
- Safe agent tool use and human approval for consequential actions.
- Error handling, retries, auditability, and monitoring.
- Security controls, repeatable tests, and deployment documentation.
- A professional README, architecture diagram, demonstration, and client handover guide.

We will measure progress through working features and evidence, not simply the number of lessons completed.

Next: Lesson 01 — Enterprise AI Commerce Operations Platform. We will define its requirements, establish the isolated environment, and build the first workflow. All subsequent lessons will extend this same product until it is ready to demonstrate as a serious portfolio project.