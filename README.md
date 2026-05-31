# 🧠 ReAct Agent From Scratch

A lightweight implementation of a ReAct (Reason + Act) Agent built from scratch using Python and Groq LLM.

The goal of this project was not to build a production-ready framework, but to understand the internal working of AI agents by implementing the core ReAct loop ourselves.

---

## 🎯 Project Goal

Understand how modern AI agents:

- Reason about a user's query
- Decide when to use tools
- Execute external functions
- Observe results
- Continue reasoning until a final answer is produced

Instead of using frameworks like LangChain or CrewAI, everything was implemented manually to learn the underlying concepts.

---

## 🏗️ Architecture

```text
User Query
    │
    ▼
Prompt Builder
    │
    ▼
LLM (Groq)
    │
    ▼
JSON Output
    │
    ▼
Parser
    │
    ▼
Tool Router
    │
    ▼
Tool Execution
    │
    ▼
Observation
    │
    ▼
LLM
    │
    ▼
Final Answer
```

---

## 📂 Project Structure

```text
react_agent/
│
├── app/
│   ├── agent/
│   │   ├── react_loop.py
│   │   ├── parser.py
│   │   └── prompt_builder.py
│   │
│   ├── llm/
│   │   └── client.py
│   │
│   └── tools/
│       ├── calculator.py
│       
│      
│
├── .env
├── main.py
├── README.md
└── pyproject.toml
```

---

## 🚀 Features

- ReAct reasoning loop
- Tool calling support
- Groq LLM integration
- Structured JSON communication
- Multi-step reasoning
- Execution tracing through logs
- Extensible tool registry

---

## 🛠️ Tools Implemented

### Calculator Tool

Supports:

- Addition
- Subtraction
- Multiplication
- Division


## 🔄 ReAct Loop Example

### User Query

```text
What is 10 / 5 and 10 * 5?
```

### Step 1

LLM decides:

```json
{
  "action": "calculator",
  "input": "{\"operation\":\"divide\",\"a\":10,\"b\":5}"
}
```

Tool executes:

```text
2.0
```

---

### Step 2

LLM decides:

```json
{
  "action": "calculator",
  "input": "{\"operation\":\"multiply\",\"a\":10,\"b\":5}"
}
```

Tool executes:

```text
50.0
```

---

### Step 3

LLM returns:

```json
{
  "action": "final",
  "answer": "10 / 5 = 2.0, 10 * 5 = 50.0"
}
```

---

## ⚠️ Challenge Faced: Parsing Errors

One of the biggest challenges was ensuring reliable communication between the LLM and the tool execution layer.

Initially, the model sometimes generated:

```text
The answer is 15.

{
   ...
}
```

or

```text
Use calculator tool to add numbers.
```

instead of valid JSON.

This caused:

- JSON parsing failures
- Broken execution flow
- Inconsistent tool invocation

---

## ✅ Solution

To solve this, a strict output contract was introduced.

The model was instructed to respond **only in JSON**.

### Tool Call Format

```json
{
  "action": "calculator",
  "input": "{\"operation\":\"add\",\"a\":10,\"b\":5}"
}
```

### Final Response Format

```json
{
  "action": "final",
  "answer": "15"
}
```

A parser layer validates the response before execution.

This significantly improved reliability and reduced malformed outputs.

---

## 🧠 Hallucination Control

A common issue with LLMs is hallucination—generating answers directly instead of using available tools.

To reduce this:

### 1. Strict Prompting

The model is instructed to:

```text
Use tools whenever required.
Do not answer from your own knowledge.
Respond only in JSON.
```

### 2. Tool-Based Execution

Mathematical calculations are performed by Python functions instead of relying on the model's internal reasoning.

This makes results deterministic and verifiable.

### 3. Structured Parsing

Only approved actions are executed.

Any invalid output is rejected by the parser.

---

## 📚 Key Learnings

Through this project I learned:

- How ReAct agents work internally
- Prompt engineering for structured outputs
- Tool calling architecture
- Agent execution loops
- JSON parsing and validation
- Hallucination mitigation techniques
- Separation of reasoning and execution

---

## 🧪 Tech Stack

- Python
- Groq API
- JSON
- Custom ReAct Architecture

---

## 💡 Takeaway

The most important lesson from this project:

> An AI agent is not just an LLM. It is a system where the LLM acts as a decision-maker while external tools perform reliable execution.

Building the ReAct loop from scratch provided a much deeper understanding than simply using an existing agent framework.
