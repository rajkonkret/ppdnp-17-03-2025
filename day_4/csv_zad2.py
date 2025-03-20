import csv
from pprint import pprint
# filename = '../dane/records.csv'
filename = '../dane/records_discount.csv'

fields = []
rows = []
# delimiter=";" znak podziału w pliku csv
with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # ;

    csv_f.seek(0)  # ustawiamy odczyt ponownie na początek pliku

    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x0000027BC6C4C7C0>

    fields = next(csvreader)  # wyciągamy pierwszy wiersz

    for row in csvreader:  # dane od elementu drugiego
        # print(row)
        rows.append(row)

print(fields)
print(rows)
# ['name', 'branch', 'year', 'cgpa']
# [['radek', 'coe', '3', '0']]
##
# ['sku;exp_date;price']
# [['1;today;100'], ['2;today;200'], ['3;tomorrow;50'], ['4;today;78'], ['5;today;10.0']]
# ['sku', 'exp_date', 'price']
# [['1', 'today', '100'], ['2', 'today', '200'], ['3', 'tomorrow', '50'], ['4', 'today', '78'], ['5', 'today', '10.0']]
pprint(rows)
# [['1', 'today', '100'],
#  ['2', 'today', '200'],
#  ['3', 'tomorrow', '50'],
#  ['4', 'today', '78'],
#  ['5', 'today', '10.0']]