
def main():
    a, r, m = input("初項、公比、項数を入力してください").split()
    a = int(a)
    r = int(r)
    m = int(m)

    for n in range(1, m+1):
        result = a * r ** (n - 1)
        print(n, result)


if __name__ == '__main__':
    main()
