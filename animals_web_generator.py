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


def generate_html(animal_data, animal_name):
    """Generate an HTML file with animal information."""
    filename = "animals.html"

    if not animal_data:
        html_content = f"""
        <html>
        <head><title>Animal Not Found</title></head>
        <body>
            <h2>The animal "{animal_name}" doesn't exist.</h2>
        </body>
        </html>
        """
    else:
        animals_info = "".join([
            f"<h2>{animal['name']}</h2>"
            f"<p><strong>Scientific Name:</strong> {animal['taxonomy']['scientific_name']}</p>"
            f"<p><strong>Habitat:</strong> {animal['characteristics'].get('habitat', 'Unknown')}</p>"
            f"<p><strong>Diet:</strong> {animal['characteristics'].get('diet', 'Unknown')}</p>"
            f"<p><strong>Top Speed:</strong> {animal['characteristics'].get('top_speed', 'Unknown')}</p>"
            for animal in animal_data
        ])

        html_content = f"""
        <html>
        <head><title>Animal Information</title></head>
        <body>
            <h1>Results for "{animal_name}"</h1>
            {animals_info}
        </body>
        </html>
        """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"Website was successfully generated to the file {filename}.")


def main():
    """Main function to handle user input and generate the website."""
    animal_name = input("Enter a name of an animal: ").strip()

    if not animal_name:
        print("Animal name cannot be empty. Please try again.")
        return

    animal_data = fetch_animal_data(animal_name)
    generate_html(animal_data, animal_name)


if __name__ == "__main__":
    main()
