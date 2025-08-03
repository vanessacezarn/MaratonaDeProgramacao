risada = input().lower()

letras = list(risada)

lista = []
for l in letras:
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        lista.append(l)

tam = len(lista)

x = 0
flag = 0
for i in lista:

    if lista[x] != lista[tam-x-1]:
        flag = 1
    x += 1

if flag == 1:
    print("N")
else:
    print("S")