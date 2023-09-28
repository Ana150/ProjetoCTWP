"""
open()      ===> função que abre arquivos
write()     ===> método que grava uma linha no arquivo
read()      ===> método que carrega o arquivo inteiro
readline()  ===> método que carrega uma linha do arquivo
readlines() ===> método que transforma as linhas do arquivo em uma lista.
seek()      ===> posiciona o cursor em algum ponto do arquivo
close()     ===> fecha o arquivo
writelines()===> Este método grava varias linhas ao mesmo tempo
flush()     ===> Atualiza o disco com o buffer (F5)
"""
arq = open("arq2.txt", "w+", encoding="utf-8")
arq.write("Linha 1\n")
arq.write("Linha 2\n")
arq.write("Linha 3\n")
arq.write("Linha 4\n")
arq.write("Linha 5\n")

# gravando 3 linhas de uma vez
arq.writelines(
    ("nova linha 6\n",
     "nova linha 7\n",
     "nova linha 8\n"
     )
)

# Exibindo o conteúdo do arquivo
arq.seek(0)
arq.flush()  # atualiza o disco com o buffer
print(arq.read())

arq.close()
