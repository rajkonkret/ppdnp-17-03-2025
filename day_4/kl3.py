class Car:
    """
    Kalsa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # hermetyzacja
        # pole prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmiana biegu")


car = Car("Golf VII", 2012)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# pole prywatne
# print(car.__predkosc)
car.licznik()  # Prędkość wynosi 50 km/h
# car.__predkosc = 0
# car.__predkosc = 10
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()
# Prędkość wynosi 50 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi 0 km/h