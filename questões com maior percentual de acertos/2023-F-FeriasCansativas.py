D, C, R = map(int, input().split())

listaC = []
listaR = []

for i in range(C):
    listaC.append(int(input()))

for i in range(R):
    listaR.append(int(input()))


cont = 0
while listaC or listaR:

    if listaC and D >= listaC[0]:        
        D = D - listaC[0]
        listaC.pop(0)
        cont += 1

    elif listaR:
        D = D + listaR[0]
        listaR.pop(0)
        cont += 1

    else:
        break

print(cont)