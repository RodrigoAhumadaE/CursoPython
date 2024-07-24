import os

os.system("cls")
'''
realice un código que muestre por pantalla las tablas de multiplicar del 1 al 10
ejemplo for con funcion range() y for anidados
'''

for i in range(1, 11):
  for j in range(1,11):
    print(f"{i} x {j} = {i * j}")
  print("==============")

