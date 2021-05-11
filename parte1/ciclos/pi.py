n = int(input("n: "))
i = 0
suma_pi = 0
while i <= n:
    if i % 2 == 0:
        suma_pi -= (1 / (i + i - 1))
    else:
        suma_pi += (1 / (i + i - 1))
    i += 1
print(4 * suma_pi - 4)