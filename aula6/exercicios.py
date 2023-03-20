n1 = float(input("Digite a nota 1: "))
if n1 >= 0 and n1 <= 10:
    n2 = float(input("Digite a nota 2: "))
    if n2 >0 and n2<10:
        media = (n1 + n2) / 2
        if media >= 6:
            print(f"APROVADO -> Média {int(media)}")
        elif media >4 and media <= 5.9:
            exame = float(input("Digite a nota do exame: "))
            if exame >= 0 and exame <= 10:
                mediaEx = (media + exame) / 2
                if mediaEx >=6:
                    print(f"APROVADO -> Nota pré exame: {media} | Nota pós exame: {mediaEx}")
                else:
                    print(f"REPROVADO -> Nota pré exame: {media} | Nota pós exame: {mediaEx}")
        else:
            print(f"REPROVADO -> Média {int(media)}")
    else:
        print(f"{int(n2)} é uma nota inválida. Tente novamente!")
else:
    print(f"{int(n1)} é uma nota inválida. Tente novamente!")

