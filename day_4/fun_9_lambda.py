# funkcja lambda - skrócony zapis funkcji
# domyślnie return

def odejmij(a, b):
    return a - b


print(odejmij(78, 87))  # -9

odejmij_2 = lambda a, b: a - b
print(odejmij_2(7, 89))  # -82


# zamien na lambdę
def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


oblicz_vat_2 = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat_2(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 4, 24, 50, 100, 500]
l = []
for i in lista:
    l.append(i * 2)
print(l)

print(([i * 2 for i in lista]))  # [2, 4, 6, 8, 48, 100, 200, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))

print(l2)  # [2, 4, 6, 8, 48, 100, 200, 1000]

# funkcje wyższego rzędu
# co przyjmują inna funkcje jako argument
# map() - bierze elementy z kolekcji i wykonuje na nich operację zadaną funkcją
print(f'Zastosowanie map(): {list(map(zmien, lista))}')
# Zastosowanie map(): [2, 4, 6, 8, 48, 100, 200, 1000]

# zaastosowanie lambdy jako funkcji anonimowej
# deklaracja w miejscu użycia
print(f'Zastosowanie map(): {list(map(lambda x: x * 2, lista))}')
print(f'Zastosowanie map(): {list(map(lambda x: x * 4, lista))}')
print(f'Zastosowanie map(): {list(map(lambda x: x * 5, lista))}')
print(f'Zastosowanie map(): {list(map(lambda x: x * 8, lista))}')
# Zastosowanie map(): [2, 4, 6, 8, 48, 100, 200, 1000]
# Zastosowanie map(): [4, 8, 12, 16, 96, 200, 400, 2000]
# Zastosowanie map(): [5, 10, 15, 20, 120, 250, 500, 2500]
# Zastosowanie map(): [8, 16, 24, 32, 192, 400, 800, 4000]

# filtrowanie danych
# zwraca elementy spełniające warunek
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)  # [1, 2]

# filter() - zwraca elementy spełniające warunek
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter: [1, 2]
print(f"Zastosowanie filter: {list(filter(lambda x: x > 15, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x > 50, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x < 200, lista))}")
# x > 3 i x < 250
print(f"Zastosowanie filter: {list(filter(lambda x: x > 3 and x < 250, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 250, lista))}")
# Zastosowanie filter: [1, 2, 3, 4, 24, 50, 100]
# Zastosowanie filter: [4, 24, 50, 100]
