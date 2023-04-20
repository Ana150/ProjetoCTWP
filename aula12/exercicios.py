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

#EXERCÍCIO 1
def numeros(numero1, numero2) -> None:
    for i in range(numero1, numero2 + 1, 1):
        print(f"{i}")

#EXERCÍCIO 2
def abertoFechado(numero1, numero2, alternativa) -> None:
    if alternativa == "S":
        for i in range(numero1+1, numero2, 1):
            print(f"{i}")
    else:
        for i in range(numero1, numero2 + 1, 1):
            print(f"{i}")

#EXERCÍCIO 5
def fatorial(numero1) -> None:
    resultado = 1
    count = 1

    while count <= numero1:
        resultado = resultado * count
        count = count + 1

    print(resultado)
#EXERCÍCIO 6
def primo(numero1) -> None:
    if numero1 >= 1:
        for i in range(1, numero1):
            if numero1 % i != 0:
                print(numero1, 'é primo')
            else:
                print(numero1, 'não é primo')
                break

#numeros(1,10)
#abertoFechado(1,10,"F")
fatorial(5)
primo(5)