from condition import judge_plus_minus


def sub():
    # 0 1 2
    for i in range(3):
        print(i)
        judge_plus_minus()

    while True:
        judge_plus_minus()


def main():
    is_correct = False
    while not is_correct:
        answer = input("パンはパンでも食べられないパンはなんだ?")
        if answer == "フライパン":
            is_correct = True
    
    while True:
        answer = input("パンはパンでも食べられないパンはなんだ?")
        if answer == "フライパン":
            break


if __name__ == '__main__':
    main()
