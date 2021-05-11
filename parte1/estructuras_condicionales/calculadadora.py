num1 = int(input("Operando: "))
op = input("Operador: ")
num2 = int(input("Operando: "))

if op == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif op == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif op == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif op == "/":
    print(num1, "/", num2, "=", num1 / num2)
elif op == "**":
    print(num1, "**", num2, "=", num1 ** num2)