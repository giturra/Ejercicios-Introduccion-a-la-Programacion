import math


num = float(input("Ingrese el número: "))
result = round(math.fabs(num - round(num)), 2)
print(result)