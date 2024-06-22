# "−1 0 0 0 5 0 5 −1 2 −5 0"
numeros = input().split(" ")


dic = {}
i = 0
while i < len(numeros):#    i = 0       |    i = 1       |  i = 2
    atual = numeros[i] # atual = "-1"   | atual = "0"    |  atual = "0" 
    dic[atual] = 0     # dic['-1'] = 0  | dic['0'] = 0   |  dic['0'] = 0
    i += 1             # {"-1":0}       | {"-1":0,"0":0} |  {"-1":0,"0":0}    



# dic['-1'] = 0
# dic['3'] = 0
# dic['0'] = 0
# dic['5'] = 0
# dic['2'] = 0
# dic['-5'] = 0
# dic.keys -> ['-1','3','0','5','2','-5']

# "−1 0 0 5 0 5 −1 2 −5 0"
i = 0
while i < len(numeros): # i = 0         # i = 1        # i = 2
    # atual = -1, 3     
    atual = numeros[i]  # atual = "-1"  # atual = "0"  # atual = "0"
    dic[atual] += 1     # dic["-1"] = 1 # dic["0"] = 1 # dic["0"] = 2
    i += 1

chaves = list(dic.keys())
print(chaves)
i = 0
# dic = {"-1":2,"0":4,"5":2,"2":1,"-5":1}
# dic.keys() = ["-1","0","5","2","-5"]
# chaves = ["-1","0","5","2","-5"]
while i < len(chaves):
    numero = chaves[i] # '-1'
    quantidade = dic[numero] # dic['-1'] = 2 
    print(numero + " aconteceu " + str(quantidade) + " vezes")
    i += 1

print(dic)
print(chaves)
