def increasing_array(vetor):
    temp = 0

    for i in range(1, len(vetor)):
        if vetor[i] < vetor[i - 1]:
            temp += vetor[i - 1] - vetor[i]
            vetor[i] = vetor[i - 1]

    return temp


if __name__ == '__main__':
    n = int(input().strip())
    vetor = list(map(int, input().strip().split()))
    print(increasing_array(vetor))
