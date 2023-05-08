#ARMAZENA VÁRIOS VALORES EM UMA MESMA VARIÁVEL
#CONHECIDO TAMBÉM COMO VETOR OU LISTA
'''
vetorNomes = ["Ana","Lais", "Maria"]
print(vetorNomes[1])

vetorNumeros = [0,1,2,3,4,5,6,7,8,9,10]
print(vetorNumeros[10])
x = vetorNumeros[1] + vetorNumeros[2]
print(x)
if vetorNumeros[1] > 100:
    print("O vetor 1 é maior que 100")
else:
    print("O vetor 1 é menor que 100")

print(vetorNumeros[1])
vetorNumeros[1] = 145
print(vetorNumeros[1])'''

vetorNumeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#PROCEDIMENTO
def exibe_vetor(v: list) -> None:
    for i in range(0, len(v), 1):
        print(f"V[{i}] = {v[i]}")

#FUNCAO
def ultimo_elemento(v:list) -> int:
    return v[len(v) - 1]

def soma_vetor(v: list) -> int:
    s = 0
    for i in range(0, len(v), 1):
        s = s + v[i]
        return s
#programaPrincipal
#a cada volta exibe-se 1 numero do vetor
'''for i in range(0,5,1):
    print(vetorNumeros[i])'''

exibe_vetor(vetorNumeros)

print(ultimo_elemento(vetorNumeros))
print(sum(vetorNumeros))
print(soma_vetor(vetorNumeros))