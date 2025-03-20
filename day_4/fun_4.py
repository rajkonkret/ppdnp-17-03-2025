# funkcja wewnętrzna, zagniezdzona
# dekoratory - uzywaja idei funkcji wew

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    # return fun2() # wynik działania funkcji
    return fun2


fun1()
wyn = fun1()
print(wyn)  # <function fun1.<locals>.fun2 at 0x0000020D17CD37E0> referencja, adres pamięci
print(type(wyn))
print(5 * "_")
wyn()  # To jest fun2
wyn()
wyn()
wyn()
wyn()
wyn()
# To jest fun2
# To jest fun2
# To jest fun2
# To jest fun2
# To jest fun2
# To jest fun2
