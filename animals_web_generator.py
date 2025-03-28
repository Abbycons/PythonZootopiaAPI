from data_fetcher import fetch_animal_data

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
            f"<div class='cards__item'>"
            f"<h2 class='card__title'>{animal['name']}</h2>"
            "<div class='card__text'>"
            f"<p><strong>Scientific Name:</strong> {animal['taxonomy']['scientific_name']}</p>"
            f"<p><strong>Habitat:</strong> {animal['characteristics'].get('habitat', 'Unknown')}</p>"
            f"<p><strong>Diet:</strong> {animal['characteristics'].get('diet', 'Unknown')}</p>"
            f"<p><strong>Top Speed:</strong> {animal['characteristics'].get('top_speed', 'Unknown')}</p>"
            
            "</div>"
            "</div>"
            for animal in animal_data
        ])

        with open("animals_template.html", "r") as file:
            template = file.read()

        html_content = template.replace('__REPLACE_ANIMALS_INFO__', animals_info)

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
