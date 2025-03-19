# pętle - możłiwość wykonania wielkrotenie tego samego fragmentu kodu
# for - iteracyjna
import random
from itertools import zip_longest

for i in range(5):  # od 0 do 4
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4

for i in range(10):
    pass  # nic nie rób, pusta pętle

for _ in range(5):  # niema zmienna
    print("Test podłoga")
    # print(_) # 4

for i in range(5):
    print(i + 2)
    print(i * 2)

# dodac do lotto pętle
lista_kule = list(range(1, 50))
lista_wyn = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    print(wyn)
    lista_wyn.append(wyn)

print("Wyniki:", lista_wyn)
# Wyniki: [35, 39, 37, 27, 30, 44]

lista3 = []
for i in range(10):
    if i % 2 == 0:  # reszta z dzielenia, modulo, liczba parzysta
        lista3.append(i)

print("Parzyste:", lista3)  # Parzyste: [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print("Parzyste:", lista3)  # Parzyste: [0, 2, 4, 6, 8]

for c in lista3:  # wyciągnie wszystkie elementy z kolekcji i zakończy
    if c > 4:
        print("Większe do 4")
    else:
        print("Mniejsze, równe 4")
# Mniejsze, równe 4
# Mniejsze, równe 4
# Mniejsze, równe 4
# Większe do 4
# Większe do 4

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

# 0
# 2
# 4
# 6
# 8
for i in range(-10, 0):  # od -10 do -1
    print(i)

for i in range(10, 0, -2):  # cofamy się, ujemny krok
    print(i)
    # 10
    # 8
    # 6
    # 4
    # 2

for c in lista3:
    if c == 2:
        c += 1
        print(c)  # dla c==2 wypisze 3
    print("Przy każdym przejsciu listy")
# Przy każdym przejsciu listy
# 3
# Przy każdym przejsciu listy
# Przy każdym przejsciu listy
# Przy każdym przejsciu listy
# Przy każdym przejsciu listy
print("Po zakończeniu pętli")
# Po zakończeniu pętli

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
    # Radek
    # Tomek
    # Zenek
    # Ania

# 0 Radek
# 1 Tomek...
for i in range(len(imiona)):
    print(i, imiona[i])

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() numeruje kolekcje i zwraca numer eleemntu i element
for p in enumerate(imiona):
    print(p)  # (3, 'Ania') -> 3 Ania

# i, o = p
for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
wiek = [44, 55, 32, 27]

# Radek 44
for p in imiona:
    print(p, wiek[imiona.index(p)])
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27

imiona = ["Radek", "Tomek", "Zenek", "Ania", "Sylwia"]
wiek = [44, 55, 32, 27]

# for p in imiona:
#     print(p, wiek[imiona.index(p)]) # IndexError: list index out of range

# zip() - łączy kolekcje
for i in zip(imiona, wiek):
    print(i)
    # ('Radek', 44)
    # ('Tomek', 55)
    # ('Zenek', 32)
    # ('Ania', 27)

for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27

# 0 Radek 44

for i in enumerate(zip(imiona, wiek)):
    print(i)

    # (0, ('Radek', 44))
    # (1, ('Tomek', 55))
    # (2, ('Zenek', 32))
    # (3, ('Ania', 27))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(a, c, d)  # 0 Radek 44
a, (c, d) = (0, ('Radek', 44))
print(a, c, d)  # 0 Radek 44

for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Ania 27

imiona = ["Radek", "Tomek", "Zenek", "Ania", "Sylwia"]
wiek = [44, 55, 32, 27]

zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x0000023595E9DF30>
# iterator
print(5 * "-")
for i in zipped:
    print(i)
# -----
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Ania', 27)
# ('Sylwia', None)
# -----
print((5 * "-"))
for i in zipped:
    print(i)
print((5 * "-"))
# iterator mozemy uzyc raz
zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)
zip_list = list(zipped)
print((5 * "-"))
for i in zip_list:
    print(i)
print((5 * "-"))
for i in zip_list:
    print(i)
print((5 * "-"))
# <itertools.zip_longest object at 0x00000260A128F790>
# -----
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Ania', 27)
# ('Sylwia', None)
# -----
# -----
# <itertools.zip_longest object at 0x00000260A135AF70>
# -----
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Ania', 27)
# ('Sylwia', None)
# -----
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Ania', 27)
# ('Sylwia', None)
# -----
