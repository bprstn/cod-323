# Brian Preston
# Module 9 - API Tutorial
# This program connects to the Game of Thrones API at https://anapioficeandfire.com/api/characters/583.
# It fetches details about the character Jon Snow and prints both the raw and formatted responses.

import requests
import json

# Define the API URL for Jon Snow
url = "https://anapioficeandfire.com/api/characters/583"

def connect_to_api():
    try:
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Successfully connected to the API!")
            
            # Print the raw JSON response
            print("\nRaw Response (No Formatting):")
            print(response.text)  # Unformatted raw response
            
            # Print the formatted JSON response
            print("\nFormatted Response:")
            data = response.json()  # Parse JSON response
            print(json.dumps(data, indent=4))  # Pretty-print JSON
            
        else:
            print(f"Failed to connect. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    connect_to_api()
