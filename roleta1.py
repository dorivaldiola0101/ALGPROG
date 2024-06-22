n = int(input())
i = 0 
roleta = []
frequencia = [0] * 37
while i < n:
    numeros = int(input())
    roleta.append(numeros)
    i += 1 
i = 0 
while i < n:
    frequencia[roleta[i]] += 1 
    i += 1 
print(frequencia)