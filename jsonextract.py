import json
import re

def extract_json(llm_output: str):
    """Extracts and returns the JSON content from an LLM output string."""
    match = re.search(r'```json\n(.*?)\n```', llm_output, re.DOTALL)  # Regex to find JSON between ```json and ```
    if match:
        json_str = match.group(1)  # Extract the JSON string
        return json.loads(json_str)  # Convert string to dictionary
    else:
        raise ValueError("No valid JSON found in the input")
    
    
def get_json_value(data: dict, path: str):
    """Retrieve a value from a nested JSON using a dot-separated path, supporting lists.
    Example: Atr1.Atr2.0.Atr3"""
    keys = path.split(".")  # Split the path into individual keys
    value = data  # Start with the full JSON data

    try:
        for key in keys:
            if isinstance(value, list):  # If current value is a list
                key = int(key)  # Convert key to int (for list index)
            value = value[key]  # Traverse deeper
        return value
    except (KeyError, IndexError, ValueError, TypeError):
        return None  # Return None if the key path is invalid