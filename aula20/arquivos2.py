"""
Fazer um programa que leia linhas e grave em um arquivo. Posteriormente exiba somente as
linhas que contenham mais do que 20 caracteres, no final desta linha, exiba a quantidade de
caracteres.

arquivoexercicio.txt
-------------------------------
No momento estamos corrigindo o exercicios.
Segunda-feira.
Bom dia.
Em breve faremos o checkpoint
-------------------------------

executando o programa:

-------------------------------
No momento estamos corrigindo o exercicios. (99)
Em breve faremos o checkpoint (99)
-------------------------------
"""
# Gravação das linhas no arquivo
import os

# ---------------- SUBALGORITMOS


def grava_arquivo(a) -> None:
    while True:
        linha = input("Digite uma linha ou . para finalizar...")
        if linha != '.':
            a.write(linha + "\n")
        else:
            break


def exibe_linhas(a):
    # Lendo o arquivo
    a.seek(0)  # posiciona o cursor no início do arquivo
    linhas_arquivo = a.readlines()

    for i in range(len(linhas_arquivo)):  # Conta quantos elementos há na lista
        # Conta quantos elementos há na posição atual da lista
        linhas_arquivo[i] = linhas_arquivo[i].replace("\n", "")
        if len(linhas_arquivo[i]) > 20:
            print(f"{linhas_arquivo[i]} - {len(linhas_arquivo[i])}")


# ---------------- PRINCIPAL
# Abertura do arquivo em modo escrita e leitura
arq = open("arq1.txt", "w+", encoding="utf-8")


grava_arquivo(arq)
exibe_linhas(arq)

arq.close()
