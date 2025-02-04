# Utility functions can go here, like validation for math expressions, etc.

# Example: Validate that the math expression entered is safe
def is_valid_expression(expression):
    allowed_chars = set("0123456789+-*/()")
    return all(char in allowed_chars for char in expression)
