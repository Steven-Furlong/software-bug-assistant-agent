# Software Bug Assistant

## Background & Scenario
In modern technical operations, support engineers and project managers waste valuable time manually going through internal databases, tracking software bugs, and cross-referencing system logs. This project simulates a real-world scenario for a robotics/prosthetics manufacturer. The objective is to transition artificial intelligence from a passive text-generator into an active technical assistant capable of solving problems. By leveraging Google's Agent Development Kit (ADK), this assistant is equipped with specialized tools to query databases, perform external searches, and triage software bugs directly on behalf of support staff.

## What This Project Does
This project implements an intelligence, tool-enabled AI agent using a basic ADK agent (Gemini Flash 2.5). Instead of offering just general advice, the agent uses structured reasoning-and-acting (ReAct) loops to dynamically select and execute tools when prompted by a user.

## Key Capabilities
* Automated Bug Triage: Analyzes incoming user reports regarding hardware/software malfunctions in prosthetic arms.
* Dynamic Tool Selection: Automatically determines which tool to invoke based on context (e.g. searching documentation, querying issue databases, or fetching system details).
* Interactive Development UI: Integrated with the ADK local web server ('adk web') for real-time testing, debugging, and chat evaluation.

## Key Concepts Explored
* Setting up a Python project for ADK development.
* Creating a basic ADK agent.
* Implementing and using Function Tools.
* Integrating Built-in Tools like Google Search.
* Leveraging Third-Party Tools from frameworks like LangChain within ADK.
* Using MCP Tools to interact with databases (Cloud SQL) and APIs.


## Tech Stack
* Core Framework: Google Agent Development Kit (ADK)
* Language Model: Gemini 2.5 Flash
* Language: Python 3
* Environment Management: 'uv' / Python Virtual Environments
