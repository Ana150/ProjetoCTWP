# ARQUIVOS
# Abertura modo 'w'. Este modo permite abrir o aquivo para Escrita (gravação)
'''
Função: open() - Função para abrir arquivo.
SINTAXE: 
    <objeto> = open("<arquivo_físico>","<modo_abertura", ...)
    <objeto> ==> nome do arquivo utilizado dentro do programa
    <arquivo_fisico> ==> nome do arquivo que será gravado no disco
    <modo_abertura> ==> forma em que o arquivo será aberto
    ... ==> outros parâmetros (utilizaremos posteriormente)
'''
import os
os.system("cls")
# =========> GRAVAÇÃO DE ARQUIVOS
# Abre o arquivo em modo escrita
arq = open("arq1.txt","w")
# Grava a orimeira linha no arquivo
arq.write("Gravando a linha 1.\n")
arq.write("Gravando a linha 2.\n")
arq.write("Gravando a linha 3.\n")
arq.close()

# Abre o arquivo em modo escrita
arq = open("arq2.txt","w", encoding="utf-8")
for i in range(1,10,1):
    arq.write(f"Gravação da linha {i}\n")
arq.close()

# Gravando uma lista
arq = open("arq3.txt","w", encoding="utf-8")
# Gravando a lista bruta
lista = ["Edson", 49, "Rua tal"]
arq.write(f"Gravação da lista bruta: {lista}\n")
# Gravando cada item da lista
arq.write(f"Nome........: {lista[0]}\n")
arq.write(f"Idade.......: {lista[1]}\n")
arq.write(f"Endereço....: {lista[2]}\n")
arq.close()

# Gravando um dicionário
contato = {
    "nome": "Edson de Oliveira",
    "idade": 49,
    "endereco": "Rua tal"
}
arq = open("arq4.txt","w", encoding="utf-8")
# Gravando o dicionário de forma bruta
arq.write(f"Gravação o dicionário de forma bruta: \n{contato}\n")
# Gravando cada item do dicionário
arq.write(f"Nome........: {contato['nome']}\n")
arq.write(f"Idade.......: {contato['idade']}\n")
arq.write(f"Endereço....: {contato['endereco']}\n")
arq.close()

print("Arquivos gravados com sucesso!!")

# =========> ABERTURA DE ARQUIVOS
arq = open("arq4.txt","r", encoding="utf-8")
print(arq.read()) # read carrega o arquivo integral
arq.close()

# Exercicio: usar o try except para tratar o erro de não existir o arquivo

# =========> EDIÇÃO DE ARQUIVOS
# modo ´a´ - Append
arq = open("arq4.txt","a", encoding="utf-8")
arq.write("inserindo uma nova linha")
arq.close()
arq = open("arq4.txt","r", encoding="utf-8")
print(arq.read()) # read carrega o arquivo integral
arq.close()

# =========> MODO ESCRITA EXCLUSIVA
# modo 'x' - exclusivo
# arq = open("arq6.txt","x", encoding="utf-8")
# arq.write("inserindo uma nova linha")
# arq.close()

# =========> Abertura modo escrita e leitura
# modo '+' - exclusivo
os.system("cls")
arq = open("arq7.txt","w+", encoding="utf-8")
arq.write("inserindo uma nova linha")
arq.flush()
arq.seek(5)
# print(arq.read()) # read carrega o arquivo integral
arq.close()

# ==========> MÉTODOS PARA MANIPULAÇÃO DE ARQUIVOS
# Abre o arquivo em modo escrita
arq = open("arq8.txt","w+")
# Grava a primeira linha no arquivo
arq.write("Gravando a linha 1.\n")
arq.write("Gravando a linha 2.\n")
arq.write("Gravando a linha 3.\n")
arq.seek(0)
tamanho_linha = len(arq.readline())
arq.seek(tamanho_linha + 1)
print(arq.readline())



# Exercicio: como exibir somente a linha 3 usando readline?

arq.write("Gravando a linha 1.\n")
arq.write("Gravando a linha 2.\n")
arq.write("Gravando a linha 3.\n")
arq.seek(0)
tamanho_linha = len(arq.readline())
arq.seek(tamanho_linha + 1)
print(arq.readline())
arq.close()

# método readlines()
os.system("cls")
print('---------------------------')
arq = open("arq8.txt","r+")
arq.write("Gravando a linha 1.\n")
arq.write("Gravando a linha 2.\n")
arq.write("Gravando a linha 3.\n")
arq.seek(0)
linhas = arq.readlines()
print(linhas)
print(linhas[1])
print('---------------------------')

# Exercício.
# Grave diversas linhas em um arquivo e apresente na tela somente as 
# linhas que contenham mais do que 20 bytes.
# No final de cada linha exibir entre parenteses o tamanho da linha
# Exibida,
