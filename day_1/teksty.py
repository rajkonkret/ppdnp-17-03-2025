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
print(tekst[4])  # "j"
