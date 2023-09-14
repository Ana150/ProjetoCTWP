#Ana Cristina Araújo - RM99816

tabela =list()
contato =dict()

def preenche_registro(t:list, reg:dict) ->None:
    print("PREENCHENDO O REGISTRO")
    reg['instagram'] =input("Instagram...........: ")
    reg['nome'] =input("Nome..........: ")
    reg['celular'] =input("Celular.......: ")
    t.append(reg.copy())

def exibe_registro(t:list, i:int) ->None:
    print(f"REGISTRO {i}:")
    print("Instagram.......:"+t[i]['instagram'])
    print("Nome......:"+t[i]['nome'])
    print("Celular...:"+t[i]['celular'])
    print()

def exibe_tabela(t:list) ->None:
    qtd_registros =len(t)
    for indice in range(qtd_registros):
        exibe_registro(t, indice)

def preenche_registros(t:list) -> None:
    while True:
        reg = dict()
        reg['instagram'] = input("Instagram (digite '.' para parar): ")
        if reg['instagram'] == '.':
            break
        reg['nome'] = input("Nome: ")
        reg['celular'] = input("Celular: ")
        t.append(reg)

def busca(t: list) -> None:
    instagram = input("Digite o Instagram que deseja consultar: ")
    for reg in t:
        if reg['instagram'] == instagram:
            exibe_registro(t, t.index(reg))
            return
    print("INSTAGRAM NÃO ENCONTRADO!\n")

def cadastroPesquisa(t:list, reg:dict) -> None:
    instagram = input("Digite o Instagram que deseja consultar: ")
    for reg in t:
        if reg['instagram'] != instagram:
            print("cADASTRADO")
            reg['instagram'] =input("Instagram...........: ")
        else:
            print("INSTAGRAM NÃO ENCONTRADO!\n")
while True:
    print("""
0 - SAIR    
1 - CADASTRAR UM CONTATO
2 - EXIBIR OS CONTATOS CADASTRADOS
3 - PREENCHA REGISTROS
4 - CONSULTA REGISTRO
5 - CADATRAR COM PESQUISA
6 - ATUALIZAR""") 

    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 0:
            break
        case 1:
            preenche_registro(tabela, contato)
        case 2:
            exibe_tabela(tabela)
        case 3: 
            preenche_registros(tabela)
        case 4:
            busca(tabela)
        case 5:
            cadastroPesquisa(tabela, contato)
        case _:
            print("Opção inválida!")