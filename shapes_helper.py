import math

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        area = self.length * self.length
        return area

    def peri(self):
        p = self.length * 4
        return p

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        return area

    def peri(self):
        p = (self.length * 2) + (self.breadth * 2)
        return p

class Triangle:
    def __init__(self, base, height, a, b):
        self.base = base
        self.height = height
        self.a = a
        self.b = b

    def area(self):
        area = 0.5 * self.base * self.height
        return area

    def peri(self):
        p = self.a + self.b + self.base
        return p

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius ** 2
        return area

    def peri(self):
        p = 2 * 3.14 * self.radius
        return p


def shapePrint(shape):

    if shape == "Square":

        print("********")
        print("*      *")
        print("*      *")
        print("********")

    elif shape == "Rectangle":

        print("********")
        print("*      *")
        print("********")

    elif shape == "Triangle":

        print("    *    ")
        print("   * *   ")
        print("  *   *  ")
        print(" *     * ")
        print("* * * * *")

    else:
        print("   **    ")
        print(" *    *  ")
        print("*      * ")
        print(" *    *  ")
        print("   **    ")