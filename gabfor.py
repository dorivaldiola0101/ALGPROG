#Exercicio Resolvido com for (treinamento)

gabarito = input().split()
qdade_provas = int(input())
for i in range(qdade_provas):
    acertos = 0
    respostas = input().split() 
    for i in range(6):
        if respostas[i] == gabarito[i]:
            acertos+=1
    print(acertos)
            