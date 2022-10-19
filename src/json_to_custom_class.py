import json


class Country:
    def __init__(self, name, population, languages):
        self.name = name
        self.population = population
        self.languages = languages


class CountryEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Country):
           # JSON object would be a dictionary.
            return {
                "name": o.name,
                "population": o.population,
                "languages": o.languages
            }
        else:
            # Base class will raise the TypeError.
            return super().default(o)

class CountryDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        decoded_country =  Country(
            o.get('name'), 
            o.get('population'), 
            o.get('languages'),
        )
        return decoded_country

with open('canada.json','r') as f:
    country_object = json.load(f, cls=CountryDecoder)

print(type(country_object))