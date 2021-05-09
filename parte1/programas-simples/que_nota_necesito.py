c1 = int(input("Ingrese nota en certamen 1: "))
c2 = int(input("Ingrese nota en certamen 2: "))
nl = int(input("Ingrese nota laboratorio: "))

c3 = (3 / 0.7) * (60 - (0.7 / 3) * (c1 + c2) - nl * 0.3)

print("Necesita nota", round(c3), "en el certamen 3")