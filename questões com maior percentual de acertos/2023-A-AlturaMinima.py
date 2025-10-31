qtd, h = map(int, input().split())
brinquedos = [int(x) for x in input().split()]

cont = 0
for i in range(qtd):
    if brinquedos[i] <= h:
        cont += 1

print(cont)