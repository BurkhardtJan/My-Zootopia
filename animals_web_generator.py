import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_data["name"]}</div>\n'
    output += '<p class="card__text">'
    output += '<ul>'
    if "diet" in animal_data["characteristics"]:
        output += f"<li><strong>Diet:</strong> {animal_data['characteristics']['diet']}</li>\n"
    if "locations" in animal_data:
        output += f"<li><strong>Location</strong>: {animal_data['locations'][0]}</li>\n"
    if "type" in animal_data["characteristics"]:
        output += f"<li><strong>Type</strong>: {animal_data['characteristics']['type']}</li>\n"
    output += '</ul>'
    output += '</p>'
    output += '</li>'
    return output


animals_data = load_data('animals_data.json')
output = ''
for animal_data in animals_data:
    output += serialize_animal(animals_data)
print(output)

with open("animals_template.html", "r") as website:
    template = website.read()
html_with_animals = template.replace("__REPLACE_ANIMALS_INFO__", output)
print(html_with_animals)


with open("animals.html", "w") as website:
    website.write(html_with_animals)
