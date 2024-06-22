gabarito = input().split(' ')   #indica a leitura do gabarito 
i = 0 
n = int(input('Digite a quantidade de provas ')) #indica a qdade de provas/alunos

while i < n:    #controla a prova que será lida 
    provas = input().split(' ')         
    acertos = 0 
       
    j = 0       #variavel de controle para o inicio do segundo laço 
    while j < 6:    #controla a verificação do gabarito 
        if provas[j] == gabarito[j]:
            acertos = acertos + 1 
        j = j + 1   #passo do segundo laço 
    print(acertos)
    i += 1 
    