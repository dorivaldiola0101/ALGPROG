#refazendo o exercicio da lista da professora de programação 

m = int(input("Informe o menor numero m: "))
n = int(input("Informe o maior numero n: "))

for i in range(m+1, n):
    print(f"A lista de divisores de {i} é igual a: ")
    for divisores in range(1,i+1):
        if i % divisores ==0:
            print(divisores, end= " ")

    print("\n")