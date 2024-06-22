#Segunda maneira de Resolução do exercicio 4 (sem armazenamento do vetor inteiro)

n = int(input())


contadores = []     #criei 6 contadores (1 a 6) 
i = 1
while i <= 6: 
    contadores.append(0) #mesma coisa que contadores[i] = 0 
    i = i + 1 
#ler os lançamentos
i = 0 
while i < n: 
    atual = int(input())
    contadores[atual] = contadores[atual] + 1 
    i = i + 1 

i = 1 
while i <=6:
    print(contadores[i], end= ' ')
    i = i + 1 