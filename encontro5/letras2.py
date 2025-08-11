n = int(input())
frases = [input() for _ in range(n)]

for frase in frases:
    flag = 1
    palavras = frase.split()

    for p in palavras:
        if len(p) == 1:
            continue

        elif len(p) > 5:
            if p[0] not in 'aeiou' or p[-1] not in 'aeiou':
                flag = 0
                break

        else:
            if p[0] in 'aeiou' or p[-1] not in 'aieou':
                flag = 0
                break

    if flag == 0:
        print('NAO')
    else:
        print('SIM')    
    

