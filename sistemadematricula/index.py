#MONTANDO O MENU DO RELATORIO FINANCEIRO 
#MENU MONTADO 
def categoria():
    print("INFORME A CATEGORIA: ")
    categoria = input()
    fp = open("categoria.csv", "r")
    leitura_de_linhas = fp.readlines()
    fp.close()
    i = 0
    existe = False 
    while i < len(leitura_de_linhas):
        if leitura_de_linhas[i] == categoria + "\n":    #sempre lembrar do "\n"
            existe = True
        i +=1 
    if not existe:
        fp = open("categoria.csv", "a")
        fp.write(categoria + "\n")
        fp.close()
    else:
        print("CATEGORIA JÁ EXISTE ")


def despesas(): #procedimento identico a montagem do menu principal (sempre lembrar disso)
    cadastrar_as_despesas = True
    while cadastrar_as_despesas:
        print("Informe a despesa que deseja cadastrar: ")
        print("Informe a data da sua despesa: ")
        despesa = float(input())
        data = input()
        fp = open("despesa.csv", "a")
        fp.write(str(despesa) + "-" + data + "\n")
        fp.close()
        print("Voce deseja continuar cadastrando despesas?\n1 - SIM\n2 - NAO")
        opcao = input()
        if opcao == '2':
            cadastrar_as_despesas = False
continua = True
while continua:
    print("1.INFORME A CATEGORIA ")
    print("2.INFORME A DESPESA ")
    print("3.VINCULAR CATEGORIA A DESPESA ")
    print("4.RELATORIO ")
    print("5.SAIR ")
    option = input()

    if option == "5":
        continua = False

    elif option == "1":
        categoria()
    elif option == "2":
        despesas()
    elif option == "3":
        print("Informe a categoria que deseja vincular a despesa: ")
        fp = open("categoria.csv", "r")
        linhas = fp.readlines()
        fp.close()
        i = 0 
        while i < len(linhas):
            print(str(i + 1) + "-" + str(linhas[i].upper()))   #mostro as linhas começando em 1 e n em zero
            i +=1 
        print("Qual a opcao de categoria deseja vincular: ")
        escolha_da_categoria = input()
        categoria_selecionada = linhas[int(escolha_da_categoria) - 1]
        categoria_selecionada =categoria_selecionada.strip()
        #Faço a mesma coisa com as despesas!!
        fp = open("despesa.csv", "r")
        ler_linhas = fp.readlines()
        fp.close()
        i = 0 
        while i < len(ler_linhas):
            print(str(i+1) + "-" + str(ler_linhas[i].upper()))
            
            i +=1
        print("Qual a despesa deseja vincular: ")
        escolha_da_despesa = input()
        despesa_desejada = ler_linhas[int(escolha_da_despesa) - 1]
        despesa_desejada = despesa_desejada.strip()
        
        fp = open("vinculo.csv", "a")
        fp.write(categoria_selecionada + "-" + despesa_desejada + "\n")
        fp.close()
        #PROCURAR POSSÍVEIS ERROS PELO CODIGO INTEIRO
    


    #MONTAGEM DE RELATORIO
    elif option == "4":
        print("Informe um ano de cadastro: ")
        ano_de_cadastro = input()
        fp = open("vinculo.csv", "r")
        ler_vinculo = fp.readlines()
        fp.close()
        i = 0 
        vetor_pega_linhas = []
        vetor_de_despesa = []
        vetor_de_todos_os_gastos = [0] * 13
        while i < len(ler_vinculo):
            vetor_pega_linhas.append(ler_vinculo[i].split("/"))
            vetor_de_despesa.append(ler_vinculo[i].split("-"))
            
            gastos = float(vetor_de_despesa[i][1])
            ano = vetor_pega_linhas[i][2].strip()
            mes = int(vetor_pega_linhas[i][1])
            if ano == ano_de_cadastro:
                vetor_de_todos_os_gastos[mes] += gastos
           
            i +=1
        i = 1 
        while i < len(vetor_de_todos_os_gastos):
           print("Voce gastou {} no mes {}".format(vetor_de_todos_os_gastos[i], i))
           i +=1

            
                              
    