# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
# pliki csv(dsv) pliki w których dane oddzielone śa znakiem podziału (, tab, ;)

import csv

fields = ["name", "branch", "year", "cgpa"]
row = ['radek', 'coe', "3", 0]

dict = dict(zip(fields, row))

# newline="" ominięcie problemu pustych lini
filename = '../dane/records.csv'
with open(filename, "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = "../dane/records_dict.csv"
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dict)

products = [
    {"sku": 1, "exp_date": "today", "price": 100},
    {"sku": 2, "exp_date": "today", "price": 200},
    {"sku": 3, "exp_date": "tomorrow", "price": 50},
    {"sku": 4, "exp_date": "today", "price": 78},
    {"sku": 5, "exp_date": "today", "price": 10.00},
]

filename = "../dane/records_discount.csv"
list_product = [key for key in products[0]]

with open(filename, "w", newline="") as fh:
    csvwriter = csv.DictWriter(fh, fieldnames=list_product, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)
#  delimiter=";" - znak podziału
