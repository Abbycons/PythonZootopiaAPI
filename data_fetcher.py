import os
from dotenv import load_dotenv # Import dotenv
import requests

# Load environment variables from .env
load_dotenv()

# Get API key from .env
api_key = os.getenv("API_KEY")

def fetch_animal_data(animal_name):
    """Fetch animal data from the API."""
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {"X-Api-Key": api_key} # Use API key from .env
    params = {"name": animal_name}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data if data else None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None