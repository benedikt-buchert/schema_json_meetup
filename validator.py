import os
import json
import uuid
from jsonschema import validate, ValidationError

# Function to load JSON from a file


def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to add 'xdm:' prefix to top-level properties


def add_xdm_prefix(example_data):
    """Recursively adds 'xdm:' prefix to all keys, including nested dictionaries."""
    if isinstance(example_data, dict):
        prefixed_data = {}
        for key, value in example_data.items():
            # Recursively add the xdm: prefix to nested dictionaries
            prefixed_data[f'xdm:{key}'] = add_xdm_prefix(value)
        return prefixed_data
    elif isinstance(example_data, list):
        # If the value is a list, apply the prefixing to each dictionary in the list
        return [add_xdm_prefix(item) for item in example_data]
    else:
        # For non-dict and non-list values, return the value as is
        return example_data

# Function to add a unique ID field (xdm:id) to the example


def add_unique_id(example_data):
    unique_id = str(uuid.uuid4())  # Generate a UUID
    example_data['@id'] = unique_id
    return example_data

# Function to validate the example against the schema


def validate_schema(schema_name, data):
    # Construct file paths for the schema and example
    schema_file_path = os.path.join('schemas', f"{schema_name}.json")

    # Check if schema file exists
    if not os.path.exists(schema_file_path):
        print(f"Schema '{schema_name}' not found in the schemas folder.")
        return

    # Add 'xdm:' prefix to the properties in the example
    data = add_xdm_prefix(data)

    # Add a unique ID field to the example
    data = add_unique_id(data)

    schema = load_json(schema_file_path)

    # Validate the modified example against the schema
    try:
        validate(instance=data, schema=schema)
        print(f"Validation successful for example '{
            data['xdm:eventType']}' against schema '{schema_name}'.")
    except ValidationError as e:
        print(f"Validation failed: {e.message}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
