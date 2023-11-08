#Ana Cristina Araújo Oliveira | RM 99816
database = []

# Registros iniciais
registro1 = {"Nome": "Ana", "Email": "ana@email.com", "Telefone": "987654321", "Idade": 28}
registro2 = {"Nome": "Carlos", "Email": "carlos@email.com", "Telefone": "123456789", "Idade": 35}
registro3 = {"Nome": "Sara", "Email": "sara@email.com", "Telefone": "555555555", "Idade": 22}

database.append(registro1)
database.append(registro2)
database.append(registro3)

def cadastrar_registro():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    idade = int(input("Digite a idade: "))
    registro = {"Nome": nome, "Email": email, "Telefone": telefone, "Idade": idade}
    database.append(registro)
    print("Registro cadastrado com sucesso!")

# Função para consultar registros
def consultar_registros():
    contador = 1
    for registro in database:
        print(f"\nRegistro {contador}:")
        for campo, valor in registro.items():
            print(f"{campo}: {valor}")
        contador += 1

def atualizar_registro():
    index = int(input("Digite o número do registro que deseja atualizar: ")) - 1
    if 0 <= index < len(database):
        campo = input("Digite o nome do campo que deseja atualizar (Nome, Email, Telefone, Idade): ")
        if campo in database[index]:
            novo_valor = input(f"Digite o novo valor para {campo}: ")
            database[index][campo] = novo_valor
            print("Registro atualizado com sucesso!")
        else:
            print("Campo inválido.")
    else:
        print("Registro não encontrado.")

def excluir_registro():
    index = int(input("Digite o número do registro que deseja excluir: ")) - 1
    if 0 <= index < len(database):
        del database[index]
        print("Registro excluído com sucesso!")
    else:
        print("Registro não encontrado.")

while True:
    print("""
0 - SAIR    
1 - CADASTRAR REGISTRO
2 - CONSULTAR REGISTRO
3 - ATUALIZAR REGISTRO
4 - EXCLUIR REGISTRO""") 

    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 0:
            break
        case 1:
            cadastrar_registro()
        case 2:
            consultar_registros()
        case 3: 
            atualizar_registro()
        case 4:
            excluir_registro()
        case _:
            print("Opção inválida!")