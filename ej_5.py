edad = int(input("Introduce tu edad: "))

if edad >= 0 and edad <= 100:
    print("edad válida")
else:
    print("edad no válida")

#if - else, sirven para tomar decisiones en el código, dependiendo de si una condición es verdadera o falsa. 
#En este caso, se verifica si la edad ingresada está dentro de un rango válido (0 a 100).
#Si la condición es verdadera, se imprime "edad válida", de lo contrario, se imprime "edad no válida".