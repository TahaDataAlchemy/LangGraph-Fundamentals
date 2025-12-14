# LangGraph – Notes 

> 🚧 **Work in Progress**
>
> - This README will be updated **daily / weekly**
> - New concepts, patterns, and learnings will be added over time
> - Notes are intentionally **short and point-based**

---

## What is LangGraph?

LangGraph is an **orchestration framework** for building **stateful, parallelism, multi-step, and multi-agent AI workflows**.

- Models logic as a **graph (nodes + edges)**
- Designed for **production-grade** AI systems
- Handles state, branching, retries, pauses, and resume

---

## Why LangGraph (vs LangChain)

### 1. Complex Workflows
- Native support for **branching, conditions, loops, jumps, parallel paths**

### 2. State Management
- **Single shared state** across all nodes
- No manual memory passing between steps

### 3. Event-Driven Execution
- Graphs can **start or resume on events**

### 4. Fault Tolerance / Resume
- If execution fails, workflow can **resume from last successful node**

### 5. Human-in-the-Loop
- Built-in support to **pause execution**
- Waits for human input (minutes / hours / days)
- Resumes with the same state

### 6. Subgraphs
- A **graph can be used as a node**
- Reusable and composable

### 7. Nested & Multi-Agent Workflows
- Easy planner → executor → reviewer patterns
- Multi-agent systems using subgraphs

### 8. Observability
- Runtime visibility of **each node execution**
- Easier debugging and monitoring

### 9. LangSmith Integration
- First-class LangSmith support
- Full tracing of graph, nodes, state, and pauses

---

## Core Concepts (Short Notes)

### Node
- Smallest unit of work
- Reads state → updates state

### State
- Shared object across all nodes
- Automatically persisted

### Edge
- Controls flow between nodes
- Can be conditional or looping

### Entry Point
- Where execution starts

### End
- Marks workflow completion

### Checkpointing
- State saved after every node
- Enables resume after failure

### Subgraph
- Graph inside another graph


## 1. Workflow

A **workflow** is a **series of tasks** executed in a defined order to achieve a goal.

- Tasks may depend on each other
- Can be simple or complex
- Not LLM-specific

---

## 2. LLM Workflow

An **LLM workflow** is a workflow where **LLMs are involved in one or more steps**.

It may include:
- Prompting
- Reasoning
- Tool calling
- Memory access
- Decision making

Characteristics:
- Can be **linear**
- Can be **branched**
- Can include **loops & retries**
- Can support **multi-agent communication**
- Can route between different LLMs or sub-workflows

---

## 3. Prompt Chaining

**Prompt chaining** means calling **multiple LLM nodes in sequence**, where the output of one LLM becomes the input of the next.

Used when:
- Task is complex
- Task can be broken into smaller steps
- Validation or checks are needed between steps

### Example
Goal: Generate a report

1. LLM 1 → Generate report outline  
2. LLM 2 → Write report using the outline  
3. Validation step →  
   - If report > 5000 words → stop or modify  
   - Else → continue

This pattern is called **Prompt Chaining**.

---

## 4. Routing

**Routing** means forwarding work to the **correct LLM or workflow** based on user intent.

### Example
System has 3 workflows:
- Sales information
- Platform information
- Orders information

Flow:
1. User sends a query
2. Intent analyzer LLM classifies the query
3. Query is routed to the relevant workflow
4. Workflow executes and returns response

Routing helps:
- Scale systems
- Keep logic clean
- Avoid unnecessary LLM calls

---

## 5. Parallelism

**Parallelism** means breaking a task into **independent subtasks** and executing them **at the same time**.

Used when:
- Tasks do NOT depend on each other
- Faster execution is needed

### Example: Content Moderation

Goal: Check if content is appropriate

Subtasks (run in parallel):
- Community guidelines check
- Misinformation check
- Sexual content check

Flow:
1. All checks run simultaneously
2. Results are sent to a decider
3. Decider determines if content is acceptable

---

## 6. Orchestrator Workflow

An **Orchestrator Workflow** dynamically decides:
- Which LLMs to use
- Which tasks to run
- What to execute in parallel

Difference from Parallelism:
- In **parallelism**, tasks are predefined
- In **orchestration**, the system decides tasks at runtime

### Example
1. User submits a query
2. Orchestrator analyzes the query
3. Assigns tasks to suitable LLMs or agents
4. Tasks run in parallel
5. Results are combined and returned
