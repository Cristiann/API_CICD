import json
from operations import apply_operation

def calculate_from_json(json_data):
    """
    Recibe un JSON con 3 etiquetas de números y una operación opcional, 
    retorna el resultado de la operación especificada en el tercer número.
    
    Args:
        json_data (str): String con formato JSON que contiene 3 etiquetas numéricas y una operación opcional.
        
    Returns:
        float: Resultado de la operación (num1 + num2) con num3 según 'operation'.
    """
    try:
        # Parsear el JSON a un diccionario Python
        data = json.loads(json_data)
        
        # Verificar que el JSON contiene al menos las etiquetas numéricas necesarias
        required_keys = {"num1", "num2", "num3"}
        if not required_keys.issubset(data.keys()):
            raise ValueError("El JSON debe contener las etiquetas 'num1', 'num2' y 'num3'")
        
        # Extraer los valores numéricos
        num1 = data["num1"]
        num2 = data["num2"]
        num3 = data["num3"]
        
        # Verificar que todos los valores son números
        for val in [num1, num2, num3]:
            if not isinstance(val, (int, float)):
                raise ValueError("Todos los valores deben ser números")
        
        # Realizar la suma inicial
        result = num1 + num2
        
        # Verificar si existe la llave 'operation' y aplicarla
        operation = data.get("operation", "multiplication")  # Por defecto multiplicación
        result = apply_operation(result, num3, operation)
        
        return result
    
    except json.JSONDecodeError:
        raise ValueError("El formato del JSON no es válido")
    except Exception as e:
        raise ValueError(f"Error al procesar el JSON: {str(e)}")
