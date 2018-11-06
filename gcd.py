"""
2つの自然数aとbを入力する。ただし a ≧ b

aをbで割った余りcを計算する
cが0ならば(割り切れたら)、最大公約数はbである
cが0でなければ、bを新しいa、cを新しいbとする
1に戻る

"""


def gcd(a, b):
    while True:
        c = a % b
        if c == 0:
            return b
        a = b
        b = c


def gcd_another(a, b):
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b


def gcd_recursive(a, b):
    c = a % b
    if c == 0:
        return b

    return gcd_recursive(b, c)


def main():
    a, b = input().split()
    print(gcd_recursive(int(a), int(b)))
    return


if __name__ == '__main__':
    main()
