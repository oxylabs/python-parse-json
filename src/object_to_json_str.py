import json

languages = ["English","French"]
country_dict = {
    "name": "Canada",
    "population": 37742154,
    "languages": languages,
    "president": None,
}


country_string = json.dumps(country_dict)
print(country_string)