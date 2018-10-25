# lは引数
def two_times_list(l):
    """
    リストの要素を２倍にする
    :param l: int型リスト
    :return: lの要素を2倍にしたリスト
    """

    tmp = []            # 空のリスト
    for value in l:     # lの中身が順番にvalueに入る
        value *= 2      # value = value * 2の略
        tmp.append(value)  # tmpにvalueが追加される
    # tmpは返値
    return tmp


def main():
    # 基本データ型
    integer = 10  # 整数(int)
    floating_point = 0.4  # 実数(float)
    string = "もじれつ"  # 文字列(str)

    my_list = [1, 3, 4, 6]  # リスト(list) -- mutable(変更可能)
    my_tuple = (1, 3, 4, 6)  # タプル(tuple) -- immutable(変更不可能)
    my_dictionary = {1: "いち", 3: "さん", 4: "よん", 6: "ろく"}  # 辞書(dict)

    result_list = two_times_list(my_list)
    print(result_list)

    sai_1 = 1/6
    sai_2 = 1/3
    sai_3 = 1/12
    sai_4 = 1/12
    sai_5 = 1/6
    sai_6 = 1/6

    sai = [1/6, 1/3, 1/12, 1/12, 1/6, 1/6]
    for kakuritu in sai:
        print(kakuritu)


if __name__ == '__main__':
    main()
