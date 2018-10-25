
def count_achievement(achievement, score_name):
    count = 0
    for subject in achievement.values():
        if score_name == subject:
            count += 1
    return count


def main():
    hirakoba_achievement = {
        "応用数学": "可",
        "ソフトハウス工学": "秀",
        "英語Tb2(7)": "不可",
        "key": "value"
    }
    print(count_achievement(hirakoba_achievement, "秀"))


if __name__ == '__main__':
    main()
