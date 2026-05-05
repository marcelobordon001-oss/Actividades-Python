usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == "Marcelo" and contrasena == "marceadmin123€":
    print("Bienvenido al sistema")
else:
    print("Acceso denegado")


#si queremos limitar el numero de intentos, podemos usar un bucle while y una variable para contar los intentos.(explicado en clase)
intentos = 0
max_intentos = 10

while intentos < max_intentos:
    usuario = input("usuario: ")
    contraseña = input("contraseña: ")

    if usuario == "Marcelo" and contraseña == "marceadmin123€":
        print("Bienvenido al sistema")
        break

    intentos += 1
    print(f"Usuario o contraseña incorrectos, te quedan {max_intentos - intentos} intentos")

#Break sirve para salir del bucle cuando se cumple la condición de acceso correcto.
#f es una forma de formatear cadenas, permite insertar variables dentro de una cadena usando llaves {}.