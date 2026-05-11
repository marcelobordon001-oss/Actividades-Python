numero = int(input("Introduce un número: "))
x = int(input("Introduce el límite de la tabla de multiplicar: "))
for multiplicador in range(1, x):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}") 