import os

os.system("cls")

# Excepciones (Manejo de errores)

num1 = 5
num2 = 1

print(num1 + num2)

num2 = "1"

# print(num1 + num2)

os.system("cls")

# try/except

try:
  print(num1 + num2)
  print("No se ha producido error")
except:
  print("Se ha producido un error")

os.system("cls")

# try/exept/else/finally

try:
  print(num1 + num2)
  print("No se ha producido error")
except:
  # se ejecuta si se produce una excepcion
  print("Se ha producido un error")
else: # opcional
  # se ejecuta si no se produce una excepcion
  print('estamos en el bloque "else"')
finally: # opcional
  # se ejecuta en ambos casos
  print('estamos en el bloque "finally"')

# print(num1 + num2)

os.system("cls")

try:
  print(num1 + num2)
  print("No se ha producido error")
except TypeError:                   
  print("Se ha producido un TypeError")
except ValueError:
  print("Se ha producido un ValueError")

os.system("cls")

try:
  print(num1 + num2)
  print("No se ha producido error")
except Exception as error:
  print(error)


os.system("cls")

cont = 0
num = ""

while True:
  try:
    num = int(input("Ingrese un número: "))
    if cont <= 1:
      palabra = "vez"
    else:
      palabra = "veces"

    print(f"el número ingresado es {num} y {cont} {palabra} ingresaste otro caracter")
    break
  except:
    print("debe ingresar un valor numérico")
    cont += 1