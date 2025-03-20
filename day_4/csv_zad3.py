import pandas

# pip install pandas

# data = pandas.read_csv('../dane/records.csv')
data = pandas.read_csv('../dane/records_discount.csv', delimiter=";")

print(data)
#     name branch  year  cgpa
# 0  radek    coe     3     0
print(data.columns)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
#    sku  exp_date  price
# 0    1     today  100.0
# 1    2     today  200.0
# 2    3  tomorrow   50.0
# 3    4     today   78.0
# 4    5     today   10.0
# Index(['sku', 'exp_date', 'price'], dtype='object')
