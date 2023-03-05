import json

# Load the input JSON
with open('data.json') as f:
    data = json.load(f)

# Create the output dictionary
output = {'name': data['name'], 'children': []}

# Loop through each category
for category in data['children']:
    # Create a dictionary for the category
    category_dict = {'name': category['name'], 'children': []}

    # Loop through each module in the category
    for module in category['children']:
        # Create a dictionary for the module
        module_dict = {'name': module['name'], 'children': []}

        # Loop through each impact category in the module
        for impact in module['children']:
            # Create a dictionary for the impact category
            impact_dict = {'name': impact['name'], 'value': impact['value']}

            # Add the impact category to the module
            module_dict['children'].append(impact_dict)

        # Add the module to the category
        category_dict['children'].append(module_dict)

    # Add the category to the output
    output['children'].append(category_dict)

# Save the output JSON
with open('output.json', 'w') as f:
    json.dump(output, f, indent=2)
