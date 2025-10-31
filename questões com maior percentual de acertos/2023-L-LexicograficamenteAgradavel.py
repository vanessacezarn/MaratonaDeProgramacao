S = input()
K = int(input())

lista = []
for i in range(len(S) - K):
    nova = S
    nova = S[:i] + S[i+K] + S[i+1:i+K] + S[i] + S[i+K+1:]
    
    lista.append(nova)


print(lista)

