entrada = input().split(' ')
i = 0 
n = int(input())
while i < n:
    respostas = input().split(' ')

    acertos = 0 
    j = 0 
    while j < 6:
        if respostas[j] == entrada[j]:
            acertos += 1 
        j += 1 
    print(acertos)
    i += 1 
