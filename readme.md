## What is XDM

# XDM UI

- [UI](https://experience.adobe.com/#/@mohrstadeemeaptrsdb/sname:prod/platform/schema/browse?initialLoad=false&limit=50&page=1&sortDescending=1&sortField=lastModifiedDate)

# Schema API

- [Documentation](https://developer.adobe.com/experience-platform-apis/references/schema-registry/)
- [Python Wrapper](https://github.com/adobe/aepp)
- [Example in get_schemas.py](./get_schemas.py)

## What is JSON Schema

- [Schema Website](https://json-schema.org/)

## Tooling for Schema Json

- [Tools](https://json-schema.org/tools?query=&sortBy=name&sortOrder=ascending&groupBy=toolingTypes&licenses=&languages=&drafts=&toolingTypes=&environments=)
- [Validator](https://github.com/python-jsonschema/jsonschema)

## Validating Schema JSON

- For example we can extract the xdm [here](https://adobestore.com/-Escape-artist-tee-Art-by-Sam-Wilde-P1346.aspx)
- Paste it into the `./examples` folder.
- [Validator Script](./validator.py)
- Adjust validator to read the new file.
- [Example in example.py](./example.py)

```PYTHON
# Example usage
schema_name = "exampleSchema"  # Name of the schema (without .json extension)
example_file = "example.json"  # Example JSON file
validate_schema(schema_name, example_file)
```

- [Selenium script](./sel.py) to automate the process.
