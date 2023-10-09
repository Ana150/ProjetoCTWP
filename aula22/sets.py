''' SETS - CONJUNTOS
- Armazena apenas itens não duplicados
- Suporta operações matematicas de conjuntos (união, intersecção...)
- Não é possivel modificar os itens existetes, sim adicionar ou remover.
- Suporta elementos de quaisquer tipos (ordenados ou não)
- Podem conter objetos imutáveis como strings
- São delimitados com chaves 
'''
import os
# Criando um conjunto vazio
os.system("clear")
conjunto = set()  # cria um conjunto vazio
print(conjunto)
print("-----------------------------------")

# Criando um set com valores
numeros = [34, 34, 34, 34, 34, 34, 56, 23, 12]
conjunto = set(numeros)
print(numeros)
print(conjunto)
print("-----------------------------------")

# inserindo um elemento em um set
numeros = [1, 2, 2, 3, 3, 3]
conjunto = set()

for num in numeros:
    conjunto.add(num)

print(numeros)
print(conjunto)
print("-----------------------------------")

# removendo um elemento de um set com remove
conjunto = set([1, 2, 2, 3, 3, 3])  # 1 2 3
print(conjunto)
conjunto.remove(2)  # remove um item do conjunto
print(conjunto)
# conjunto.remove(4)
print("-----------------------------------")

# removendo um elemento de um set com discard
conjunto = set([1, 2, 2, 3, 3, 3])  # 1 2 3
print(conjunto)
conjunto.discard(2)  # remove um item do conjunto
print(conjunto)
conjunto.discard(4)
print(conjunto)
print("-----------------------------------")

# removendo todos os elementos de uma vez
conjunto = set([1, 2, 2, 3, 3, 3])  # 1 2 3
print(conjunto)
conjunto.clear()  # remove um item do conjunto
print(conjunto)
print("-----------------------------------")

# =============== OPERAÇÕES MATEMÁTICAS COM CONJUNTOS - SETS
# union - União entre conjuntos
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a.union(b)
print(f"Impares..: {a}")
print(f"Pares....: {b}")
print(f"Todos....: {c}")
print("-----------------------------------")

# | - união entre conjuntos
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a | b
print(f"Impares..: {a}")
print(f"Pares....: {b}")
print(f"Todos....: {c}")
print("-----------------------------------")

# intersection - intersecção entre conjuntos
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a.intersection(b)
print(f"A..: {a}")
print(f"B..: {b}")
print(f"C..: {c}")
print("-----------------------------------")

# & - intersecção entre conjuntos
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a & b
print(f"A..: {a}")
print(f"B..: {b}")
print(f"C..: {c}")
print("-----------------------------------")

# operadores de associação: in
planetas = {"plutão", "marte", "terra", "venus"}
print(planetas)
print("plutão" in planetas)
print("plutão" not in planetas)
print("-----------------------------------")

# casting com conjuntos - sets
#    0  1  2  3  4  5  6  7
a = [0, 0, 1, 1, 3, 5, 7, 9]
a_set = set(a)
print(a)
print(a_set)
aa = list(a_set)
print(a)
print(aa)
print(a_set)
print("-----------------------------------")

# ===================== COMPARAÇÕES ENTRE CONJUNTOS
# igualdade ou diferença de conjuntos
planetas1 = {"terra", "marte", "mercurio", "venus"}
planetas2 = {"terra", "marte", "mercurio", "venus", "jupiter"}
print(planetas1 == planetas2)
print(planetas1 != planetas2)
print("-----------------------------------")

# < verifica se o conjunto à esquerda é um subconjunto da direita
planetas1 = {"terra", "marte", "mercurio", "venus"}
planetas2 = {"terra", "marte", "mercurio", "venus", "jupiter"}
print(planetas1 < planetas2)
print(planetas1 > planetas2)
print("-----------------------------------")

# difference ou -: a diferenca entre dous conjuntos é um conjunto contendo os elementos do conjunto a esquerda que nao estao no conjunto da direita
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
print(planetas1 - planetas2)
print(planetas1.difference(planetas2))
print("-----------------------------------")

# diferença simétrica (^ ou .symmetric_diference - considera apenas os elementos não repetidos
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
print(planetas1 ^ planetas2)
print(planetas1.symmetric_difference(planetas2))
print("-----------------------------------")

# disjunção - não possuem nenhum elemento em comum
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
planetas3 = {"jupiter", "urano", "saturno"}
print(planetas1.isdisjoint(planetas2))
print(planetas1.isdisjoint(planetas3))
print("-----------------------------------")

# união com |= ou metodo update - realiza uma operacao de uniao, mas ordenando aleatoriamente
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
planetas1 |= planetas2
print(planetas1)
print("-----------------------------------")

# pop() - remove um elemento aleatorio
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
print(planetas1)
print(planetas1.pop())
print(planetas1)
print("-----------------------------------")

# copy() - efetua a cópia de uma lista
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = planetas1.copy()
print(planetas1)
print(planetas2)
print("-----------------------------------")

"""
EXERCÍCIOS:
1. Escreva uma função que receba uma lista de elementos e retorne a quantidade de elementos
unicos da lista.
2. Escreva uma função que receba uma lista de elementos duplicados na alista.
"""
