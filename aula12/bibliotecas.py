#Procedimento: executa um bloco e não retona valor
def saudacao() -> None:
    print("Bom dia, turma!")

def saudacao2(nome: str) -> None:
    print(f"Bom dia, {nome}!")

def saudacao3(nome: str, hora: int) -> None:
    if hora < 12:
        print(f"Bom dia, {nome}!")
    elif hora < 18:
        print(f"Boa tarde, {nome}!")
    else:
        print(f"Boa noite, {nome}!")

#Função: executa um bloco e retorna um valor
def raizQuadrada(n: float) -> float:
    return n ** 1/2