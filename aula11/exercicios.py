#EXERCICIO 2
''''
digitar os numero(repete)
somar os numeros(repete)
apresentar a somatoria(nao repete)


VARIAVEL CONTADORA
var = var + valor
x = x + 1
VARIAVEL ACUMULADORA
var = var + outra_var
x = x+ n'''

#inicio do laço - REPITA
'''soma = 0
while True:
    n = float(input("Número: "))
    soma = soma + n
    if n == 0:
        break

print(f"Somatória: {soma}")'''

#inicio do laço - ENQUATO
'''soma = 0
n = 1
while n != 0:
    n = float(input("Número: "))
    soma = soma + n'''

#EXERCÍCIO 2v2
'''soma = 0
n = 1
while n >= 0:
    n = float(input("Número: "))
    if n > 0:
        soma = soma + n
    else:
        print("Insira um número positivo")'''

#EXERCICIO 3
'''#for i in range(inicio, final, incremento)
tab = int(input("Taboada: "))
m = int(input("Multiplicador: "))
for i in range(1, m+1, 1):
    mult = tab * i
    print(f"{tab} X {i} = {mult}")'''

'''
multiplicar os numeros
apresentar em formato de taboada'''

#EXERCICIO 4
'''Em uma votação existem 3 candidato
Pedir e acumular votos ate que em votos seja digitado O
Exibir a quantiddae de votos de cada no final
while True:
    print("""
        1 - HUGUINHO
        2 - ZEZINHO
        3 - LUIZINHO
    """)
    voto = int(input("Voto: "))
    c1 = c2 = c3 = c4 = 0
    match voto:
        case 0:
            break
        case 1:
            #c1 = c1 + 1
            c1 += 1
        case 2:
            c1 += 1
        case 3:
            c3 = c3 + 1
        case _:
            c4 = c4

    print(f"""
            1 - HUGUINHO - {c1} votos
            2 - ZEZINHO  - {c2} votos
            3 - LUIZINHO - {c3} votos
            4 - NULOS    - {c4} votos""")
'''

c1 = c2 = c3 = c4 = 0
while True:
    print("""
    1 - HUGUINHO
    2 - ZEZINHO
    3 - LUIZINHO
    0 - TERMINO DA VOTAÇÃO
    """)
    voto = int(input("Voto: "))

    match voto:
        case 0:
            break
        case 1:
            # c1 = c1 + 1
            c1 += 1
        case 2:
            c2 = c2 + 1
        case 3:
            c3 = c3 + 1
        case _:
            c4 = c4 + 1

    soma = c1+c2+c3+c4
    percentual1 = (soma * 100) / c1
    percentual2 = (soma * 100) / c2
    percentual3 = (soma * 100) / c3
    percentual4 = (soma * 100) / c4
    print(f"""
    1 - HUGUINHO - {c1} votos -> O candidato conseguiu {int(percentual1)}% dos votos
    2 - ZEZINHO  - {c2} votos -> O candidato conseguiu {int(percentual2)}% dos votos
    3 - LUIZINHO - {c3} votos -> O candidato conseguiu {int(percentual3)}% dos votos
    4 - NULO     - {c4} votos -> O candidato conseguiu {int(percentual4)}% dos votos
    """)

