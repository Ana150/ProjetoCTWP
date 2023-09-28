#Ana Cristina Araújo Oliveira - RM 99816

def validar_email(email):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    especiais = "!'\"#$%&()*+,-./:;<=>?@[\\]^_`{|}~´§"

    partes = email.split("@")
    
    if len(partes) != 2:
        print("O email deve conter um caractere '@'.")
    else:
        nome, sobrenome = partes
        if not nome or not sobrenome:
            print("O nome e o sobrenome não podem estar vazios.")
        elif nome[0] not in letras or sobrenome[0] not in letras:
            print("O nome e o sobrenome devem começar com uma letra.")
        elif especiais in nome or especiais in sobrenome:
            print("O nome e o sobrenome não podem conter caracteres especiais.")
        elif sobrenome.count(".") < 1 or sobrenome.count(".") > 2:
            print("O sobrenome deve conter um ou dois pontos.")
        elif "@." in email or email[-1] == ".":
            print("O ponto não pode estar no início ou no final do sobrenome.")
        elif ".." in email:
            print("Não pode haver pontos consecutivos no sobrenome.")
        else:
            arq = open("RM99816.txt","a")
            arq.write(f"\nEmail: {email}")

while True:
    print("""
0 - SAIR    
1 - CADASTRAR UM EMAIL""") 

    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 0:
            break
        case 1:
            email = input("Informe o email: ")
            validar_email(email)
        case _:
            print("Opção inválida!")