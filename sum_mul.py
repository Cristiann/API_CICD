import json

def calculate_from_json(json_data):
    """
    Recibe un JSON con 3 etiquetas de números y retorna la suma de los dos
    primeros multiplicada por el tercero.
    
    Args:
        json_data (str): String con formato JSON que contiene 3 etiquetas numéricas
        
    Returns:
        float: Resultado de (num1 + num2) * num3
    """
    try:
        # Parsear el JSON a un diccionario Python
        data = json.loads(json_data)
        
        # Verificar que el JSON contiene exactamente 3 etiquetas
        if len(data) != 3:
            raise ValueError("El JSON debe contener exactamente 3 etiquetas")
        
        # Verificar que el JSON contiene las etiquetas requeridas
        if "num1" not in data or "num2" not in data or "num3" not in data:
            raise ValueError("El JSON debe contener las etiquetas 'num1', 'num2' y 'num3'")
        
        # Extraer los valores numéricos usando las etiquetas específicas
        num1 = data["num1"]
        num2 = data["num2"]
        num3 = data["num3"]
        
        # Verificar que todos los valores son números
        for val in [num1, num2, num3]:
            if not isinstance(val, (int, float)):
                raise ValueError("Todos los valores deben ser números")
        
        # Realizar el cálculo: (num1 + num2) * num3
        result = (num1 + num2) * num3
        
        return result
    
    except json.JSONDecodeError:
        raise ValueError("El formato del JSON no es válido")
    except Exception as e:
        raise ValueError(f"Error al procesar el JSON: {str(e)}")
