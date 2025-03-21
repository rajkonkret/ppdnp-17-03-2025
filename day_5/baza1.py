# baza danych - system do zarzadzania danymi
# bazy relacyjne - sql
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza danych zostala podłaczona")
except sqlite3.Error as e:
    print("Bład otwierania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostalą zamknięta")
# Baza danych zostala podłaczona
# Baza danych zostalą zamknięta
