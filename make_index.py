import json

# File paths
input_file_path = '../fodmap4all/assets/packs/default/en/ing.json'
output_file_path = 'en.json'

# Load JSON data from the file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    json_data = json.load(input_file)

# Convert JSON array to dictionary with 'id' as key and 'name' as value
dictionary = {item['id']: item['name'] for item in json_data}

# Save the resulting dictionary to an output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(dictionary, output_file, indent=2)

print(f"Dictionary saved successfully to {output_file_path}!")
