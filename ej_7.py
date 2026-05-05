print("Menú de opciones:")
print("1. Ver saludo")
print("2. Ver curso")
print("3. Salir")

opcion = input("Elige una opción: ")

if opcion == "1":
    print("bienvenido al curso")
elif opcion == "2":
    print("Curso de Python")
elif opcion == "3":
    print("Saliendo, adiós!")
else:
    print("Opción no válida")

#Resumen: Menú donde donde al elegir se responde con un mensaje específico, o se muestra un error si la opción no es válida.
#usamos condicionales para manejar las opciones del menú(if, elif, else).