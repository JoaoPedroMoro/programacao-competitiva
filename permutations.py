def permutations(n):
    if n == 2 or n == 3:
        print("NO SOLUTION")
    else:
        permutacao = []
        for i in range(2, n + 1, 2):
            permutacao.append(i)
        for i in range(1, n + 1, 2):
            permutacao.append(i)

        print(" ".join(map(str, permutacao)))


if __name__ == '__main__':
    n = int(input().strip())
    permutations(n)
