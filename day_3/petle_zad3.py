#  while - sterowana warunkiem

# pętla nieskońćzona
# while True:
#     print("Komunikat !!!!")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !! !!")
    if licznik > 10:
        break
# Komunikat 2 !! !! !!
# Komunikat 2 !! !! !!
# Komunikat 2 !! !! !!
# Komunikat 2 !! !! !!
# Komunikat 2 !! !! !!
# Komunikat 2 !! !! !!
# Komunikat 2 !! !! !!
# Komunikat 2 !! !! !!
# Komunikat 2 !! !! !!
# Komunikat 2 !! !! !!
# Komunikat 2 !! !! !!
print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!! !!! !!!")
# Komunikat 3 !!! !!! !!!
# Komunikat 3 !!! !!! !!!
# Komunikat 3 !!! !!! !!!
# Komunikat 3 !!! !!! !!!
# Komunikat 3 !!! !!! !!!
# Komunikat 3 !!! !!! !!!
# Komunikat 3 !!! !!! !!!
# Komunikat 3 !!! !!! !!!
# Komunikat 3 !!! !!! !!!
# Komunikat 3 !!! !!! !!!

# password = input("Podaj hasło")
# while password != "secret": # != różne
#     password = input("Błędne hasło, podaj ponownie")
# print("Hasło prawidłowe")
# Podaj hasłowwww
# Błędne hasło, podaj ponownieqeqeqw
# Błędne hasło, podaj ponowniewqeefdec
# Błędne hasło, podaj ponownie1213
# Błędne hasło, podaj ponownieesfdvfv
# Błędne hasło, podaj ponowniesecret
# Hasło prawidłowe

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)  # ['1', '2', '3', '4', '5', '6', '55', '88', '99', '00']
print(lista_int)
# ['1', '2', '3', '4', '56']
# [1, 2, 3, 4, 56]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6] zachowało kolejność

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}
unique = list(dict.fromkeys(my_list))
print(unique)  # [1, 5, 2, 3, 4, 6]
