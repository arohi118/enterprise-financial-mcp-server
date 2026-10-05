# Enterprise Financial MCP Server

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![MCP Protocol](https://img.shields.io/badge/protocol-Model%20Context%20Protocol-green.svg)](https://modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready **Model Context Protocol (MCP)** server built in Python that exposes relational financial databases and internal banking REST APIs to LLM agents with strict security guardrails[cite: 1].

Designed for enterprise banking and asset management contexts, this server enforces **AST-based SQL mutation blocking**, schema-aware context injection, and paginated data extraction to safeguard enterprise ledgers while preventing token window exhaustion.

---

## 🏗️ Architecture Overview
                  ┌──────────────────────────────────────┐
                  │    LLM Agent / MCP Host Client       │
                  │  (Claude Desktop, Cursor, LangChain) │
                  └──────────────────┬───────────────────┘
                                     │ JSON-RPC / Stdio / SSE
                                     ▼
                  ┌──────────────────────────────────────┐
                  │    Enterprise Financial MCP Server   │
                  │   (FastMCP Framework / Python 3.11)  │
                  └──────┬────────────────────────┬──────┘
                         │                        │
         1. Schema Discovery                      │ 2. Safe Query Execution
                         ▼                        ▼
           ┌────────────────────────┐  ┌────────────────────────┐
           │   Schema Reflection    │  │   SQL Security Guard   │
           │  - Table Metadata      │  │  - AST Validation      │
           │  - Type Definitions    │  │  - Mutation Blocking   │
           └────────────────────────┘  └───────────┬────────────┘
                                                   │ Approved SELECTs Only
                                                   ▼
                                     ┌───────────────────────────┐
                                     │    PostgreSQL Database    │
                                     │ (Financial Ledgers & Data)│
                                     └───────────────────────────┘

---

## ✨ Key Features

- **Schema-Aware Context Discovery:** Exposes database schema and column metadata as MCP resources, allowing LLM agents to construct precise, valid SQL queries without guesswork.
- **AST-Based SQL Guardrails:** Uses `sqlparse` to analyze the query syntax tree, rejecting non-read-only queries (`INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`) before they reach the database.
- **Context-Window Safe:** Enforces strict server-side row limits and pagination to prevent oversized context injections into downstream LLMs.
- **Containerized & Production-Ready:** Packaged with multi-stage Docker builds and Docker Compose for fast local development and cloud deployments[cite: 1].

---

## 🛠️ Tech Stack

- **Language:** Python 3.11+[cite: 1]
- **Protocol:** Model Context Protocol (MCP) SDK / FastMCP[cite: 1]
- **Database Driver:** `psycopg2-binary`[cite: 1]
- **SQL Parsing & Security:** `sqlparse`[cite: 1]
- **Containerization:** Docker, Docker Compose[cite: 1]

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.11+ installed[cite: 1]
- Docker and Docker Compose installed[cite: 1]

### 2. Clone and Setup Environment

```bash
git clone [https://github.com/arohi118/enterprise-financial-mcp-server.git](https://github.com/arohi118/enterprise-financial-mcp-server.git)
cd enterprise-financial-mcp-server

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

3. Spin Up Local Services (PostgreSQL)
Bash
docker compose up -d
4. Run the MCP Server
Bash
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/finance_db"
python -m app.server
🔌 Connecting to Claude Desktop / Cursor
Add the server configuration to your claude_desktop_config.json:

JSON
{
  "mcpServers": {
    "enterprise-financial-mcp": {
      "command": "python",
      "args": [
        "-m",
        "app.server"
      ],
      "cwd": "/path/to/enterprise-financial-mcp-server",
      "env": {
        "DATABASE_URL": "postgresql://postgres:postgres@localhost:5432/finance_db"
      }
    }
  }
}
🔒 Security Compliance
This server enforces strict compliance measures designed for regulated financial institutions[cite: 1]:

Parameterized/Read-Only Execution: Only SELECT, SHOW, and DESCRIBE statement types are processed. Any transaction mutation attempts return an immediate SecurityViolationError[cite: 1].

Access Scoping: Database credentials used by the MCP server should be bounded to a restricted read-only role with access to required schemas only[cite: 1].

👤 Author
Arohi Rup

LinkedIn: linkedin.com/in/arohirup

GitHub: @arohi118


