def calcular_nivel(vitorias):
    if vitorias <= 10:
        return "Ferro"
    elif vitorias <= 20:
        return "Bronze"
    elif vitorias <= 50:
        return "Prata"
    elif vitorias <= 80:
        return "Ouro"
    elif vitorias <= 90:
        return "Diamante"
    elif vitorias <= 100:
        return "Lendário"
    else:
        return "Imortal"


def calcular_rankeadas(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas
    nivel = calcular_nivel(vitorias)
    return saldo_vitorias, nivel


def main():
    while True:
        try:
            vitorias = int(input("Informe o número de vitórias: "))
            derrotas = int(input("Informe o número de derrotas: "))

            if vitorias < 0 or derrotas < 0:
                print("Os valores não podem ser negativos. Tente novamente.\n")
                continue

            saldo, nivel = calcular_rankeadas(vitorias, derrotas)

            print(f"\nO Herói tem de saldo de {saldo} está no nível de {nivel}\n")

            continuar = input("Calcular novamente? (s/n): ").strip().lower()
            if continuar != "s":
                break

        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.\n")


main()