def apply_operation(base_value, num3, operation):
    """
    Aplica la operación especificada entre base_value y num3.
    
    Args:
        base_value (float): El resultado de (num1 + num2).
        num3 (float): El número sobre el que se aplicará la operación.
        operation (str): Operación a realizar ('multiplication', 'addition', 'subtraction', 'division').
    
    Returns:
        float: Resultado de la operación aplicada.
    """
    if operation == "multiplication":
        return base_value * num3
    elif operation == "addition":
        return base_value + num3
    elif operation == "subtraction":
        return base_value - num3
    elif operation == "division":
        if num3 == 0:
            raise ValueError("No se puede dividir por cero")
        return base_value / num3
    else:
        raise ValueError(f"Operación no válida: {operation}")
