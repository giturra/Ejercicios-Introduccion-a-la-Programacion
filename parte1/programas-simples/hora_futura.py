hora_actual = int(input("Hora actual: "))
cantidad_de_horas = int(input("Cantidad de horas: "))

resultado = (hora_actual + cantidad_de_horas) % 12

print("En", cantidad_de_horas, "horas, el reloj marcara las", resultado)