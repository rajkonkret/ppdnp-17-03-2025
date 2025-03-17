import sys

print()  # pusta linia wypisz/wydrukuj
# zasady PEP8 https://peps.python.org/pep-0008/ zasady czystego kodu
# ctrl alt l (ctrl opt l) formatowanie kodu

print("Nazywam się Radek")
print('Nazywam się Radek')
# ctrl / (?) komentarz lini z kursorem
# print('Radek") 3 musi byc zamknięty takim jak otwqarty
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-17-03-2025\day_1\pierwszy.py", line 7
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 7)
# Process finished with exit code 1 wystapił bląd, program się zatrzyma
print("Dalej")
#
# Nazywam się Radek
# Nazywam się Radek
# Dalej
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
# ctrl d - powielanie lini z kursorem
# ctrl shift strzałka w dół -> zammiana kolejnosci
print('Nazywam się Radek')

# type() - sprawdzenie typu
print(type("Radek"))  # <class 'str'>, dane tekstowe

print("39" + "39")  # 3939 łączy stringi, konkatenacja

print(39 + 39)  # 78
print(type(39))  # liczba całkowita
print(sys.int_info)
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640
# )

# silne typowanie - nie zamienai typów
# print("39" + 39) # TypeError: can only concatenate str (not "int") to str

# musimy jawnie podac (rzutowac) typ przy takiego typu operacji
print(int("39") + 39)  # int() zammiana (rzutowanie)  na int, 78
# print(int("A")) # ValueError: invalid literal for int() with base 10: 'A'

# łacze jako stringi (konkatenacja)
print("39" + str(39))  # str() - rzutowanie na tekst, 3939

print(5 * "4")  # 44444
print(5 * "-")  # -----

print(168 * 50)  # 8400
print("168" * 50)
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print(int("168") * int(50))  # 8400

# zmienna - pudełko na dane, przechowuje jeden element
# snake_case
# nazwa zmiennej podpowiada co przechowuje

# typowanie dynamiczne
# zmienna przyjmuje typ danej jaką przechowuje
a = "Radek"
print(type(a))  # <class 'str'>
a = 10
print(type(a))  # <class 'int'>

name = "Radek"
name = 10

# to jest tylko podpowiedź dla programisty, pycharma, ale program tych danych nie weryfikuje
# mypy
# pip install mypy
name: str = "Radek"
name = 10
# pierwszy.py:76: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:80: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:85: error: Name "name" already defined on line 79  [no-redef]
# pierwszy.py:86: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 4 errors in 1 file (checked 1 source file)

name = "radek"
age = 56  # 56
print(age)
print(type(age))
# <class 'int'>
# <class 'int'>
