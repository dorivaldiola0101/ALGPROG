#exercicio 9 da lista 4 de prog resolvido com o uso de dicionario 
#1 2 1 1 0 3 (entrada)
#0 1 2 3 (saida)
sequencia = input().split(' ')
i = 0 
nao_repetidos = {}
while i < len(sequencia):
    atual = sequencia[i]
    nao_repetidos[atual] = 0
    i += 1

i = 0 
while i < len(sequencia):
    atual = sequencia[i]
    nao_repetidos[atual] += 1
    i += 1
chaves = list(nao_repetidos.keys())
print(chaves)

i = 0
semrep = []
while i < len(chaves):
    if nao_repetidos[chaves[i]] == 1 :
        semrep.append(chaves[i])
    i += 1
print(semrep)