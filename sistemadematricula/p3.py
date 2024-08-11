#montagem do sistema de menu do cadastramento
def cadastramento ():
    print("Inicio do cadastramento de aluno")
    #Inicio do cadastro dos alunos 
    print("Informe o nome do aluno: ")
    print("Informe a data de nascimento do aluno: ")
    print("Informe o curso do aluno: ")
    aluno = input()
    nascimento = input()
    curso = True
    while curso:
        print("(0) Ciencias da computação")
        print("(1) Engenharia da Computação")
        print("(2) Engenharia de Software")
        print("(3) Sistema de Informação")
        print("(4) Outros cursos")
        print("(5) Sair")
        escolha = input()
        if escolha == "0" or escolha == "1" or escolha == "2" or escolha == "3" or escolha == "4":
            fp = open("alunos.csv", "a")
            fp.write(aluno + "," + nascimento + "," + escolha +"\n")
            fp.close()
        
        elif escolha == "5":
            curso = False
continua = True
while continua:
    print("(1) Nome do aluno, nascimento, curso")
    print("(2) Opiniao sobre o aluno cadastrado")
    print("(3) Relatorio ")
    print("(4) Saída")
    option = input()

    if option == "1":
        cadastramento()
    
    elif option =="2":
        
        fp = open("alunos.csv", "r")
        linhas = fp.readlines()
        fp.close()
        i = 0
        vetor_quebra = []
        while i < len(linhas):
            vetor_quebra.append(linhas[i].split(","))
            i +=1
        i = 0
        while i < len(linhas):
            print(str(i+1) + "-" + str(vetor_quebra[i][0].upper()))
            i +=1
        print("Informe qual aluno deseja escolher:")
        escolha_de_alunos = input()
        alunos = vetor_quebra[int(escolha_de_alunos) - 1]
        

            


    elif option == "3":
        print("Gerar um relatorio do aluno")
    elif option == "4":
        print("Aqui é a sua saída")
        continua = False
    else:
        print("Entrada Invalida!")