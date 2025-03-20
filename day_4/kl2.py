class Human:
    """
    Kalsa Human opisująca obiekt w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # wypisz_wiek
    def wypisz_wiek(self):
        print(f"Masz teraz {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Masz {self.wzrost} cm wzrostu.")

    def ruszaj(self):

        if self.plec == "k":
            print("Ruszyłąm w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Anna", 45, 170)
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)

cz1.powitanie()
cz1.wypisz_wiek()
cz1.wypisz_wzrost()

cz2 = Human("radek", 50, 190, "m")
cz1.ruszaj()
cz2.ruszaj()
# Ruszyłąm w drogę
# Ruszyłem w drogę
