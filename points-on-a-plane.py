# This is the Python Essentials 2 LAB 3.4.1.14 Points on a plane

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        # This constructor obviously creates  __x and __y properties
        # The only feature is the privateness of these proprties
        self.__x = x
        self.__y = y

    def getx(self):
        # Simply returns value of __x
        return self.__x

    def gety(self):
        # Simply returns value of __y
        return self.__y

    def distance_from_xy(self, x, y):
        # Uses math.hypot() to calculate distance to the point specified as two coords 
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        # Uses self.distance_from_xy()
        # to calculate distance to the point given as another Point class
        return self.distance_from_xy(point.getx(), point.gety())



if __name__ == "__main__":
    # This code implements some test cases
    # Expected output:
    # 1.4142135623730951
    # 1.4142135623730951

    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(2, 0))

