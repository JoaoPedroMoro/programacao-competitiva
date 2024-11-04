def two_knights(n):
    resultados = []
    for k in range(1, n + 1):
        total = (k * k * (k * k - 1)) // 2
        atks = 4 * (k - 1) * (k - 2) if k > 2 else 0
        nao_atks = total - atks
        resultados.append(nao_atks)
    return resultados


if __name__ == "__main__":
    n = int(input())
    resultado = two_knights(n)
    print("\n".join(map(str, resultado)))
