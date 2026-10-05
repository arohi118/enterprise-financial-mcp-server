import sqlparse

def is_safe_read_only(query: str) -> bool:
    """Verifies that the executed SQL statement performs only read operations."""
    parsed = sqlparse.parse(query)
    for statement in parsed:
        stmt_type = statement.get_type()
        if stmt_type not in ("SELECT", "SHOW", "DESCRIBE"):
            return False
    return True
