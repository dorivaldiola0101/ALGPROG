n = int(input()) #quantidade de lançamentos do dado viciado 
i = 0 
dados = [] 
while i < n:    #ler cada lançamento de dados 
    faces = int(input())
    dados.append(faces)
    i = i  + 1

i = 1   #novo inicializador, agora para as faces do dado 
while i <= 6:   #laço que caminha pelas faces do dado, vendo quantas vezes cada face ocorre  
    j = 0   
    ocorrencia = 0 
    while j < n:
        if dados[j] == i: #entro no meu vetor dados e e caminho por por ele pela posição do contador
            ocorrencia = ocorrencia + 1 
        j = j + 1 
    print(ocorrencia, end=' ')
    i = i + 1 
