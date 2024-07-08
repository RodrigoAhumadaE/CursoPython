import os

# Listas

mi_lista = list()
mi_otra_lista = []

print(len(mi_lista))

mi_lista = [35, 24, 62, 52, 30, 30, 17]
print(len(mi_lista))

os.system('cls')

mi_otra_lista = [41, 1.76, "Rodrigo", "Ahumada"]
print(mi_otra_lista)
print(len(mi_otra_lista))
print(type(mi_otra_lista))
print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[-1])
print(mi_otra_lista[-3])
# print(mi_otra_lista[5])

edad, estatura, nombre, apellido = mi_otra_lista

print(edad, estatura, nombre, apellido)

print(mi_lista + mi_otra_lista)
print(mi_lista * 3)

nueva_lista = mi_lista + mi_otra_lista
print(nueva_lista)

os.system('cls')

# Funciones de lista

mi_otra_lista.append("Desarrollador")
print(mi_otra_lista)

mi_otra_lista.insert(2, 987654321)
print(mi_otra_lista)

mi_otra_lista[2] = 971232411
print(mi_otra_lista)

mi_otra_lista.remove(971232411)
print(mi_otra_lista)

print(mi_lista)
mi_lista.remove(30)
print(mi_lista)

print(mi_lista.pop())
print(mi_lista)

print(mi_lista.pop(2))
print(mi_lista)

del mi_lista[2]
print(mi_lista)

nueva_lista = mi_lista.copy()
print(nueva_lista)

mi_lista.clear()
print(mi_lista)

nueva_lista.reverse()
print(nueva_lista)

nueva_lista.sort()
print(nueva_lista)