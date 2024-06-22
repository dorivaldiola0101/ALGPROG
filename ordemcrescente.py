#5 7 2 10
#2 7 5 10       #2 5 7 10
entrada = input().split(' ')
i = 0 
while i < len(entrada): #conversao de string p inteiro 
    entrada[i] = int(entrada[i])
    i += 1 

#agora é necessario pegar o menor numero
i = 0
print(entrada)
menor = entrada[0]  
while i < len(entrada):
    j = 0 
    print('ESSE É O VALOR DE ENTRADA NA POSIÇÃO I =', entrada[i])
    while j < len(entrada):
        print('ESSE É O VALOR DE ENTRADA NA POSIÇÃO J =' , entrada[j])
        if entrada[i] < entrada[j]:
            aux = entrada[i]
            entrada[i] = entrada[j]
            entrada[j] = aux
        j += 1 
    i += 1
print(entrada)
