nota = float(input("Introduce la nota: "))

if nota < 4:
    print("Suspenso")
if nota < 5:
    print("Insuficiente")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")

#Resumen: El programa solicita al usuario que introduzca una nota y luego evalúa esa nota para determinar su calificación correspondiente.
# dependedienfo de la nota imprimirá "Suspenso", "Insuficiente", "Suficiente", "Bien", "Notable" o "Sobresaliente".