#26-(ord(letra)-97)

palavra = input()

soma=0
for letra in palavra:
    soma += 26-(ord(letra)-97)

print(soma)