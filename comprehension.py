def even_zero2n(n):
    l = []
    for i in range(n+1):
        if i % 2 == 0:
            l.append(i)
    return l


def even_zero2n_another(n):
    l = [i for i in range(n + 1) if i % 2 == 0]
    return l


def main():
    print(even_zero2n_another(4))
    print(even_zero2n_another(80))


if __name__ == '__main__':
    main()
