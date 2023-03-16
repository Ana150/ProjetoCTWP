'''#IMPOSTO DE RENDA
salario = float(input("Insira o salário: "))

if (salario > 0) and (salario <= 1903.98):
    aliquota = salario * 0.07
    deduzir = aliquota - 0

elif salario <= 2826.65:
    aliquota = salario * 0.09
    deduzir = aliquota - 142.80

elif salario <= float(3751.05):
    aliquota = salario * 0.15
    deduzir = aliquota - 354.80

elif salario < float(4664.68):
    aliquota = salario * 0.22
    deduzir = aliquota - 636.13

else:
    aliquota = salario * 0.27
    deduzir = aliquota - 869.36

novoSalario = salario + deduzir
print(f"""
Salário....................: R$ {salario:8.2f}
Aliquota...................: R$ {aliquota:8.2f}
IR.........................: R$ {deduzir:8.2f}
Novo salário...............: R$ {novoSalario:8.2f}""")

#IMPOSTO DE RENDA + INSS
salario = float(input("Insira o salário: "))

if (salario > 0) and (salario <= 1903.98):
    aliquota = salario * 0.7
    deduzir = aliquota - 0

elif salario <= 2826.65:
    aliquota = salario * 0.12
    deduzir = aliquota - 142.80

elif salario <= float(3751.05):
    aliquota = salario * 0.15
    deduzir = aliquota - 354.80

elif salario < float(4664.68):
    aliquota = salario * 0.22
    deduzir = aliquota - 636.13

else:
    aliquota = salario * 0.27
    deduzir = aliquota - 869.36


#INSS
if (salario > 0) and (salario <= 1302):
    inss = salario * 0.07

elif (salario > 1302) and (salario <= 2571.29):
    inss = salario * 0.09

elif (salario > float(2571.29)) and (salario <= float(3856.94)):
    inss = salario * 0.12

elif (salario > float(2571.29)) and (salario < float(7507.49)):
    inss = salario * 0.14

else:
    inss = 1051.05

resultado = salario - (deduzir + inss)

print(f"""
Salário....................: R$ {salario:8.2f}
IR.........................: R$ {deduzir:8.2f}
INSS.......................: R$ {inss:8.2f}
Novo salário...............: R$ {resultado:8.2f}""")
'''
#INSS CARTA

quantEmpregos = input("Você possuí dois empregos?: ")

salario = float(input("Insira o salário: "))
if quantEmpregos == "s" or quantEmpregos == "sim":
    salario = float(input("Insira o salário do segundo emprego: "))

possuiCarta = float(input("Possuí carta (s/n): "))


