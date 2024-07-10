import json

vehicle_entity = {  "motorvehicles": {      "vehicle": {      "registration_no": "CBB1456",      "make": "Toyota",      "model": "Premio"    },    "owner": {      "first_name": "Amal",      "last_name": "Perera", "nic": "900324770V" }  }}

serialized = json.dumps(vehicle_entity)
deserialized = json.loads(serialized)

print(serialized)
print(deserialized)