tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>


# wypisać dużymi literami
# teksty są niemutowalne
# """ Return a copy of the string converted to uppercase. """
tekst.upper()  # orginał niezmieniony
print(tekst)  # Witaj Świecie
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()  # WITAJ ŚWIECIE
print(tekst_upper)  # WITAJ ŚWIECIE

tekst_lower = tekst.lower()
print(tekst_lower)  # witaj świecie
print(tekst)  # Witaj Świecie

# Witaj Świecie
# 01234567890... indeksy
print(tekst[6])  # litera o indeksie 6, "Ś"

print(tekst.index("Ś"))  # indeks 6
print(tekst.index("i"))  # indeks 1, pierwsze wystąpienie
print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # występuje 0 razy, 0123, zbiór z prawej otwarty
print(tekst[4])  # "j" indeks numer 4

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie białych znaków/spacji wiodących i następujących
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

tekst_zamiana = "Witaj Dobry Świecie"
print(tekst_zamiana.replace("Dobry", ""))  # "Witaj  Świecie"

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie' typ bajtowy
print(type(encode_s))  # <class 'bytes'>
# \xhh - Znak o wartości szesnastkowej (np. \x0A reprezentuje znak nowej linii)
print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
# f string, tekst sformatowany
tekst_format = f"Mam na imię {imie} i lubię pythona"
print(tekst_format)  # Mam na imię Radek i lubię pythona

tekst_format = f"\tMam na imię {imie}\n i kocham pythona.\b"
print(tekst_format)
# Mam na imię Radek i lubię pythona
# \n - Nowa linia
# \t - Tabulacja pozioma
# \b - Powrót kursora (usuwa poprzedni znak) backspace
# 	Mam na imię Radek
#  i kocham pythona

starszy = "Witaj %s!"  # %s - string
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!

print("Witaj", imie)  # Witaj Radek

print("""
Tekst
    wielolinijkowy
    """)
# Tekst
#     wielolinijkowy

"""Komentarz
    wielolinijkowy"""
