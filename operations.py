def apply_operation(base_value, num3, operation):
    """
    Applies the specified operation between base_value and num3.

    Args:
        base_value (float): The sum of num1 and num2.
        num3 (float): The number to be used in the operation.
        operation (str): The operation to be performed ('multiplication', 'addition', 'subtraction', 'division').

    Returns:
        float: The result of applying the operation.

    Raises:
        ValueError: If an invalid operation is provided or if division by zero occurs.
    """
    if operation == "multiplication":
        return base_value * num3
    elif operation == "addition":
        return base_value + num3
    elif operation == "subtraction":
        return base_value - num3
    elif operation == "division":
        if num3 == 0:
            raise ValueError("Division by zero is not allowed")
        return base_value / num3
    else:
        raise ValueError(f"Invalid operation: {operation}")
