#LER UMA SEQUENCIA INTEIRA EM UMA LINHA (meu primeiro passo)
sequencia = input().split(' ') #faço a sequencia de strings 
 
i = 0
while i < len(sequencia): #transformo em valores inteiros 
    sequencia[i] = int(sequencia[i])
    i += 1 

i = 0 
blacklist = []  #armazeno numeros que n sao repetidos 
#existe = False-->> serve para verificar se eu vou adc ou n meu valor de sequencia[i] na blacklist 
while i < len(sequencia):
    j = 0 
    existe = False
    while j < len(blacklist):
        if sequencia[i] == blacklist[j]:
            existe = True
        j += 1
    if existe == False:
        blacklist.append(sequencia[i])
    i += 1 
print(blacklist)