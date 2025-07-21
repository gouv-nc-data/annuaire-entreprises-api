import importlib.resources as pkg_resources
import json

import app.labels as labels_package

# List of module names to import
file_modules = [
    "codes-NAF",
    "forme-juridiques",
    "type-structures",
]


# Function to load JSON content from a module
def load_json_from_module(module_name: str):
    json_content = pkg_resources.read_text(labels_package, f"{module_name}.json")
    return json.loads(json_content)


# Load all JSON files into a dictionary
loaded_files = {
    module_name.upper(): load_json_from_module(module_name)
    for module_name in file_modules
}

# Accessing the data
FORME_JURIDIQUES = loaded_files["FORME-JURIDIQUES"]
CODES_NAF = loaded_files["CODES-NAF"]
TYPE_STRUCTURES = loaded_files["TYPE-STRUCTURES"]
