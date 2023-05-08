'''
1. Criar um procediento que passe dois valores referentes a um intervalo e exiba os numeros do intervalo
    intevalo(3,9)
    > > 3 4 5 6 7 8 9

2. Criar um procediento que passe dois valores referentes a um intervalo e a 'A' para aberto e F para fechado
    intevalo(3,9,A)
    4 5 6 7 8
    intervalo(3,9,F)
    3 4 5 6 7 8 9

3. Criar umA FUNÇÃO QUE PEGUE O NUMERO PASSADO POR PARAMETRO E RETORNE O PROXIMO MULTIPLO DE 5
    print(proxMulti5(7)
    > > 10

4. Criar uma função que pegue um numero e o multiplo por parametro e retorne o proximo numero multiplo
    print(proximoMult(16, 7))
    > > 21
'''

'''#EXERCÍCIO 1
#EM PROCEDIMENTO PODEMOS USAR PRINT E INPUT, EM UM FUNÇÃO NÃO!
def numeros(numero1, numero2) -> None:
    for i in range(numero1, numero2 + 1, 1):
        print(f"{i}", end='')


#EXERCÍCIO 2
def abertoFechado(numero1, numero2, alternativa) -> None:
    if alternativa == "F" or alternativa == "f":
        for i in range(numero1+1, numero2, 1):
            print(f"{i}", end='')
    else:
        for i in range(numero1, numero2 + 1, 1):
            print(f"{i}", end='')

#EXERCÍCIO 5
def fatorial(numero1) -> None:
    resultado = 1
    count = 1

    while count <= numero1:
        resultado = resultado * count
        count = count + 1

    print(resultado)

numeros(1,10)
print("")
abertoFechado(1,10,"F")
print("")
fatorial(5)'''

#CORREÇÃO
def intervalo(inicio: int, fim:int) -> None:
    for i in range(inicio, fim+1, 1):
        print(f"{i}", end='')


#RETORNAR PROXIMO MULTIPLO DE 5
def proxMult5(num:int) -> int:
    return  num // 5 * 5 + 5

def proxMult(num:int, mult:int) -> int:
    return num // mult * mult + mult
print()
intervalo(3,9)
print()
print(proxMult5(7))
print(proxMult(7, 6))

def procededimentoPrimo(num: int) -> None:
    cont = 0

    for i in range (1, num + 1, 1):
        if num  % i == 0:
            cont = cont + 1
    if cont == 2:
        print("É primo")
    else:
        print("Não é primo")

procededimentoPrimo(113)

def funcaPrimo(num: int) -> bool:
    cont = 0
    for i in range(2, num,1):
        if num  % i == 0:
            cont = cont + 1
    if cont == 0:
        return (True)
    else:
        return (False)

if funcaPrimo(10):
    print("É primo")
else:
    print("Não é primo")

