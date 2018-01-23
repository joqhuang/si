import requests
import json

species_names = {"https://swapi.co/api/species/1/":"Human","https://swapi.co/api/species/2/":"Droid"}

class Character:
    def __init__(self, name="Luke Skywalker", species="Human", json_dict=None):
        if json_dict is None:
            self.name = name
            self.species = species
        else:
            self.name = json_dict["name"]
            species_url = json_dict["species"][0]
            if species_url in species_names:
                self.species = species_names[species_url]
            else:
                self.species = "Other"

    def __str__(self):
        return self.name + " is a " + self.species

class Human(Character):
    def __init__(self, name="Luke Skywalker", species="Human", eye_color = "Brown", json_dict=None):
        super().__init__(name, species, json_dict)
        if json_dict is not None:
            self.eye_color = json_dict['eye_color']

    def __str__(self):
        super().__str__() + " and has " + self.eye_color + " eyes"

class Jedi(Human):
    def has_lightsaber(self):
        return True

baseurl = "https://swapi.co/api/people"
results = requests.get(baseurl)
results_dict = json.loads(results)
results_list = results_dict["results"]
characters = []
for r in results_list:
    species_url = r['species'][0]
    if species_names[species_url] =="Human":
        characters.append(Human(json_dict=r))
    else:
        characters.append(Character(json_dict=r))

print(han)
print(c3po)
print(luke)
