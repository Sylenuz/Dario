notas={
    "joão": [7, 8, 9],
    "maria": [10, 9, 8],
    "Ana": [6, 7, 8]
}

media_notas={aluno: sum(notas)/len(notas) for aluno, notas in notas.items()}
print(media_notas)