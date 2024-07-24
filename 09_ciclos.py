import os
os.system("cls")

# Loops/Ciclos/bucles

# while

num = 0

while num < 10:
  print(num)
  num += 2
else:
  print(f"num es mayor o igual a {num}")

print("la ejecución continua!")

os.system("cls")

num = 0
while True:
  print(num)
  num += 2
  if num >= 10:
    break

os.system("cls")

while num < 20:
  num += 1
  if num == 15:
    print(f"num es igual a {num}")
    continue
  
  print(f"{num} es menos a 20")

print("la ejecución continua")

# For
os.system("cls")

for i in range(1, 11 ):
  print(i)

os.system("cls")

mi_lista = [35, 24, 62, 52, 30, 30, 17]

for dato in mi_lista:
  print(dato)

mi_tupla = (41, 1.76, "Rodrigo", "Ahumada", "Desarrollador")
for dato in mi_tupla:
  print(dato)

mi_set = {"HTML", "CSS", "Javascript", "C#", "Python", "React JS", "MySQL"}
for dato in mi_set:
  print(dato)

mi_dict = {
  'nombre':'Rodrigo',
  'apellido':'Ahumada',
  'pais':'Chile',
  'edad':41
}
for dato in mi_dict.values():
  print(dato)
else:
  print("el For a terminado")

os.system("cls")

for dato in mi_set:
  print(dato)
  if dato == "React JS":
    break
  print("se ejecuta")


os.system("cls")

matriz = [
[35, 24, 62, 52, 30, 30, 17, 43],
[12, 36, 81, 9, 33, 57, 109, 54],
[25, 24, 70, 69, 33, 49, 15, 65],
[19, 55, 1, 111, 47, 30, 32, 76],
[99, 76, 64, 52, 27, 20, 40, 87],
[50, 60, 35, 7, 107, 30, 17, 98],
[35, 24, 162, 52, 30, 30, 17, 2],
[22, 33, 44, 55, 66, 77, 88, 99]
]

for lista in matriz:
  for numero in lista:
    if numero % 2 != 0:
      print(numero)

os.system("Cls")

for i in range(len(matriz)):
  for j in range(len(matriz[i])):
    if matriz[i][j] % 2 == 0:
      print(matriz[i][j])
