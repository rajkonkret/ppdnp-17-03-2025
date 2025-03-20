# funkcja zwracająca wynik
# kończy się słowkiem return

def dodaj(a, b):
    return a + b


def odejmij(a, b=0, c=10):
    return a - b - c


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(dodaj(5, 9))  # 14
wynik = dodaj(89, 56)
print("Wynik", wynik)  # Wynik 145

print(odejmij(6, 7, 8))

print(odejmij(8, 1, 2) + dodaj(7, 90))  # 102

zm = oblicz_vat(1000)
print(zm)  # 1230.0
print(type(zm))  # <class 'float'>

if zm == 1230:
    print("OK")

print(odejmij(10, b=90, c=876))  # -956
