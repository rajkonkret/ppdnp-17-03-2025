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
print(lista[-2:0]) # [3:0] -> []
print(lista[0:-2]) # [0:3] -> ['Radek', 'Tomek', 'Zenek']


