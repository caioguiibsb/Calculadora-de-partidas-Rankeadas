def calcular_rank(vitorias, derrotas):
    saldo = vitorias - derrotas

    niveis = [
        (10, "Ferro"),
        (20, "Bronze"),
        (50, "Prata"),
        (80, "Ouro"),
        (90, "Diamante"),
        (100, "Lendário"),
        (float('inf'), "Imortal")
    ]

    for limite, nome_nivel in niveis:
        if vitorias <= limite:
            return saldo, nome_nivel


# Programa principal
vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))

saldo, nivel = calcular_rank(vitorias, derrotas)

print(f"O Herói tem um saldo de {saldo} e está no nível de {nivel}")
