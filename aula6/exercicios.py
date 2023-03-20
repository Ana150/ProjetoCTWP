''' #Dadas duas notas, calcular a média das duas notas e verificar se o aluno foi aprovado (media 6)
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
media = (n1 + n2) / 2

if media > 6:
    print(f"Aprovado com media {media}")
    else:    print(f"Reprovado com media {media}")

V2.0 - Considere o enunciado da versão anterior. Contudo, consistir os dados
para que a medianáo seja calculada de forma errada.
TESTES
Nota 1: 4   Nota 2: 5       SAÍDA: Reprovado com media 4.5
Nota 1: 7   Nota 2: 15      SAÍDA: A segunda nota é inválida
Nota 1: -3                  SAÍDA: A primeira nota é inválida
'''

 n1 = float(input("Digite a nota 1: "))
 media = (n1 + n2) / 2

 if n1 >0 and n1<10:
     n2 = float(input("Digite a nota 2: "))
     if n2 >0 and n2<10:
         if media > 6:
             print(f"Aprovado com media {media}")
         else:
             print(f"Reprovado com media {media}")
 else:
     prit(f"{n1} é uma nota inválida. Tente novamente!")
 media = (n1 + n2) / 2

