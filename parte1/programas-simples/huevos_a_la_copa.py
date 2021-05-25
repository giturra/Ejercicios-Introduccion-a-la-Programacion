import math

To = int(input("Temperatura original del huevo: "))
M = 47
rho = 1.038
c = 3.7
K = 5.4e-3
Ty = 70
Tw = 100

t = (M ** (2 / 3) * c * rho ** (1 / 3)) / K * math.pi ** 2 * (4 * math.pi / 3) ** (2 / 3)
t *= math.log(0.76 * (To - Tw) / (Ty - Tw))

print("El tiempo que le toma es", round(t), "segundos")