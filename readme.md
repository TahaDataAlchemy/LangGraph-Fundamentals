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

