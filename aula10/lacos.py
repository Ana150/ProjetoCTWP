#LAÇO PRÉ-DETERMINADO

#Ler valor inicial
n1 = int(input("Digite o valor inicial: "))

#Ler valor final
n2 = int(input("Digite o valor final: "))

'''#Inicio do laço
while n1 <= n2:
    #exibir os números
    print(n1)

    #somar 1 ao próximo
    n1 = n1 + 1
else:#é executado quando não há interferência no laço
    print("Tudo certo")
#Final do laço'''

'''#EXERCICIO LAÇO FECHADO
if n1 > n2:
    print("O segundo número deve ser menor que o primeiro")
else:
    n1 = n1 + 1
    n2 = n2 - 1
    while n1 <= n2:
        # exibir os números
        print(n1)

        # somar 1 ao próximo
        n1 = n1 + 1'''

#While True
'''while True:
    print(n1)
    n1 = n1 + 2
    print("Executou o bloco")
    if n1 > n2:
        break'''

'''opcao = "S"
while opcao == "S":
    n1 = int(input("Digite o valor inicial: "))
    n2 = int(input("Digite o valor final: "))

    while n1 <= n2:
        print(n1)
        n1 = n1 + 2

    opcao = input("Deseja continuar (S/N)?: ").upper()
    while opcao.upper() != 'S' and opcao.upper() != 'N':
        print("Erro! Digite S ou N")
        opcao = input("Deseja continuar (S/N)?: ")'''