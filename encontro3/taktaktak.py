senha = input()
resultado = []
resposta = "-1"

tam = len(senha)

for pulo in range(1, tam+1): #comentar aqui depois
    if tam % pulo == 0:
        blocos = []
        for i in range(0, tam, pulo):
            blocos.append(senha[i:i+pulo])
        #blocos = [senha[i:i+pulo] for i in range(0, tam, pulo)]
        resultado.append(blocos)    
#print(resultado)

flag = 0
for bloco in resultado:
    if len(bloco) == 1:
        continue  # pula blocos únicos

    elemento0 = bloco[0]
    iguais = True
    for i in range(1, len(bloco)):  # Começa do 1, ignora o próprio elemento0
        elemento = bloco[i]
        if elemento != elemento0:
            iguais = False
            break
    if iguais:
        resposta = bloco[0]
        flag = 1
        break
print(resposta)