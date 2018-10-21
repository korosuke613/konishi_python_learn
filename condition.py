def judge_plus_minus():
    integer = 10  # int
    boolean = True  # bool(True, False)
    a = int(input("a: "))
    b = int(input("b: "))

    if a > b:
        print("a > b")
    elif a == b:
        print("a = b")
    else:
        print("b > a")


if __name__ == '__main__':
    judge_plus_minus()
