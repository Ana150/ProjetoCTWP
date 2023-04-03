# Ana Cristina Araújo - RM 99816
'''
Reajuste
SM 1302
• até dois salários-mínimos, terá o reajuste de 6,45%.
• cinco salários-mínimos, terá o reajuste de 4,55% .
• mais de cinco salários-mínimos, o reajuste será de 2,89%.

Bonus*
1000 Reais
Para quem não teve faltas

Requisitos:
• Se for digitado um salário negativo, exibir a mensagem: “ERRO! Digite um salário positivo!” e o programa deve terminar.
• Caso seja digitado um número negativo na quantidade de faltas, considerar que não tem filhos e prosseguir com os cálculos e exibições.
'''
sal = float(input("Salario: "))

if sal < 0:
    print ("ERRO! Digite um salário positivo!")
else:
    qtd_faltas = int(input("Faltas: "))
    sal_min = 1302

    # Verifiquei e calculei o reajuste
    if sal <= sal_min * 2:
        reajuste = sal * 0.0645
    elif sal <= sal_min * 5:
        reajuste = sal * 0.0455
    else:
        reajuste = sal * 0.0289

    sal_reajustado = sal + reajuste

    # Verificar se ganhou bonus
    bonus = 0
    if qtd_faltas <= 0:
        bonus = 1000

    print(f"""
    Salário..............: R$ {sal:9.2f}
    Salário reajustado...: R$ {sal_reajustado:9.2f}
    Bônus................: R$ {bonus:9.2f}
    """)