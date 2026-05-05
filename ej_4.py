anio_actual = 2026

#int lo utilizamos para convertir el valor ingresado por el usuario a un número entero, ya que el input devuelve una cadena de texto.
anio_nacimiento = int(input("Introduce tu año de nacimiento: "))

edad = anio_actual - anio_nacimiento

print(f"Tu edad aproximada es: {edad} años")