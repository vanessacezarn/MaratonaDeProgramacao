n = int(input())
frases = [input() for _ in range(n)]

for frase in frases:
    flag = 1
    palavras = frase.split(' ')
    for p in palavras:
        if len(p) == 1:
            continue
        elif len(p) > 5:
            lista = list(p)
            if (lista[0] not in 'aeiou' and lista[-1] not in 'aeiou') or (lista[0] in 'aeiou' and lista[-1] not in 'aeiou') or (lista[0] not in 'aeiou' and lista[-1] in 'aeiou'):
                flag = 0
                
        elif len(p) <= 5 and len(p) > 1:
            lista = list(p)
            if (lista[0] in 'aeiou' and lista[-1] not in 'aieou') or (lista[0] in 'aeiou' and lista[-1] in 'aieou') or (lista[0] not in 'aeiou' and lista[-1] not in 'aieou'):
                flag = 0
                
        if flag == 0:
            print('NAO')
            break
    if flag == 1:
        print('SIM')