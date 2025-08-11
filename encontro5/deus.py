n = int(input())

palavras = []
for i in range(n):
    p = input()
    palavras.append(p)

for a in palavras:
    lista = list(a)
    flag = 1 # valido
    for x in range(len(lista) - 1):
        if lista[x] in "aeiou" and lista[x+1] in "aeiou":
            flag = 0
            continue
        if lista[x] not in "aeiou" and lista[x+1] not in "aeiou":
            flag = 0
            continue

    if flag == 1:
        print("YES")
    else:
        print("NO")