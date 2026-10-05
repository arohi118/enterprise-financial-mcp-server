import os
import psycopg2
from psycopg2.extras import RealDictCursor
from mcp.server.fastmcp import FastMCP
from app.security.sql_guard import is_safe_read_only

mcp = FastMCP("Enterprise-Financial-MCP-Server")

DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/finance_db")

@mcp.tool()
def get_financial_schema() -> str:
    """Discovers available tables, columns, and data types in the financial database."""
    query = """
        SELECT table_name, column_name, data_type 
        FROM information_schema.columns 
        WHERE table_schema = 'public'
        ORDER BY table_name, ordinal_position;
    """
    with psycopg2.connect(DB_URL) as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query)
            return str(cur.fetchall())

@mcp.tool()
def run_financial_query(sql_query: str) -> str:
    """
    Executes a read-only SQL query against the financial ledger.
    Mutating statements are rejected to maintain enterprise compliance.
    """
    if not is_safe_read_only(sql_query):
        return "SecurityViolationError: Only read-only SELECT queries are allowed."

    try:
        with psycopg2.connect(DB_URL) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(sql_query)
                rows = cur.fetchmany(50)  # Constrain output for context-window efficiency
                return str(rows)
    except Exception as exc:
        return f"DatabaseError: {str(exc)}"

if __name__ == "__main__":
    mcp.run()
