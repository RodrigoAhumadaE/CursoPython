import os

# Operadores aritmeticos

print(2 + 5)    #suma
print(9 - 5)    #resta
print(3 * 7)    #multiplicación
print(12 / 5)    #división
print(type(str(12 / 5)))    #división
print(9 % 2)    #modulo o resto de una división
print(3 ** 3)   #potencia
print(11 // 3)   #división con resultado entero

print("¡" + "Hola " + "mundo" + "!")
print("hola " + str(5))
print("hola " * 5)

os.system("cls")

# Operadores Comparativos

print(3 > 4)    #mayor
print(3 < 4)    #menor
print(3 >= 4)   #mayor igual > =
print(3 <= 4)   #menor igual
print(4 == 4)   #igual = =
print(4 != 4)   #distinto ! =

print(3 < 4 > 2)

os.system("cls")

# Operadores de asignacion

num = 1
print(num)

num += 3    # num = num + 3
print(num)

num -= 2
print(num)

num *= 15
print(num)

num /= 2
print(num)

num %= 4
print(num)

num //= 2
print(num)

num = 2

num **= 3
print(num)

os.system("cls")

# Operadores lógicos

print(5 > 3 and 2 > 5)        # False ^ && ||
print(5 > 3 and 2 < 5)        # True

print(not(5 > 3 and 2 < 5))   # False

print(5 > 3 or 2 > 5)         # True
print(5 < 3 or 2 > 5)         # False