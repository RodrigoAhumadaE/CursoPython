import os

# Variables
dato = ""
miVariable = "Texto de la variable"
print(miVariable)
print(dato)

mi_variable = "otro texto de la variable" # forma correcta
print(mi_variable)

_if = True
print(_if)

'''
como no definir variables
first-name
first@name
first$name
num-1
1num
'''

'''Tipo string'''
nombre: str = 'Rodrigo'
apellido = 'Ahumada'
pais = 'Chile'

'''tipo numericas'''
edad = 41
estatura = 1.76
constante = 3 + 1j

print(nombre)

nombre = 15
print(nombre)
nombre = False
print(nombre)

nombre = "Rodrigo"

'''tipo bool'''
casado = False
titulado = True

'''tipo lista'''
habilidades = ['HTML', 'CSS', 'JS', 'React', 'Python']
print(habilidades[2])

'''tipo tupla'''
planetas = ("Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno")
print(planetas[5])

'''tipo diccionario'''
informacion_personal = {
  'nombre':'Rodrigo',
  'apellido':'Ahumada',
  'pais':'Chile',
  'edad':41
}

print(informacion_personal["edad"])

os.system('cls')

'''tipo set'''
conjunto1 = {4, 5, 7, 8}
conjunto2 = {9, 3, 7, 5}
print(f"conjunto1: {conjunto1}")
print(f"conjunto2: {conjunto2}")

print(f"unión: {conjunto1 | conjunto2}")

print(f"intersección: {conjunto1 & conjunto2}")

print(f"diferencia del conjunto1 sobre el conjunto2: {conjunto1 - conjunto2}")
print(f"diferencia del conjunto2 sobre el conjunto1: {conjunto2 - conjunto1}")

print("Mi nombre es", nombre, apellido, "y mido", estatura, "m.")
print("Mi nombre es " + nombre + " " + apellido + " y mido " + str(estatura) + "m.")
print(f"Mi nombre es {nombre} {apellido} y mido {estatura}m.")   #cadena formateada f-string o interpolación de cadena