def add(x, y):
    """Adds two numbers together."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def divide(x, y):
    """Divides two numbers. Raises a ValueError for division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y