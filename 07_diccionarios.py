# Diccionarios

import os
os.system('cls')


mi_dict = dict()
mi_otro_dict = {}

print(type(mi_dict))
print(type(mi_otro_dict))

mi_dict = {
  'Nombre': 'Rodrigo',
  'Apellido': 'Ahumada',
  'Edad': 41,
  'Estatura': 1.76,
  "Lenguajes": {"python", "JavaScript", "C#"},
  1: 425
}

print(mi_dict)

print(mi_dict['Nombre'])

mi_otro_dict = {
  'nombre': 'Rodrigo',
  'apellido': 'Ahumada',
  'edad': 41,
  'estatura': 1.76,
  1: "python"
}

print(mi_otro_dict)

print(mi_dict['Lenguajes'])

mi_dict['Nombre'] = 'Alex'

print(mi_dict['Nombre'])

mi_dict['Calle'] = 'Calle Uno'

print(mi_dict)

del mi_dict['Calle']

print(mi_dict)

print("Ahumada" in mi_dict.values())

print("Nombre" in mi_dict)

os.system("cls")

print(mi_dict.items())
print(mi_dict.values())
print(mi_dict.keys())
print(mi_dict.get("Nombre"))
print(mi_dict.pop(1))
print(mi_dict)





