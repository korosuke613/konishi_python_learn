def main():
    print("hello")
    hirakoba_sum1()


def hirakoba_sum1():
    a = input("数字を1つ入力してください: ")  # aはstrになる
    b = input("もう一つ入力してください: ")

    total = a + b  # str + str でtotalはstrになります。"1" + "2"は"12"になります。
    print(total)

    total = int(a) + int(b)  # int + intでtotalはint
    print(total)
    total = float(a) + float(b)  # float + floatでfloat
    print(total)

    # int 整数
    seisuu = 1

    # float 実数
    syosuu = 3.00

    # str 文字列(string)
    mojiretu = 'もじ'


if __name__ == '__main__':
    main()
