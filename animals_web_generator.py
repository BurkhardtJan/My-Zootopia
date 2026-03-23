import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
    if "name" in animal:
        print("Name: " + animal["name"])
    if "diet" in animal["characteristics"]:
        print("Diet: " + animal["characteristics"]["diet"])
    if "locations" in animal:
        print("Location: " + animal["locations"][0])
    if "type" in animal["characteristics"]:
        print("Type: " + animal["characteristics"]["type"])
    print()
