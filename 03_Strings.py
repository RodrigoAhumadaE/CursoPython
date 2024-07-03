import os
os.system('cls')
# Strings

letra = 'P'
print(letra)
print(len(letra))

frase = '¡Hola mundo!'
print(frase)
print(len(frase))

oracion = "No existen preguntas sin respuesta, solo preguntas mal formuladas"
print(oracion)
print(len(oracion))

parrafo = '''Valiente es el que se arriesga en
defender lo que cree correcto, y
no el que afronta el peligro para
impresionar a otros.'''

print(parrafo)

# Secuencias de escape
print('No existen preguntas sin respuesta,\n solo preguntas mal formuladas')

print('Días\tTemas\tEjercicio')
print('Día 1\t5\t5')
print('Día 2\t6\t20')
print('Día 3\t5\t23')
print('Día 4\t1\t35')

print('este es el simbolo de backslash (\\)')

print("En todos los lenguajes de programación comienza con \"¡Hola mundo!\"")

os.system('cls')

# antigua forma de formatear un string

# solo strings
nombre = 'Rodrigo'
apellido = 'Ahumada'
lenguaje = 'Python'
string_formateado = 'Mi nombre es %s %s y estamos programando en %s' %(nombre, apellido, lenguaje)
print(string_formateado)

# Strings  y números
radio = 10
pi = 3.14
area = pi * radio ** 2
string_formateado = 'El área de un circulo de radio %d es %.1f.' %(radio, area)
print(string_formateado)

librerias_python = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
string_formateado = 'Las siguientes son librerias de Python:%s' % (librerias_python)
print(string_formateado)

os.system('cls')

# nueva forma de formatear un string

nombre = 'Rodrigo'
apellido = 'Ahumada'
lenguaje = 'Python'
string_formateado = 'Mi nombre es {} {}y estamos programando en {}'.format(nombre, apellido, lenguaje)
print(string_formateado)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings  and numbers
radio = 10
pi = 3.14
area = pi * radio ** 2
string_formateado = 'El área de un circulo de radio {} es {:.2f}.'.format(radio, area) # 2 digitos en el decimal
print(string_formateado)

os.system('cls')

# Interpolacion de string

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

os.system('cls')

# strins como seguencia de caracteres en Python

lenguaje = 'Python'

print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[2])
print(lenguaje[3])
print(lenguaje[4])
print(lenguaje[5])

os.system('cls')

print(lenguaje[-1])
print(lenguaje[-2])
print(lenguaje[-3])
print(lenguaje[-4])
print(lenguaje[-5])
print(lenguaje[-6])

a, b = 5, 8

print(a, b)

os.system('cls')

a,b,c,d,e,f = lenguaje

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

os.system('cls')

print(lenguaje)
lenguaje_slice = lenguaje[0:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[3:]
print(lenguaje_slice)

reverso = lenguaje[::-1]
print(reverso)

palabra = "encriptacion"
print(palabra)
saltado = palabra[0:12:2]
print(saltado)

saltado = palabra[0:12:3]
print(saltado)

os.system('cls')

# Funciones de strings
print(palabra.capitalize())
print(palabra.upper())
print(palabra.count("c"))
print(palabra.isnumeric())
print("1".isnumeric())
palabra = palabra.upper()
print(palabra.lower())
print(palabra.isupper())
print(palabra.startswith("enc"))
print(palabra.startswith("ENC"))
