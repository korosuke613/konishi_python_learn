def extraction_middle2last(s):
    return s[len(s)//2:]


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a[::])
    print(a[5:7:1])
    print(extraction_middle2last("abcdefghijklmn"))
    print(extraction_middle2last("abcdefghijklm"))


if __name__ == '__main__':
    main()
