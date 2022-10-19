import json

languages = ["English","French"]
country_dict = {
    "name": "Canada",
    "population": 37742154,
    "languages": languages,
    "president": None,
}


with open('countries_exported.json', 'w') as f:
    json.dump(country_dict, f, indent=4)
