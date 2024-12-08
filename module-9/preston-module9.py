# Brian Preston
# Module 9 - API Tutorial
# This program connects to the Open Notify API at http://api.open-notify.org/astros.json.
# It fetches data about the astronauts currently in space and displays their names
# and the spacecraft they are aboard.

import requests

# Define the correct API URL
url = "http://api.open-notify.org/astros.json"

def connect_to_api():
    try:
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Successfully connected to the API!")
            print("Astronaut Data:")
            
            # Parse the JSON response
            data = response.json()
            print(f"Number of people in space: {data['number']}")
            for person in data['people']:
                print(f"{person['name']} is aboard {person['craft']}")
        else:
            print(f"Failed to connect. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    connect_to_api()
