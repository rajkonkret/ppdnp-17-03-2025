# baza danych - system do zarzadzania danymi
# bazy relacyjne - sql
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza danych zostala podłaczona")

    query = """
    CREATE TABLE IF NOT EXISTS developers(
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_data DATETIME,
    salary REAL NOT NULL);
    """

    # # uruchamianie query
    # cursor.execute(query)
    # sql_connection.commit()  # zatwierdzenei zmian

    with open('tables.sql', "r") as file:
        sql_script = file.read()

    cursor.executescript(sql_script)  # wykonanie skryptu

except sqlite3.Error as e:
    print("Bład otwierania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostalą zamknięta")
# Baza danych zostala podłaczona
# Baza danych zostalą zamknięta
