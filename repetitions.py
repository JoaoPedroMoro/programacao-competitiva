def repetitions(sequencia_dna):
    maxima = 1
    atual = 1

    for i in range(1, len(sequencia_dna)):
        if sequencia_dna[i] == sequencia_dna[i - 1]:
            atual += 1
        else:
            maxima = max(maxima, atual)
            atual = 1

    maxima = max(maxima, atual)

    return maxima


if __name__ == '__main__':
    sequencia_dna = input().strip()
    print(repetitions(sequencia_dna))
