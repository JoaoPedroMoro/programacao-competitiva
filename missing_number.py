def missing_number(n, numbers):
    soma_n = n * (n+1) // 2
    soma_numbers = sum(numbers)
    falta = soma_n - soma_numbers
    return falta


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(missing_number(n, numbers))
