# '{"name":"John", "age":30, "car":null}'
# dane typu klucz-wartosc
# odpowiednikiem jsona jest słownik

import json

person_dict = {'name': "Radek", "age": 40, "czy_pali": None}
print(type(person_dict))  # <class 'dict'>

with open("nasze_dane.json", "w") as f:
    json.dump(person_dict, f)

with open("nasze_dane.json", "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }
with open("nasze_dane.json", "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }
with open('nasze_dane.json', "r") as file:
    data = json.load(file)

print(data)
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
print(data["name"])  # Radek
