from datetime import datetime, date, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2025-03-19
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas:", time)  # Aktualny czas: 2025-03-19 13:34:04.833069

print(time.year)  # 2025
print(today.day)  # 19

# TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# tomorrow = today + 1
#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print("Jutro będzie:", tomorrow)  # Jutro będzie: 2025-03-20

formated_data = datetime.now().strftime("%d/%m/%Y")
print(type(formated_data))  # <class 'str'>
print("Data sformatowana:", formated_data)  # Data sformatowana: 19/03/2025

# wyswietlenie czasu 13:40
formated_time = datetime.now().strftime("%H:%M")
print(type(formated_time))
print("Sformatowany czas:", formated_time)
# Sformatowany czas: 13:45

# wypisac jako czas USA 10:09 pm

products = [
    {"sku":1, "exp_date": today,"price":100},
    {"sku":2, "exp_date": today,"price":200},
    {"sku":3, "exp_date": tomorrow,"price":50},
    {"sku":4, "exp_date": today,"price":78},
    {"sku":5, "exp_date": today,"price":10.00},
]

for p in products:
    # print(p)
    # print(p['exp_date']) # 2025-03-19
    if p['exp_date']  != today: # != różne
        continue # odstawia na pólke, wraca na początek pętli, pętla weźmie następny
    p['price'] *= 0.8  # price = price * 0.8
    print(f"""Price for sku {p['sku']}
is now {p["price"]}""")
# Price for sku 1
# is now 80.0
# Price for sku 2
# is now 160.0
# Price for sku 4
# is now 62.400000000000006
# Price for sku 5
# is now 8.0