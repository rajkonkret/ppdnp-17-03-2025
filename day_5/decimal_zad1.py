# decimal - typ danych do ominięcia problemu azaokrąglenia
import decimal

decimal.getcontext().prec = 2 # precyzja na dwie cyfry (ogółem)

a = decimal.Decimal('1.2345')
b = decimal.Decimal('2.3456')

c = a + b
print(c) # 3.6
