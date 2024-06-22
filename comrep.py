sequencia = input().split(' ')
#-1 0 -1 -1 -1 3
i = 0 
repetidos = {}
while i < len(sequencia): #    i = 0             |    i = 1       |  i = 2
    atual = sequencia[i]  # atual = "-1"         | atual = "0"    |  atual = "0" 
    repetidos[atual] = 0  # repetidos['-1'] = 0  | dic['0'] = 0   |  dic['0'] = 0
    i += 1                 # {"-1":0}       | {"-1":0,"0":0} |  {"-1":0,"0":0}    

i = 0 
while i < len(sequencia):
    atual = sequencia[i]
    repetidos[atual] += 1
    i += 1
chaves = list(repetidos.keys())
print(chaves)

i = 0
resultado = [] 
while i < len(chaves):
    if repetidos[chaves[i]] > 1:
        resultado.append(chaves[i])
    i += 1
print(resultado)
