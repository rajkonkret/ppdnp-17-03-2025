# słownik - para klucz wartość
# {"user": "Radek", "wiek": 76}
# klucze nie mogą sie powtarzac
# odpowiednik jsona

# pusty słownik
dictionary = dict()
print(dictionary)  # {} pusty słownik
print(type(dictionary))  # <class 'dict'>

dictionary_1 = {}
print(type(dictionary_1))
print(dictionary_1)
# <class 'dict'>
# {}

# dodanie elementów do słownika
dictionary["imie"] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 48
print(dictionary)  # {'imie': 'Radek', 'wiek': 48}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 48])
# dict_items([('imie', 'Radek'), ('wiek', 48)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 48}

# wypisanie wartosci ze słownika
print(dictionary['imie'])  # Tomek

# gdy klucz nie istnieje
# print(dictionary["Imie"])  # KeyError: 'Imie'
print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "deafault"))  # deafault

dictionary.update({'data': "12-12-2025"})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 48, 'data': '12-12-2025'}

# [('imie', 'Radek'), ('wiek', 48)]
dict_small = {'x': 2}
print(dict_small)  # {'x': 2}
dict_small.update([('y', '3'), ('z', '5')])
print(dict_small)
# {'x': 2, 'y': '3', 'z': '5'}
