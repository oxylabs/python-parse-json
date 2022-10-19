import json

countries = '["United States", "Canada"]'
counties_list= json.loads(countries)

print(type(counties_list))
print(counties_list[0])

