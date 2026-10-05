# Enterprise Financial MCP Server

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![MCP Protocol](https://img.shields.io/badge/protocol-Model%20Context%20Protocol-green.svg)](https://modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready **Model Context Protocol (MCP)** server built in Python that exposes relational financial databases and internal banking REST APIs to LLM agents with strict security guardrails[cite: 1].

Designed for enterprise banking and asset management contexts, this server enforces **AST-based SQL mutation blocking**, schema-aware context injection, and paginated data extraction to safeguard enterprise ledgers while preventing token window exhaustion[cite: 1].

---

## 🏗️ Architecture Overview
