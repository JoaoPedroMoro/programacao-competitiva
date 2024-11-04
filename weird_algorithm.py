def weird_algorithm(n):
    if n == 1 or n == 1000000:
        return [int(n)]
    flag = True
    values = [int(n)]
    while flag:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int((n * 3) + 1)
        values.append(n)
        if n == 1:
            flag = False
    return values


if __name__ == '__main__':
    n = int(input())
    output = weird_algorithm(n)
    print(" ".join(map(str, output)))
