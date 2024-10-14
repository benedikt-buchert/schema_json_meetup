import os
import json
from aepp import schema
import aepp

# Import the configuration and connect to the instance
connection = aepp.importConfigFile('credentials.json', connectInstance=True)

# Create an instance of the Schema class
mySchemaInstance = schema.Schema(config=connection)

# Fetch all schemas
schemas = mySchemaInstance.getSchemas()

# Create a folder named 'schemas' if it doesn't exist
output_folder = 'schemas'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over the schemas, get the full schema, and write each schema to a separate file
for schema_data in schemas:
    # Extract the schema ID from the schema data
    schema_id = schema_data.get('$id')  # or use 'meta:altId' if preferred
    schema_title = schema_data.get('title', 'no_title').replace(' ', '_')

    if schema_id:
        # Fetch the full schema using the schema ID
        full_schema = mySchemaInstance.getSchema(schemaId=schema_id, full=True)

        # Generate the file name from the title or fallback to 'unknown_schema'
        filename = f"{schema_title}.json"

        # Write the full schema to a JSON file in the 'schemas' folder
        file_path = os.path.join(output_folder, filename)
        with open(file_path, 'w') as f:
            json.dump(full_schema, f, indent=4)
            print(f"Full schema for '{schema_title}' saved to {file_path}")
    else:
        print(f"Schema ID missing for title: {schema_title}")
