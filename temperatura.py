n = int(input())
temperaturas = [] #temperaturas = list()

i = 0 
soma = 0 
while i < n:
    temperatura = float(input())
    temperaturas.append(temperatura)
    soma = soma + temperatura
    i = i + 1 

media = soma/n

#Agora o conjunto de temperaturas está disponível!
#Agora é necessário comparar as temperaturas com a média(temos ambos)

i = 0 
while i < n:
    if temperaturas[i] > media :
        print('A temperatura ficou acima da média no dia ' + str(i), end= '.')
    i += 1 
