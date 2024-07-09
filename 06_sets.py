import os
os.system('cls')
# sets

mi_set = set()
mi_otro_set = {}

print(type(mi_set))
print(type(mi_otro_set))

mi_otro_set = {41, 1.76, "Rodrigo", "Ahumada"}
print(type(mi_otro_set))
# print(mi_otro_set[0])

print(mi_otro_set)

mi_otro_set.add("Desarrollador")
print(mi_otro_set)

print("Rodrigo" in mi_otro_set)
print("rodrigo" in mi_otro_set)

mi_otro_set.remove("Desarrollador")
print(mi_otro_set)

mi_otro_set.clear()
print(len(mi_otro_set))

del mi_otro_set
# print(mi_otro_set)

lenguajes = {"Javascript", "C#", "Python", "Java", "PHP", "Ruby"}
conocimientos = {"HTML", "CSS", "Javascript", "C#", "Python", "React JS", "MySQL"}

print(conocimientos.union(lenguajes))
print(lenguajes.union({"Go"}))

print(conocimientos.difference(lenguajes))
print(lenguajes.difference(conocimientos))

print(conocimientos.intersection(lenguajes))