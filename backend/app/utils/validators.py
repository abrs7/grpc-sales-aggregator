from __future__ import annotations
from datetime import datetime

def is_valid_date_iso(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_row(fields: list[str]) -> tuple[bool, str]:
    """Expect [Department, Date, NumberOfSales]"""
    if len(fields) != 3:
        return False, "Row must have exactly 3 columns"
    dept, date_str, sales_str = fields
    if not dept.strip():
        return False, "Department name must not be empty"
    if not is_valid_date_iso(date_str.strip()):
        return False, "Date must be ISO YYYY-MM-DD"
    try:
        sales = int(sales_str.strip())
    except ValueError:
        return False, "Number of Sales must be integer"
    if sales < 0:
        return False, "Number of Sales must be non-negative"
    return True, ""
