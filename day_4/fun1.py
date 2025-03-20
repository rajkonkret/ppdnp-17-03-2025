# funkcja - wykonanie fragmentyu kodu w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# w miejscu deklaracji nie wykoję się!!!
# żeby uruchomić funkcję należy ją wywołąć

a = 8
b = 6


# funkcje niezwracające wyniku
# deklaracja funkcji
# PEP8 - dwie linijki odstepu miedzy funkcjami
def dodaj():
    print(a + b)  # wypisz wynik dodawania


def dodaj2(a, b):  # dwa argumenty, obowiązkowe
    print(a + b)  # wartości przekazane, lokalne


# symuluje przeciązanie funkcji liczbą argumentów
def odejmij(a, b, c=0):  # c ma wartość domyślną
    print(a - b - c)


# uruchomienie funkcji, nazwa funkcji z nawiasami
dodaj()  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# przekazywanie argumentów po pozycji
dodaj2(45, 90)  # 135
odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4

# przekawazynie argumentów po nazwie
odejmij(a=4, b=8, c=9)  # -13
odejmij(b=4, c=8, a=9)  # -3
odejmij(b=90, a=87)  # -3, c=0

# argumenty mieszane
odejmij(1, 2, c=90)  # -91
# argumenty pozycyjne muszą być przed nazwanymi
# odejmij(c=8, 1, 2)  # SyntaxError: positional argument follows keyword argument

print(dodaj())
# 14
# None
# print(dodaj() + dodaj2(4, 67))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
