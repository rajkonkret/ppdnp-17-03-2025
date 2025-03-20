a = 10
b = 10


def dodaj():
    a = 8  # wartości lokalne
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)  # weżmie wartości globalne


def dodaj3():
    global a  # użyj globalne a
    a = 9  # globalne a, zmiana powoduje zmiane globalnej a
    b = 89
    print(a + b)


print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj()  # 15
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj2()  # 20
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj3()  # 98
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=9 (globalna)
dodaj2()  # 19
