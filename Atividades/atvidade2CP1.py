#Ana Cristina Araújo Oliveira - RM 99816

dicionario = {
    'Nome': 'Ana Cristina Oliveira',
    'Idade': 19,
    'Telefone': '(11) 95454-5454',
    'Residencia': 'São Paulo'
}

print("\n--------- DICIONÁRIO INICIAL ---------")
for k, v in dicionario.items():
    print(f"{k} ......... {v}")

def exibirRegistro():
    print("\n--------- DICIONÁRIO ATUALIZADO ---------")
    for k, v in dicionario.items():
        print(f"{k} ......... {v}")

def criarRegistro() -> None:
    key = input("Insira a key: ")
    value = input("Insira o value: ")
    dicionario[key] = value

def alterarRegistro(key, arteracao) -> None:
    key = input("Qual key deseja alterar? (Insira o texto, não o índice): ")
    alteracao = input("Qual será o novo conteúdo da key?: ")
    if key in dicionario:
        dicionario[key] = alteracao
    else:
        print("\nKEY INVÁLIDA!!! Você pode selecionar a 2° opção para verificar o conteúdo da key.")

while True:
    opcao = input('''
Escolha a opção desejada:
0 -> SAIR
1 -> Preencher regisitro
2 -> Exibir conteúdo do registro
3 -> Alterar Conteúdo do registro
''')
  
    if opcao.isdigit():
        match int(opcao):
            case 0:
                break
            case 1:
                criarRegistro()
            case 2:
                exibirRegistro()
            case 3:
                alterarRegistro("", "")
            case _:
                print("\nINSIRA UMA OPÇÃO VÁLIDA!!")