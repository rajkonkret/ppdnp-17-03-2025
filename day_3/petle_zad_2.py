from mypy.memprofile import print_memory_profile

dictionary = {"imie": "Radek", 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>
# klucz
# wartośc
# para

# wyswietla klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)

# wartości
for i in dictionary.values():
    print(i)
    # Radek
    # Kowalski

# pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski

for k, v in dictionary.items():
    print(k, v, sep="=>", end=" : ")
    # imie=>Radek : nazwisko=>Kowalski :
print("Radek")  # ustawi domyslny sep i end
# imie=>Radek : nazwisko=>Kowalski : Radek
print("Następna linia")
# Następna linia
pol_ang = {"kot": "cat", 'pies': "dog", "dach": "roof"}
ang_pol = {}  # pusty słownik
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

print(({value: key for key, value in pol_ang.items()}))
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

# tabnine
# coopilot
