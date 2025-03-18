# kolekcje przechowuje dowolną ilośc elementów, róznego typu na raz

# lista, krotka, zbiór, słownik

# lista - przechowuje dowolną ilośc elementów, róznego typu na raz
# zachowuje kolejnośc podczas dodwania elemntów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Anna")
lista.append("Wojtek")
# zmienia bazową listę
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Anna', 'Wojtek']
# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Wojtek']
#     0         1       2        3        4 indeksy
#     -5        -4      -3       -2       -1
print(len(lista))  # 5

print(lista[0])  # Radek
print(lista[2])  # Zenek
print(lista[4])  # Wojtek

# próba odczytania nieistniejącego indeksu
# print(lista[10])  # IndexError: list index out of range

print(lista[4])  # Wojtek ostatni element z listy
print(lista[len(lista) - 1])  # Wojtek ostatni element z listy
print(lista[-1])  # # Wojtek ostatni element z listy

print(lista[-3])  # Zenek

# wyswietlanie (wycinanie)  fragmentu listy - slicowanie
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'], indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Anna', 'Wojtek'] indeksy 234 z ostatnim włacznie
print(lista[2:4])  # ['Zenek', 'Anna'] bez indeksu 4

print(lista[2:16])  # ['Zenek', 'Anna', 'Wojtek']
print(lista[:])  # całą lista # ['Radek', 'Tomek', 'Zenek', 'Anna', 'Wojtek']
print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek']
print(lista[10:27])  # []

# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Wojtek']
#     0         1       2        3        4 indeksy
#     -5        -4      -3       -2       -1
print(lista[-2:0])  # [3:0] -> []
print(lista[0:-2])  # [0:3] -> ['Radek', 'Tomek', 'Zenek']

lista_15 = list(range(15))  # generuje liczbu od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# co druga liczbę wyświetlić
print(lista_15[0:15:2])  # [start:stop:krok]
# [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # (start, stop, krok), [0, 2, 4, 6, 8, 10, 12, 14]
print(lista[::2])  # ['Radek', 'Zenek', 'Wojtek']
print(lista_15[::2])  # [0, 2, 4, 6, 8, 10, 12, 14]

# wypisanie w odwrotnej kolejnosci
print(lista[::-1])  # ['Wojtek', 'Anna', 'Zenek', 'Tomek', 'Radek']
print(lista_15[::-1])  # [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# nadpisanie elementu w liście na wskazanym indeksie
lista[3] = "Marek"
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Wojtek']

# wstawienie elementu do listy na wskazany indeks
lista.insert(1, "Krzysztof")
print(lista)  # ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Marek', 'Wojtek']

lista.insert(15, "Kasia")
print(lista)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Marek', 'Wojtek', 'Kasia']

# sprawdzenie na którym indeksie jest dany element
print(lista.index("Kasia"))  # 6
print(lista.index("Krzysztof"))  # 1
lista.append("Tomek")
print(lista)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Marek', 'Wojtek', 'Kasia', 'Tomek']
print(lista.index("Tomek"))  # indeks 2, pierwsze wystąpienie

# usunięcie elementu
lista.remove("Marek")
print(lista)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Wojtek', 'Kasia', 'Tomek']

# pop() - usunięcie po indeksie
print(lista.pop(6))  # Tomek, zwraca co usunął celem weryfikacji
print(lista)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Wojtek', 'Kasia']
print(lista.pop(-3))  # Zenek
print(lista.pop())  # usunie ostatni element Kasia
print(lista)  # ['Radek', 'Krzysztof', 'Tomek', 'Wojtek']

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3
b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista_2 = lista  # a = b, kopia referencji, kopia adresu
lista_copy = lista.copy()  # kopia elemntów listy w nowej liście
print(lista_2)
print(lista)
print(lista_copy)
# ['Radek', 'Krzysztof', 'Tomek', 'Wojtek']
# ['Radek', 'Krzysztof', 'Tomek', 'Wojtek']
lista.clear()  # usunięcie elementów z listy
print(lista)  # []
print(lista_2)  # []
print(lista_copy)  # ['Radek', 'Krzysztof', 'Tomek', 'Wojtek']
print(id(lista))  # 2879406842496
print(id(lista_2))  # 2879406842496
print(id(lista_copy))  # 2879411470080

liczby = [54, 999, 34, 22, 12.34, 567]
print(liczby)  # [54, 999, 34, 22, 12.34, 567]
print(type(liczby))  # <class 'list'>
liczby.sort()
print(liczby)  ## [12.34, 22, 34, 54, 567, 999]

liczby = [54, 999, 34, 22, 12.34, 567, "A"]
print(type(liczby))  # <class 'list'>
# liczby.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

print(lista_copy)  # ['Radek', 'Krzysztof', 'Tomek', 'Wojtek']
lista_copy.sort()
print(lista_copy)  # ['Krzysztof', 'Radek', 'Tomek', 'Wojtek']

lista_copy.sort(reverse=True)  # sortowanie z odwróceniem
print(lista_copy)  # ['Wojtek', 'Tomek', 'Radek', 'Krzysztof']

lista_copy.reverse()  # odwrócenie listy bez sortowanie
# ['Wojtek', 'Tomek', 'Radek', 'Krzysztof']

liczby[3] = 666
print(liczby[0:3])
print(liczby[-2])
print(liczby)  # [54, 999, 34, 666, 12.34, 567, 'A']

tekst = "Pyth on."
lista1 = list(tekst)
# rozpakowanie sekwencji
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']
print(len(lista1))  # 8

lista2 = [tekst]
print(lista2)  # ['Pyth on.']
print(len(lista2))  # 1

krotka = tuple(lista_copy)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Krzysztof', 'Radek', 'Tomek', 'Wojtek')
