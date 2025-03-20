# klasa - element programowania obiektowego
# klasa - szablon, opis, przepis wg którego będą budowane obiekty
# cechy - pola (zmienne)
# metody - funkcje
# klasa musi być zadeklarowana przed użyciem
# tworzenie obiektu uruchmai metodę __init__ (konstruktor)
# paradygmaty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja


# PascalCase -> PEP8
# deklaracaja klasy
class Human:
    """
    Kalsa Human opisująca człowieka w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    # self - obiekt, który wyołuje metode w klasie
    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # wypisz_wiek
    def wypisz_wiek(self):
        print(f"Masz teraz {self.wiek} lat.")


# tworzenie obiektu
cz1 = Human()
# print(Human.__doc__)
#
# print(print.__doc__)
# help(Human)


# pydoc -b uruchomienie serwera z dokumentacją
# cd .\day_4
#  pydoc -w kl1 - tworzenie pliku html z dokumentacją

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
#
# None
# k
cz1.wiek = 50
cz1.imie = "Radek"
cz1.plec = "m"

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Radek
# 50
# m

# drugiczłowiek odmiennej płci
cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 34
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Anna
# 34
# k
cz1.powitanie()
cz2.powitanie()
# Nazywam się Radek
# Nazywam się Anna
