import json
from operations import apply_operation

def calculate_from_json(json_data):
    """
    Receives a JSON string with three numerical values and an optional operation.
    Returns the result of applying the specified operation on the sum of the first two numbers with the third number.

    Args:
        json_data (str): A JSON-formatted string containing three numerical keys and an optional 'operation' key.

    Returns:
        float: The result of (num1 + num2) operated with num3 based on the 'operation' key.
    """
    try:
        # Parse the JSON string into a Python dictionary
        data = json.loads(json_data)
        
        # Ensure the required numerical keys exist
        required_keys = {"num1", "num2", "num3"}
        if not required_keys.issubset(data.keys()):
            raise ValueError("The JSON must contain the keys 'num1', 'num2', and 'num3'")

        # Extract numerical values
        num1 = data["num1"]
        num2 = data["num2"]
        num3 = data["num3"]

        # Validate that all values are numbers
        for val in [num1, num2, num3]:
            if not isinstance(val, (int, float)):
                raise ValueError("All values must be numeric (int or float)")

        # Perform the initial sum operation
        result = num1 + num2

        # Check if an operation is specified; default to 'multiplication'
        operation = data.get("operation", "multiplication")
        result = apply_operation(result, num3, operation)

        return result
    
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    except Exception as e:
        raise ValueError(f"Error processing JSON: {str(e)}")
