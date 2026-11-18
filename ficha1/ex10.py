frase=input("Digite uma frase: ")

letrasRepetidas={}
for letra in frase:
    if letra in letrasRepetidas:
        letrasRepetidas[letra]+=1
    else:
        letrasRepetidas[letra]=1

print(letrasRepetidas)