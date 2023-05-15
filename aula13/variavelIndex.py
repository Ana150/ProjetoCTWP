#      0    1   2    3   4   5    <- índice
vet = [23, 736, 34, 12, 44, 12]

'''
EXERCÍCIOS:
Considerando o vetor vet acima, fazer os seguintes módulos (subalgoritmos):
1. Fazer um procedimento chamado exibe_pares que exiba somente os elementos pares do vetor
exibe_pares(vet)
>>> 736 34 12 44 12

2. Fazer um procedimento chamado exibe_indices_impares que exiba somente os elementos cujos indices sejam impares.
exibe_indices_impares(vet)
>>> 736 12 12

3. Fazer uma função chamada conta_elementos_impares que conte quantos elementos ímpares exitem no vetor.
x = conta_elementos_impares(vet)
>>> x valerá 1

4. Fazer uma função chamada somar_vetor que some os elementos do vetor
x = somar(vet)
>>> x valerá 861

5. Fazer uma função chamada media_vetor que calcule a média dos elementos do vetor
x = media_vetor(vet)
>>> x valerá 143.5


'''





# ------ SUBALGORITMOS
# --- PROCEDIMENTO
# Este procedimento exibe o vetor na íntegra formatado
def exibe_vetor(v: list) -> None:
    for i in range(0, len(v), 1):
        print(f"V[{i}] = {v[i]}")

# --- FUNÇÃO
# retorne o ultimo elemento do vetor
def ultimo_elemento(v: list) -> int:
    return v[len(v) - 1]


def soma_vetor(v: list) -> int:
    s = 0
    for i in range(0, len(v), 1):
        s = s + v[i]
    return s




# ------ PROGRAMA PRINCIPAL
exibe_vetor(vet)

print(ultimo_elemento(vet))

print(sum(vet))
print(soma_vetor(vet))





'''
print(vet)
print(vet[4])
x = vet[1] + vet[2]
print(x)
if vet[1] > 100:
    print("A posição é maior do que 100")
else:
    print("A posição é menor do que 100")

print(vet)
vet[1] = 12
print(vet)
'''