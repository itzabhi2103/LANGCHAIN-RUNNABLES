#Understanding Runnables in LangChain
This repository/project explores the concept of Runnables in LangChain, a key architectural change introduced to standardize how components interact and form chains.

Table of Contents
Introduction
The Problem
What are Runnables?
Key Concepts
Code Demo
Introduction
In the evolution of LangChain, the team identified that managing manual chains for every specific use case created a massive, unmaintainable codebase. Runnables solve this by providing a unified, standardized interface for all components.

The Problem
Initially, components like LLMs, Prompt Templates, and Retrievers were not standardized (30:02). Different methods like predict, format, and get_relevant_documents were required to interact with them, forcing developers to write complex, custom wrapper functions to chain them together (31:00 - 32:40).

What are Runnables?
Runnables are units of work that follow a common interface, allowing them to be plugged together like Lego blocks (33:44 - 36:44). Key characteristics include:

Standardized Interface: Every runnable features a common set of methods, most notably invoke().
Composability: Outputs from one runnable can be piped as inputs to the next.
Abstraction: Complex workflows built from multiple runnables are themselves runnables, enabling infinitely nestable chains.
Key Concepts
invoke(): The primary method used to process input and return an output (35:00).
batch(): Used for processing multiple inputs simultaneously (35:13).
stream(): Used for streaming output from models (35:25).
Code Demo
This project includes a step-by-step implementation from scratch:

Dummy Components: Building mock LLM and Prompt classes (40:00).
Standardization: Using abstract base classes to force an invoke method across components (55:00).
Chain Logic: Creating a RunnableConnector to loop through steps and pass data dynamically (1:02:00).
Resources: CampusX GitHub | Colab Notebooks




