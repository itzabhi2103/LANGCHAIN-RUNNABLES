# Understanding Runnables in LangChain

This project explores the concept of **Runnables** in LangChain, a foundational architectural improvement that standardizes how different components interact and form chains.

## 📚 Table of Contents

* Introduction
* The Problem
* What are Runnables?
* Key Features
* Core Methods
* Implementation Walkthrough
* Resources

---

## 🚀 Introduction

As LangChain evolved, developers faced increasing complexity when connecting various components such as LLMs, Prompt Templates, Output Parsers, and Retrievers.

To address this challenge, LangChain introduced **Runnables**, a unified interface that enables seamless composition of different components while reducing code complexity and improving maintainability.

---

## ❌ The Problem

In earlier versions of LangChain, different components exposed different methods:

| Component       | Method                     |
| --------------- | -------------------------- |
| LLM             | `predict()`                |
| Prompt Template | `format()`                 |
| Retriever       | `get_relevant_documents()` |

Because each component had its own interface, developers had to write custom wrapper logic to connect them together.

### Challenges

* No standard communication protocol between components.
* Complex chain-building process.
* Increased maintenance overhead.
* Difficult to scale applications.

---

## ✅ What are Runnables?

A **Runnable** is a unit of work that follows a common interface.

Every Runnable accepts an input, performs an operation, and returns an output using standardized methods.

This allows developers to combine components like building blocks.

### Key Characteristics

### 1. Standardized Interface

Every Runnable exposes the same core methods.

```python
runnable.invoke(input)
```

### 2. Composability

Outputs from one Runnable can be directly passed as inputs to another.

```python
prompt | llm | parser
```

### 3. Abstraction

A chain made from multiple Runnables is itself a Runnable.

This enables nested workflows and reusable pipelines.

---

## 🔑 Core Methods

### invoke()

Processes a single input and returns a single output.

```python
result = runnable.invoke("Hello")
```

---

### batch()

Processes multiple inputs simultaneously.

```python
results = runnable.batch([
    "Input 1",
    "Input 2",
    "Input 3"
])
```

---

### stream()

Streams output incrementally as it is generated.

```python
for chunk in runnable.stream("Tell me a story"):
    print(chunk)
```

---

## 🛠 Implementation Walkthrough

This project demonstrates how Runnables work internally by implementing them from scratch.

### Step 1: Create Dummy Components

Build mock versions of:

* LLM
* Prompt Template

Example:

```python
class DummyPrompt:
    def invoke(self, topic):
        return f"Tell me about {topic}"
```

---

### Step 2: Standardize Components

Use Abstract Base Classes (ABC) to enforce the Runnable interface.

```python
from abc import ABC, abstractmethod

class Runnable(ABC):

    @abstractmethod
    def invoke(self, input):
        pass
```

This guarantees that every component implements the `invoke()` method.

---

### Step 3: Build a Runnable Connector

Create a chain mechanism that dynamically passes outputs between components.

```python
class RunnableConnector:

    def __init__(self, steps):
        self.steps = steps

    def invoke(self, input):
        result = input

        for step in self.steps:
            result = step.invoke(result)

        return result
```

---

### Example Flow

```text
Input
  ↓
Prompt Template
  ↓
LLM
  ↓
Output Parser
  ↓
Final Output
```

Since each component follows the same interface, they can be connected effortlessly.

---

## 🎯 Benefits of Runnables

* Consistent API across components
* Easier chain creation
* Better scalability
* Improved maintainability
* Supports nesting and composition
* Enables advanced workflows such as LangGraph

---

## 📖 Resources

* CampusX LangChain Lecture
* LangChain Documentation
* CampusX GitHub Repository
* Google Colab Notebooks

---

## 🏁 Conclusion

Runnables represent one of the most important architectural improvements in LangChain. By introducing a standardized interface through methods like `invoke()`, `batch()`, and `stream()`, LangChain enables developers to create scalable, modular, and maintainable AI applications with significantly less boilerplate code.

Understanding Runnables is essential for mastering modern LangChain development.
