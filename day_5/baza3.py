# baza danych - system do zarzadzania danymi
# bazy relacyjne - sql
import sqlite3

data = [
    (4, "PHP", 135),
    (5, "Angular", 245),
    (6, "Android", 7100),
]

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza danych zostala podłaczona")

    insert = '''
    INSERT INTO software (id,name,price) VALUES (1, 'Python',200);
    '''

    # insert
    # cursor.execute(insert)
    # sql_connection.commit()

    insert2 = """
    INSERT INTO software (id,name,price) VALUES (?,?,?);
    """
    # cursor.execute(insert2, ("2", "Java", 350))
    # sql_connection.commit()

    id = 3
    product = "C++"
    price = 500

    # cursor.execute(insert2, (id, product, price))
    # sql_connection.commit()
    #
    # cursor.executemany(insert2, data)
    # sql_connection.commit()

    select_all = """
    SELECT * FROM software;
    """

    # select
    for row in cursor.execute(select_all):
        print(row)

    # (1, 'Python', 200.0)
    # (2, 'Java', 350.0)
    # (3, 'C++', 500.0)
    # (4, 'PHP', 135.0)
    # (5, 'Angular', 245.0)
    # (6, 'Android', 7100.0)

    select_id_1 = """
    SELECT * FROM software WHERE id=1;
    """

    for row in cursor.execute(select_id_1):
        print(row)  # (1, 'Python', 200.0)

    # update
    update = """
    UPDATE software SET price=2000 WHERE id=1;
    """

    # cursor.execute(update)
    # sql_connection.commit()

    # delete
    delete = """
    DELETE FROM software WHERE id=6;
    """
    cursor.execute(delete)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Bład otwierania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostalą zamknięta")
# Baza danych zostala podłaczona
# Baza danych zostalą zamknięta

# CRUD (od ang. create, read, update, delete)
# Działanie	        Instrukcja SQL	HTTP	            DDS
# Create	        INSERT	        PUT / POST	        write
# Read (Retrieve)	SELECT	        GET	                read / take
# Update	        UPDATE	        POST / PUT / PATCH	write
# Delete (Destroy)	DELETE	        DELETE	            dispose
