entrada = input().split(' ')
i = 0 
while i < len(entrada): #conversão das strings para inteiros 
    entrada[i] = int(entrada[i])
    i += 1 
menor = 0 
i = 0  
while i < len(entrada):
    if i == 0:
        menor = entrada[i]
    else:
        if entrada[i] < menor:
            menor = entrada[i]
    
    i += 1 
print(menor)