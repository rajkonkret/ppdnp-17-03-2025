# zbiór (set) - zbior przechowuje unikalne wartości (bez duplikatów)
# nie zachowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # tworzenie zbioru
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'> zbiór

# pusty zbiór
zb2 = set()  # tylko i wyłacznie za pomocą set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie elemntu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(54)
zbior.add(24)
print(zbior)
# {33, 66, 777, 11, 44, 18, 22, 55, 54, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 54, 24}

# pop() - usnięcie pierwszego elementu
print(zbior.pop())
print(zbior)
print(zbior.pop())
# 33
# {66, 777, 11, 44, 18, 22, 54, 24}
# 66
zmienna = zbior.pop()
print("usunęliśmy element:", zmienna)  # usunęliśmy element: 777

zbior_copy = zbior.copy()
print(zbior_copy)  # {18, 22, 54, 24, 11, 44}
print(zbior)  # {11, 44, 18, 22, 54, 24}
print(id(zbior))  # 2130558277152
print(id(zbior_copy))  # 2130558603488

zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

# suma zbiorów, zwraca nowy zbior
print(zbior | zbior_2)  # {11, 44, 12.34, 18, 52, 22, 54, 24, 667, 62}
print(zbior.union(zbior_2))  # {11, 44, 12.34, 18, 52, 22, 54, 24, 667, 62}

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica
print(zbior - zbior_2)  # {54, 24, 22}
print(zbior.difference(zbior_2))  # {54, 24, 22}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# łaczy zbiory, zmienia bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {11, 44, 12.34, 18, 52, 22, 54, 24, 667, 62}

krotka = tuple(zbior)
print(zbior)

lista = list(zbior)
print(lista)

print(667 in zbior)  # True
print(777 in lista)  # False
print(777 in krotka)  # False
