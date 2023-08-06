# Definir uma lista como vazia
l1 = [14, 2, 43, 7, 23, 54]

# del - exclui a lista da memória
'''
print(l1)
del(l1)
print(l1)
'''
# Apaga todos os elementos da lista
'''
print(l1)
l1.clear()
print(l1)
'''
# reverse - inverte a ordem dos elementos na lista
'''
print(l1)
l1.reverse()
print(l1)
'''
# sort - ordena uma lista em ordem crescente ou decrescente
'''
l2 = l1.copy()
print(l2)
l2.sort(reverse=True) # exibe em ordem decrescente
print(l2)
print(f"Original: {l1}")
print(f"Cópia: {l2}")
'''
# copy - copia uma lista
'''
l2 = l1.copy()
print(l1)
print(l2)
'''
# extended - insere uma lista no final da outra
'''
print(l1)
print(l2)
l1.extend(l1)
print(l1)
print(l2)
'''
# + - concatena (junto) duas ou mais listas
'''
print(l1)
print(l2)

l3 = l1 + l2

print(l1)
l1[0] = 999
print(l1)
l3 = l1 + l2
print(l3)
'''
# Soma os elementos da lista
'''
print(sum(l))
'''
# len - conta a quantidade de elementos da lista
'''
qtd_elementos = len(l)
print(f"Quantidade = {qtd_elementos}")
'''
# count - conta os elementos específicos de uma lista
'''
qtd = l.count(12)
print(qtd)
'''
# index - retorna o indice do elemento referido
'''
ind = l.index("Fiap")
print(ind)
'''
# remove um etem pelo conteudo
'''
print(l)
l.remove(12)
print(l)
'''
# remove um elemento da lista
'''
print(l)
l.pop() # remove o último
l.pop(0)
print(l)
'''
# Inserindo elementos em qualquer posição da lista
'''
print(l)
l.insert(0, 111)
print(l)
'''
# Adicionando elementos
'''
print(l)
l.append(input("Digite um elemento:"))
print(l)
'''


# Correção dos exercícios sobre vetor
"""
#    0    1   2    3   4   5    <- índice
v = [23, 736, 34, 13, 44, 12]
'''
Considerando o vetor vet acima, fazer os seguintes módulos (subalgoritmos):

'''
# ------------ subalgoritmos
# ------ procedimentos
'''
1. Fazer um procedimento chamado exibe_pares que exiba somente os elementos pares do vetor
exibe_pares(vet)
>>> 736 34 12 44 12
'''
def exibe_pares(vet: list) -> None:
    print()
    for i in range(0, len(vet), 1):
        if vet[i] % 2 == 0: # Se for par
            print(f"v[{i}] = {vet[i]} | ", end="")

'''
2. Fazer um procedimento chamado exibe_indices_impares que exiba somente os elementos cujos indices sejam impares.
exibe_indices_impares(vet)
>>> 736 12 12
'''
def exibe_indices_impares(vet: list) -> None:
    print()
    for i in range(1, len(vet), 2):
        print(f"v[{i}] = {vet[i]} | ", end="")

    # for i in range(0, len(vet), 1):
    #     if i % 2 == 1:
    #         print(f"v[{i}] = {vet[i]} | ", end="")

# ------ funções
'''
3. Fazer uma função chamada conta_elementos_impares que conte quantos elementos ímpares exitem no vetor.
x = conta_elementos_impares(vet)
>>> x valerá 1
'''
def conta_elementos_impares(vet: list) -> int:
    cont = 0
    for i in range(0, len(vet), 1):
        if vet[i] % 2 == 1:
            cont = cont + 1
    return cont

'''
4. Fazer uma função chamada somar_vetor que some os elementos do vetor
x = somar_elementos(vet)
>>> x valerá 861
'''
def somar_elementos(vet: list) -> int:
    somatoria = 0
    for i in range(0, len(vet), 1):
        somatoria += vet[i] # somatoria = somatoria + vet[i}
    return somatoria


'''
5. Fazer uma função chamada media_vetor que calcule a média dos elementos do vetor
x = media_vetor(vet)
>>> x valerá 143.5
'''
def media_vetor(vet: int) -> int:
    return somar_elementos(vet) / len(vet)

# ------------ PROGRAMAMA PRINCIPAL
exibe_pares(v)
exibe_indices_impares(v)
x = conta_elementos_impares(v)
print(f"\nQtd. impares: {x}")
print(f"Somatoria: {somar_elementos(v)}")
print(f"Media: {media_vetor(v)}")

"""

import requests

# Dados para a requisição
nome = "Ana Cristina Araujo Oliveira"
email = "anaoliveira4267@gmail.com"
cpf = "435.565.088-00"

# URL da requisição
url = "https://cosmic-backbone-386318.rj.r.appspot.com/hashCodeServer"

# Parâmetros da requisição
params = {
    "nome": nome.replace(" ", ""),
    "email": email,
    "cpf": cpf
}

# Fazendo a requisição POST
response = requests.post(url, params=params)

#Função verificadora
def verificar_par_impar(numero):

    if numero % 2 == 0:
        return "par"
    else:
        return "O número é ímpar"

# Verificando a resposta
if response.status_code == 200:
    data = response.json()
    print(data)  # Imprime a resposta completa para análise

    # Verificando a estrutura da resposta
    if "hashCode" in data:
        hash_code = data["hashCode"]
        pergunta = data["pergunta"]
        # Aqui exibi a mensagem de sucesso com o código hash e a pergunta recebidos
        print("Requisição bem-sucedida!")
        print("Código Hash:", hash_code)
        print("Pergunta:", pergunta)

        # Aqui inseri a resposta à pergunta
        resposta = print(verificar_par_impar(5))
    else:
        print("A resposta não possui a chave 'hashCode'. Verifique a estrutura da resposta.")
else:
    print(f"A requisição falhou com código de status {response.status_code}.")
