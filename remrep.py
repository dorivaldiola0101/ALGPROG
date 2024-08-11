#LER UMA SEQUENCIA SEM REPETIÇÕES CRIANDO UMA FUNÇÃO CHAMADA REMREP PARA SER UTILIZADA PARA PEGAR AS REPETIÇÕES

#Inicialmente devemos ler uma sequencia de numeros e transformá-los em inteiros, para isso utilizamos um laço 

numeros = input().split(" ")
i = 0
while i < len(numeros):
    numeros[i] = int(numeros[i])
    i +=1

#Agora devemos começar a organizar uma forma de ir eliminando os numeros repetidos
i = 0 
blacklist = [] #Será utilizada para armazernar os numeros que serão repetidos
while i < len(numeros):
    j = 0 
    existe = False
    while j < len(blacklist):
        if numeros[i] == blacklist[j]:
            existe = True
        j +=1

    if existe == False:
        blacklist.append(numeros[i])
    i +=1
print(blacklist)
