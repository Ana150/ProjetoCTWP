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

teto = False
inss2 = 0
qtd_empr = int(input("Quantidade de empregos: "))

if qtd_empr > 1:
    sal = float(input("Digite o seu salário: R$ "))
if sal <= 1302:
    inss = sal * 0.07
elif sal <= 2571.29:
    inss = sal * 0.09
elif sal <= 3856.94:
    inss = sal * 0.12
elif sal <= 7507.49:
    inss = sal * 0.14
else:        # paga no teto
    teto = True
    inss = 1051.05
    if teto == True:
        #nao cobrar o inss do segundo emprego
        inss2 = 0
        sal2 = float(input("Digite o seu salário 2: R$ "))    else:        # cobrar o inss do segundo emprego        sal2 = float(input("Digite o seu salário 2: R$ "))        if sal2 <= 1302:            inss2 = sal * 0.07        elif sal2 <= 2571.29:            inss2 = sal * 0.09        elif sal2 <= 3856.94:            inss2 = sal * 0.12        elif sal2 <= 7507.49:            inss2 = sal * 0.14        else:            # paga no teto            inss2 = 1051.05    # Cálculo do salário líquido    sal_liq = sal + sal2 - inss - inss2    # Exibição das informações    print(f"""            Salário..........: R$ {sal:8.2f}            Salário 2........: R$ {sal2:8.2f}            INSS.............: R$ {inss:8.2f}            INSS 2...........: R$ {inss2:8.2f}            Salário Líquido..: R$ {sal_liq:8.2f}        """)else:    sal = float(input("Digite o seu salário: R$ "))    if sal <= 1302:        inss = sal * 0.07    elif sal <= 2571.29:        inss = sal * 0.09    elif sal <= 3856.94:        inss = sal * 0.12    elif sal <= 7507.49:        inss = sal * 0.14    else:        inss = 1051.05    # Cálculo do salário líquido    sal_liq = sal - inss    # Exibição das informações    print(f"""        Salário..........: R$ {sal:8.2f}        INSS.............: R$ {inss:8.2f}        Salário Líquido..: R$ {sal_liq:8.2f}    """)