def soma(x):
    return (x+1)%10
def sub(x):
    return (x-1)%10

t = int(input())
atual = [int(x) for x in input().split(' ')]
senha = [int(x) for x in input().split(' ')]



contador = 0 # variavel acumuladora

anti_horario = atual.copy() #inicia input original
horario = atual.copy()
certo = [] # armazena os valores corretos
for c in range(1,t+1):
    i = -1 # praticidade, pegar ultimo da lista

    if c != 1: #depois da primeira iteração ele sempre atualiza os valores
        anti_horario = certo.copy()
        horario = certo.copy()

    while True:
        if anti_horario[i] != senha [i]: 
            anti_horario = sub(anti_horario) # se nao bate valor, anda 1
        else:
            acumuladora -= 1
            certo = anti_horario
            certo.pop(i)
            senha.pop(i)
        
        if horario[i] == senha [i]: # se nao bate valor, anda 1
            horario = soma(horario)
        else:
            acumuladora += 1
            certo = horario
            certo.pop(i)
            senha.pop(i)
            

