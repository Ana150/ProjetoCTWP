#Ana Cristina Araújo Oliveira - RM: 99816

arq = open("dados.txt", "r")
arqLogin = open("login.txt", "w")
arqEmail = open("email.txt", "w")

for linha in arq:
    partes = linha.strip().split(", ")
    if len(partes) == 2:
        login = partes[0]
        email = partes[1]
        arqLogin.write(login + "\n")
        arqEmail.write(email + "\n")

arq.close()

arqLogin = open("login.txt", "r")
linhasLogin = arqLogin.read()
print(f"login.txt:\n{linhasLogin}")
arqLogin.close()

arqEmail = open("email.txt", "r")
linhaEmail = arqEmail.read()
print(f"email.txt: \n{linhaEmail}")
arqEmail.close()