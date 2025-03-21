from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # dekorator, metoda abstrakcyjna
    def wydaj_glos(self):
        pass


class Kura(Ptak):  # dziedziczymy po klasie Ptak
    """
    Klasa Kura dziedziczy po kalsie Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # super() klasa wyzsza, musimy wywołać konstruktor klasy wyższej

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_glos(self):
        print("ko oko koko")

    def dziobanie(self):
        print(f"Tu {self.gatunek}. Idę sobie podziobać")


class Orzel(Ptak):
    """
    Klasa Orzeł
    """

    def wydaj_glos(self):
        print("Kir kier kir")

    def polowanie(self):
        print(f"Tu {self.gatunek}. Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Klasa Sowa
    """


# klasa Ptak jest abstrakcyjna
# nie mozesz stworzyc obiektu tej klasy
# TypeError: Can't instantiate abstract class Ptak
# without an implementation for abstract method 'wydaj_glos'
# or1 = Ptak("Orzeł", 45)
# or1.latam()  # Tu Orzeł Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
kur2.wydaj_glos()  # ko oko koko

or2 = Orzel("Orzeł Bielik", 50)
or2.latam()
or2.wydaj_glos()
# Tu Orzeł Bielik Lecę z szybkością 50
# Kir kier kir

or2.polowanie()
kur2.dziobanie()
# Tu Orzeł Bielik. Rozpoczynam polowanie
# Tu Kura. Idę sobie podziobać

# Brak metody wydaj_odglos w klasie Sowa
# TypeError: Can't instantiate abstract class Sowa
# without an implementation for abstract method 'wydaj_glos'
# sow = Sowa("Sowa", 20)

# polimorfizm - cechy wspolne obiektów róznych klas
# poprzez dziedziczenie po tej samej klasie
lista = [kur2, or2]

for i in lista:
    i.wydaj_glos()
# ko oko koko
# Kir kier kir
