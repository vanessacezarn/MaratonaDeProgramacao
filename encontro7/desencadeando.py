def soma(x):
    return (x+1)%10
def sub(x):
    return (x-1)%10

t = int(input())
atual = [int(x) for x in input().split(' ')]
senha =[int(x) for x in input().split(' ')]

anti_horario = atual.copy()
horario = atual.copy()

contador = 0
certo = []
for c in range(1,t+1):
    i = -1

    if c != 1:
        anti_horario = certo.copy()
        horario = certo.copy()

    while True:

        if anti_horario[i]!= senha [i] and horario[i]!=senha[i]:
            anti_horario = [sub(x) for x in anti_horario]
            horario = [soma(x) for x in horario]
        elif anti_horario[i]== senha [i]:
            anti_horario.pop(-1)
            senha.pop(-1)
            certo = anti_horario.copy()
            break
        elif horario[i]== senha [i]:
            horario.pop(-1)
            senha.pop(-1)
            certo = horario.copy()
            break

        contador = contador + 1

print(contador)