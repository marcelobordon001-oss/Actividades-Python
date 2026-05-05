numero = int(input("Introduce un número: "))

if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")
else:
    print("es cero")

#En este código, se utiliza una estructura condicional para saber si el numero introducido es +,- o 0.
#Se usa la función input() para pedir al usuario que introduzca un número, y luego se convierte a entero con int().