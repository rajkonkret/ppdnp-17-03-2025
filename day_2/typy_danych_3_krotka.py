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

# tupla jest niemutowalna
# tupla_liczby[3] = 134  # TypeError: 'tuple' object does not support item assignment

# usunięcie tupli
del tupla_liczby
# print(tupla_liczby) # NameError: name 'tupla_liczby' is not defined

print(tupla_imiona.index("Radek"))  # indeks 0
print(tupla_imiona.count("Radek"))  # występuje 1 raz
# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>

a, b = 1, 2
print(a, b)

a, b = tup
print(f"{a=}, {b=}")  # a=1, b=2

tup_2 = 1, 2, 3

# a, b = tup_2
a, *b = tup_2
print(f"{a=}, {b=}")
# a=1, b=[2, 3]

print(tupla_imiona)
# imie1, imie2, imie3
# * worek na pozostałe dane
imie1, *imie2, imie3 = tupla_imiona
print(f"{imie1}, {imie2}, {imie3}")
# Radek, ['Tomek', 'Zenek', 'Mateusz', 'Sylwia', 'Zbyszek'], Donald

*imie1, imie2, imie3 = tupla_imiona
print(f"{imie1}, {imie2}, {imie3}")
# ['Radek', 'Tomek', 'Zenek', 'Mateusz', 'Sylwia'], Zbyszek, Donald

imie1, imie2, *imie3 = tupla_imiona
print(f"{imie1}, {imie2}, {imie3}")
# Radek, Tomek, ['Zenek', 'Mateusz', 'Sylwia', 'Zbyszek', 'Donald']

# sortowanie krotki zwraca listę
print(sorted(tupla_imiona))
# ['Donald', 'Mateusz', 'Radek', 'Sylwia', 'Tomek', 'Zbyszek', 'Zenek']
print(tupla_imiona)
# krotka zostaje nieposortowana
# ('Radek', 'Tomek', 'Zenek', 'Mateusz', 'Sylwia', 'Zbyszek', 'Donald')
