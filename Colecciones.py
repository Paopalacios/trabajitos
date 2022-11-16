lista = [1,2,3,4,5,6,7]
print(lista[3])
lista.append(14)
print(lista)
print(lista[-1])
print(lista[0:3])
lista.remove(4)
lista.pop(4)
print(lista)

#tarea 
paises =["Argentina", "Uruguay", "Brasil", "Chle", "Colombia", "Paraguay"]
print(paises)
size= len(paises)
print(size)
for p in paises:
    print(p)
paises.append("Bolivia")
paises.append("Perú")
print(paises)

for p in reversed(paises):
    print(p)
