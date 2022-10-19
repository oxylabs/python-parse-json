import json

with open('united_states.json') as f:
  data = json.load(f)

print(type(data))