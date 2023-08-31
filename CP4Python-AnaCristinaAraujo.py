#Ana Cristina Araújo Oliveira - RM 99816
nome = "Ana Cristina Araújo"

def nomeCompleto() -> None:
    nomeCplt = input("Insira um nome completo: ")

def nomeSeparado():
    def quebrar_frase(nome: str) -> list:
        lista_nome = nome.split()
        return lista_nome
            
    def palavras_nome(lista_nome: list) -> None:
        ind = lista_nome[0]
        for elem in lista_nome:
            if ind == 0:
                print(f"NOME: {lista_nome[ind]}")
                ind = ind + 1
            else:
                print(f"SOBRENOME: {lista_nome[ind]}")
                ind = ind + 1

    print(palavras_nome(quebrar_frase(nome)))
    
def contar_palavras(lista_nome: list) -> None:
    qtd = 0
    for elem in lista_nome:
        qtd += 1
    return qtd

def bibliografia(lista_nome) :
    lista = lista_nome.split()
    indice = lista[-1]
    print(f"\n{indice.upper()}, {lista_nome}")

while True:
    print('''\nESCOLHA A OPÇÃO DESEJADA:
0 - SAIR
1 - Digite um nome completo
2 - Exibe separado o "nome" do "sobrenome"
3 - Conta quantas palavras há no "nome completo"
4 - Exibir em formato de bibliografia''')
    opcao = input("\nDigite a opção desejada: ")

    if opcao.isdigit():
        match int(opcao):
            case 0:
                break
            case 1:
                nomeCompleto()
            case 2:
                nomeSeparado()
            case 3:
                print(f"Há: {contar_palavras(quebrar_frase(nome))} palavras no nome")
            case 4:
                bibliografia(nome)
            case _:
                print("\nOpção inválida, digite um item de 0 a 4")
    else:
        print("Digite um número!")

    