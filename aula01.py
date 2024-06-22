entrada = input('Digite uma palavara para ser transformada em numero ')
cont = 0 
convertido = []
while cont < 8:
    if entrada[cont] == 'A' or entrada[cont] == 'B' or entrada[cont] == 'C':
        convertido.append(2)
    elif entrada[cont] == 'D' or entrada[cont] == 'E' or entrada[cont] == 'F':
        convertido.append(3)
    elif entrada[cont] == 'G' or entrada[cont] == 'H' or entrada[cont] == 'I':
        convertido.append(4)
    elif entrada[cont] == 'J' or entrada[cont] == 'K' or entrada[cont] == 'L':
        convertido.append(5)
    elif entrada[cont] == 'M' or entrada[cont] == 'N' or entrada[cont] == 'O':
        convertido.append(6)
    elif entrada[cont] == 'P' or entrada[cont] == 'Q' or entrada[cont] == 'R' or entrada[cont] == 'S':
        convertido.append(7)
    elif entrada[cont] == 'T' or entrada[cont] == 'U' or entrada[cont] == 'V':
        convertido.append(8)
    elif entrada[cont] == 'W' or entrada[cont] == 'X' or entrada[cont] == 'Y'or entrada[cont] == 'Z':
        convertido.append(9)

    cont += 1 

i = 0 
while i < 8:
    print(convertido[i], end='')
    i = i + 1 