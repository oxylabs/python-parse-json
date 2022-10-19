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


canada = Country("Canada", 37742154, ["English", "French"])
print(json.dumps(canada, cls=CountryEncoder))
