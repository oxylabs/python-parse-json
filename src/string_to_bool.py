import json
 
bool_string = 'true'
bool_type = json.loads(bool_string)
print(bool_type)
print(type(bool_type))
