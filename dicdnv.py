#REFAZENDO A QUESTÃO DE DICIONARIO DA LISTA 4 DE VETORES

sequencia = input().split(" ")
dicionario = {}
i = 0
while i < len(sequencia):
    atual = sequencia[i]
    dicionario[atual] = 0
    i +=1

i = 0 
while i < len(sequencia):
    atual = sequencia[i]
    dicionario[atual] += 1
    i += 1
print(dicionario)

chaves = list(dicionario.keys())
print(chaves)

i = 0 
#SEMPRE LEMBRAR DA ULTIMA PARTE DO EXERCICIO EM QUANTIDADE
while i < len(chaves):
    sequencia = chaves[i]
    quantidade = dicionario[sequencia]
    print(sequencia + " ocorreu " + str(quantidade) + " vez(es) ")
    i +=1