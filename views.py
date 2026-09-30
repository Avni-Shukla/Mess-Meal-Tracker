# views.py

def print_menu():
    print("\n===== Mess Meal Tracker =====")
    print("1. Add new meal entry")
    print("2. Show today's entry")
    print("3. Show all entries")
    print("4. Exit")
    print("==============================")


def print_message(msg: str):
    """Print a single-line message to the user."""
    print(msg)


def print_table(headers: list[str], rows: list[list]):
    """
    Print a simple ASCII table in the terminal.

    headers: list of column headers
    rows: list of rows, each row is a list of cell values
    """
    if not headers:
        return

    # Convert all cells to string and compute column widths
    str_rows = [[str(cell) for cell in row] for row in rows]
    col_widths = [len(h) for h in headers]

    for row in str_rows:
        for i, cell in enumerate(row):
            if i >= len(col_widths):
                break
            col_widths[i] = max(col_widths[i], len(cell))

    # Helper to format a row
    def format_row(cells):
        return " | ".join(
            cell.ljust(col_widths[i]) for i, cell in enumerate(cells)
        )

    # Print header
    print(format_row(headers))
    # Print separator
    separator = "-+-".join("-" * w for w in col_widths)
    print(separator)
    # Print rows
    for row in str_rows:
        # If some rows have fewer columns, pad with empty strings
        padded = row + [""] * (len(headers) - len(row))
        print(format_row(padded))