arq = open("RM99816.txt", "r")
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
caracteres = "!#$%¨&*()_+{}?:;/\|][]-='"

def validarLogin(login):
    if len(login) > 6 or len(login) < 6:
        print("O login deve ter exatamente 6 caracteres")
    elif login[0] not in numeros:
        print("O login deve começar com 1 numero")
#    elif letras in login:
#        print("Deve haver ao menos 1 letra no login")
    else:
        arq.write(f"{login}\n")
        print("Email e senha salvos!")



def validarEmail(email):
    partes = email.split("@")
    while True:
        if len(partes) != 2:
            print("O email deve conter apenas um @")
        else:
            nome, sobrenome = partes
            
            if nome[0] not in letras or sobrenome[0] not in letras:
                print("O nome e o sobrenome devem comear com letras")
            elif caracteres in nome or caracteres in sobrenome:
                print("Não podem exitir caracteres especiais no email")
            elif sobrenome.count(".") < 1 or sobrenome.count(".") > 2:
                print("A segunda parte do email deve conter 1 ou 2 pontos")
            elif "@." in email or email[-1] == ".":
                print("A segunda parte do email não deve iniciar ou terminar com .")
            elif ".." in email:
                print("não pode haver dois pontos consecutivos")
            else:
                arq.write(f"{email}, ")
                


while True:
    print('''
0 - SAIR
1 - Digite as credências (login e email)
2 - Exibir arquivo''')

    opcao = int(input("Insira a opção desejada: "))
    match opcao:
        case 0:
            break
        case 1:
            email = input("Insira o email: ")
            login = input("Insira o login: ")
            validarEmail(email)
            validarLogin(login)
        case 2:
            texto = arq.read()
            print(f"\n{texto}")