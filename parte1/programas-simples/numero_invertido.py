num = int(input("Ingrese número: "))
rev = 0
digit = num%10
rev = (rev * 10) + digit
num = num // 10
digit = num % 10
rev = (rev * 10) + digit
num = num // 10
digit = num % 10
rev = (rev * 10) + digit
num = num // 10
print(rev)