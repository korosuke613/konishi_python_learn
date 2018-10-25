import math


class Point:
    def __init__(self):
        self.x = None
        self.y = None
        self.name = None
        self.input_coordinate()

    def input_coordinate(self):
        x, y = input("座標を入力してください").split()
        self.x = float(x)
        self.y = float(y)
        self.name = input("名前を入力してください")


class PointPair:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.distance = math.sqrt((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2)


def main():
    point1 = Point()
    point2 = Point()
    point_pair = PointPair(point1, point2)
    print(point_pair.distance)


if __name__ == '__main__':
    main()
