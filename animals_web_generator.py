import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')
output = ''


for animal_data in animals_data:
    output += '<li class="cards__item">'
    if "name" in animal_data:
        output += f"Name: {animal_data['name']}<br/>\n"
    if "diet" in animal_data["characteristics"]:
        output += f"Diet: {animal_data['characteristics']['diet']}<br/>\n"
    if "locations" in animal_data:
        output += f"Location: {animal_data['locations'][0]}<br/>\n"
    if "type" in animal_data["characteristics"]:
        output += f"Type: {animal_data['characteristics']['type']}<br/>\n"
    output += '</li>'
print(output)


with open("animals_template.html", "r") as website:
    template = website.read()
html_with_animals = template.replace("__REPLACE_ANIMALS_INFO__", output)
print(html_with_animals)


with open("animals.html", "w") as website:
    website.write(html_with_animals)
