def type_check(param):
    if isinstance(param, int):
        return "intです"
    elif isinstance(param, float):
        return "floatです"


def another_convert_type(param):
    if '.' in param:
        param = float(param)
    else:
        param = int(param)
    return param


def convert_type(param):
    try:
        param = int(param)
    except ValueError:
        param = float(param)

    return param


def main():
    a = 1
    b = 1.5
    print(type_check(a))
    print(type_check(b))

    a, b = input().split()

    a = another_convert_type(a)
    try:
        b = convert_type(b)
    except ValueError:
        print("えらー")
        return

    print(a)
    print(b)


if __name__ == '__main__':
    main()
