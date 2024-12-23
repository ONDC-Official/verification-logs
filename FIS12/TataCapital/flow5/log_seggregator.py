import json

# Function to read the input JSON file and save the payload keys as individual files


def save_payload_keys(input_file):
    # Read the JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Extract the payload object
    payload = data.get('payload', {})

    # Iterate through each key-value pair in the payload
    for key, value in payload.items():
        # Define the filename as the key with a .json extension
        filename = f"{key}.json"

        # Save the value as a JSON file
        with open(filename, 'w') as outfile:
            json.dump(value, outfile, indent=4)
        print(f"Saved {filename}")


# Specify the input JSON file
input_file = 'flow5.json'

# Call the function to save the payload keys as individual files
save_payload_keys(input_file)
