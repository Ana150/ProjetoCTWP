print("----------> 1° SEMESTRE <----------")
print("-----------------------------------")
print("Notas dos CheckPoints - 1° semestre")
nota1Cp = float(input("Insira a 1° nota: "))
nota2Cp = float(input("Insira a 2° nota: "))
nota3Cp = float(input("Insira a 3° nota: "))

if nota1Cp < nota2Cp and nota1Cp < nota3Cp:
    mediaCp = (nota2Cp + nota3Cp)/2

elif nota2Cp < nota1Cp and nota2Cp < nota3Cp:
    mediaCp = (nota1Cp + nota3Cp)/2

else:
    mediaCp = (nota1Cp + nota2Cp)/2

print("-----------------------------------")
print(f"A média dos CheckPoints é: {mediaCp}")
print("-----------------------------------")
print(f"Notas dos Sprints - 1° semestre")
nota1Sp = float(input("Insira a 1° nota: "))
nota2Sp = float(input("Insira a 2° nota: "))

mediaSp = (nota2Sp + nota1Sp)/2

print("-----------------------------------")
print(f"A média dos Sprints é: {mediaSp}")
print("-----------------------------------")
print(f"Nota da GlobalS - 1° semestre")
nota1Gs = float(input("Insira a nota obtida: "))

mediaSem1 = (mediaCp * 0.2) + (mediaSp * 0.2) + (nota1Gs * 0.6)

print("-----------------------------------")
print(f"MÉDIA 1° SEMESTRE: {(mediaSem1)}")
print("-----------------------------------")

print("----------> 2° SEMESTRE <----------")
print("-----------------------------------")
print("Notas dos CheckPoints - 2° semestre")
nota1Cp = float(input("Insira a 1° nota: "))
nota2Cp = float(input("Insira a 2° nota: "))
nota3Cp = float(input("Insira a 3° nota: "))

if nota1Cp < nota2Cp and nota1Cp < nota3Cp:
    mediaCp = (nota2Cp + nota3Cp) / 2

elif nota2Cp < nota1Cp and nota2Cp < nota3Cp:
    mediaCp = (nota1Cp + nota3Cp) / 2

else:
    mediaCp = (nota1Cp + nota2Cp) / 2

print("-----------------------------------")
print(f"A média dos CheckPoints é: {mediaCp}")
print("-----------------------------------")

print(f"Notas dos Sprints - 2° semestre")
nota1Sp = float(input("Insira a 1° nota: "))
nota2Sp = float(input("Insira a 2° nota: "))

mediaSp = (nota2Sp + nota1Sp) / 2

print("-----------------------------------")
print(f"A média dos Sprints é: {mediaSp}")
print("-----------------------------------")

print(f"Nota da GlobalS - 2° semestre")
nota1Gs = float(input("Insira a nota obtida: "))

mediaSem2 = (mediaCp * 0.2) + (mediaSp * 0.2) + (nota1Gs * 0.6)

print("-----------------------------------")
print(f"MÉDIA 2° SEMESTRE: {mediaSem2}")
print("-----------------------------------")

mediaAnual = (mediaSem1 * 0.4) + (mediaSem2 * 0.6)

if mediaAnual >=6:
    print(f"MÉDIA ANUAL: {mediaAnual} - ALUNO(A) APROVADO")
elif mediaAnual >=4 and mediaAnual <6:
    print(f"MÉDIA ANUAL: {mediaAnual} - ALUNO(A) DE EXAME")
    notaEx = float(input("Insira a nota do exame: "))
    mediaEx = (mediaAnual + notaEx)/2
    if mediaEx >= 6:
        print(f"MÉDIA ANUAL: {mediaEx} - ALUNO(A) APROVADO")
    else:
        print(f"MÉDIA ANUAL: {mediaEx} - ALUNO(A) REPROVADO")
else:
    print(f"MÉDIA ANUAL: {mediaAnual} - ALUNO(A) REPROVADO")