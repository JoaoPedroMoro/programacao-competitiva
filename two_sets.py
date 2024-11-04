def two_sets(n):
    soma_total = n * (n + 1) // 2
    if soma_total % 2 == 1:
        return "NO"

    metade_soma = soma_total // 2
    conjunto1 = []
    conjunto2 = []

    while n > 0:
        if metade_soma >= n:
            conjunto1.append(n)
            metade_soma -= n
        else:
            conjunto2.append(n)
        n -= 1

    resultado = ["YES"]
    resultado.append(str(len(conjunto1)))
    resultado.append(" ".join(map(str, conjunto1)))
    resultado.append(str(len(conjunto2)))
    resultado.append(" ".join(map(str, conjunto2)))
    return "\n".join(resultado)


if __name__ == "__main__":
    n = int(input().strip())
    print(two_sets(n))
