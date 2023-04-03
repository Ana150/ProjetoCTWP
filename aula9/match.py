#match case

print('''ESCOLHA A OPÇÃO DESEJADA:
1 - Cadastrp
2 - Consulta
3 - Alteração
4 - Exclusão''')
opcao = input("Digite a opção desejada: ")

if opcao.isdigit():
    match int(opcao):
        case 1:
            print("Efetuando cadastro")
        case 2:
            print("Efetuando cadastro")
        case 3:
            print("Efetuando cadastro")
        case 4:
            print("Efetuando cadastro")
        case _:
            print("Opção inexistente. Escolha um número de 1 a 4!")
else:
    print("Digite um número!")