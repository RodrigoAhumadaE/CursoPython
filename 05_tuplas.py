import os
os.system("clear")

# Tuplas
mi_tupla = tuple()
mi_otra_tupla = ()

mi_tupla = (41, 1.76, "Rodrigo", "Ahumada")
mi_otra_tupla = (35, 24, 62, 52, 30, 30, 17)

print(mi_tupla[0])
print(mi_tupla[-1])

print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla.count(41))
print(mi_otra_tupla.count(30))
print(mi_tupla.count(45))

print(mi_tupla.index(1.76))

# mi_tupla[1] = 1.80 error

os.system("clear")

nueva_tupla = mi_tupla + mi_otra_tupla
print(nueva_tupla)
print(type(nueva_tupla))

print(nueva_tupla[3:6])

mi_tupla = list(mi_tupla)
print(type(mi_tupla))

mi_tupla.append("Desarrollador")
print(mi_tupla)

mi_tupla = tuple(mi_tupla)
print(mi_tupla)
print(type(mi_tupla))

del mi_tupla

# del mi_tupla[1]

# print(mi_tupla)
