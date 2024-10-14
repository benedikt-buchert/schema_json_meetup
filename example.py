import os
from validator import validate_schema, load_json


def load_example(example_file_path):
    example_file_path = os.path.join('examples', example_file)
    # Check if example file exists
    if not os.path.exists(example_file_path):
        print(f"Example '{example_file}' not found in the examples folder.")
        return
    example = load_json(example_file_path)
    return example


# Example usage
schema_name = "webSDKevent"  # Name of the schema (without .json extension)
example_file = "test.json"  # Example JSON file
validate_schema(schema_name, load_example(example_file))
