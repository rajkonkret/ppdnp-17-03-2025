# krotka - tuple - kolekcja tylko do odczytu, niemutowalna
# pozwala efektywniej zarządzać pamięcią
# przechowywanie stałych
# krotka jednoelementowa

tupla_imiona = "Radek", "Tomek", "Zenek", "Mateusz", "Sylwia", "Zbyszek", "Donald"
print(tupla_imiona)
# ('Radek', 'Tomek', 'Zenek', 'Mateusz', 'Sylwia', 'Zbyszek', 'Donald')
print(type(tupla_imiona))  # <class 'tuple'>

tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

# PEP8 zaleca krotke jedoelementowa z nawiasem
# tupla jednoelemntowa
tupla = (43,)
print(tupla)  # (43,)
print(type(tupla))  # <class 'tuple'>

# tupla jednoelemntowa
tupla = 43,
print(tupla)  # (43,)
print(type(tupla))  # <class 'tuple'>
