import math
'''
sintaxe:
for <contador> in range(inicio, fim, incremento)
    <bloco de repetição>
'''


#FUNCOES FOR
inicio = 0
fim = 40
incr = 3


for cont in range (inicio, fim, incr):
    print(f"{cont} ", end = "")

print()

for cont in range (100, 1 - 1, 1):
    print(f"{cont} ", end = "")

print()

for cont in range (1, 10 + 1, 1):
    print(f"{cont} ", end = "") #end = "" faz com que o print não pule um linha

print()
cont = 0
volta = 1
while volta <= 2:
    n = int(input("Número: "))
    cont = cont + n
    volta = volta + 1
print ("Soma: ", cont)

print()
cont = 0
for volta in range (0, 5, 1):
    n = int(input("Numero: "))
    cont = cont + n
print ("Soma: ", cont)

#ARMAZENR
def exibe_1_10():
    inicio = 0
    fim = 10
    incr = 1

    print()
    for cont in range(inicio, fim, incr):
        print(f"{cont} ", end="")
print("Testando: ")
exibe_1_10()
def exibe_intervalo(i, f, incr):
    print()
    for cont in range(i, f, incr):
        print(f"{cont} ", end="")

inicio = 0
fim = 30
incremento = 3
exibe_intervalo(inicio, fim, incremento)

#FUNÇÃO
#calcular raiz quadrada
def raiz2(n:float) -> float:
    print()
    return n ** (1/2)

print(f"Raiz quadrada: {raiz2(30)}")

resp = math.sqrt(30)
print(f"Raiz quadrada: {resp}")

def maior3n(n1:int, n2:int, n3:int) -> int:
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    return maior

print()

maior = maior3n(4, 9, 10)
print(maior)

maior = max(56,8,15)
print(maior)