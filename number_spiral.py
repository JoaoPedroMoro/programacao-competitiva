def numer_spiral(y, x):
    # Verificando se a linha y é maior que a coluna x
    if y > x:
        # Calculando a área do quadrado interno que envolve a posição
        area = (y - 1) * (y - 1)
        # Verificando se a linha y é ímpar ou par
        if y % 2 != 0:
            # Se for ímpar, somamos x à área
            soma = x
        else:
            # Se for par, somamos 2*y - x
            soma = 2 * y - x
        # Retornandoo número final somando a área com o valor que foi calculado
        return area + soma
    else:  # Se a coluna x for maior ou igual à linha y
        # Calculando a área do quadrado interno, mas agora com x
        area = (x - 1) * (x - 1)
        # Verificando se a coluna x é par ou ímpar
        if x % 2 == 0:
            # Para coluna par, soma y à área
            soma = y
        else:
            # Para coluna ímpar, usa a fórmula 2*x - y
            soma = 2 * x - y
        # Retornando o resultado final com a soma
        return area + soma


if __name__ == '__main__':
    t = int(input())  # Número de casos de teste
    resultados = []
    for _ in range(t):
        y, x = map(int, input().split())  # Lê a linha e a coluna para cada teste
        resultados.append(numer_spiral(y, x))  # Adiciona o resultado da função à lista

    print("\n".join(map(str, resultados)))
