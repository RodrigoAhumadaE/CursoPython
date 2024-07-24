import os

os.system('cls')
# Condicionales

condicion = True
condicion = False

if condicion:
  print("Mensaje condición")

print("Mensaje fuera de la condición")

condicion = 5 * 2

if condicion >= 10:
  print("Mensaje 2da condición")

if condicion > 10:
  print("Mensaje 3ra condición")

print("Mensaje fuera de la 3ra condición")

if condicion > 10:
  print("Es mayor que 10")
else:
  print("Es menor o igual a 10")

# condicion = 5 * 3

os.system("cls")

if condicion > 10 and condicion < 20:
  print("Es mayor que 10 y menor que 20")
else:
  print("Es menor o igual a 10 o mayor que 20")




  print("Es menor o igual a 10 o mayor que 20")
print("Mensaje fuera de la condición")


os.system("cls")
condicion = 5 * 5

if condicion > 10 and condicion < 20:
  print("Es mayor que 10 y menor que 20")
elif condicion % 5 == 0:
  print("Es multiplo de 5")
elif condicion > 20:                                   
  print("Es mayor que 20")
else:
  print("Es menor o igual a 10 o mayor que 20")


string = ""

if string:
  print("string no está vacio")

if not string:
  print("string está vacio")