#Simple math program for calculate surface and circuit
import math

class Square:
    def surface_area(self, a):
        return a * a
    def circuit(self, a):
        return 4 * a


class Rectangle:
    def surface_area(self, a, b):
        return a * b
    def circuit(self, a, b):
        return (2*a) + (2*b)


class Triangle:
    def surface_area(self, a, h):
        return 0.5 * a * h
    def circuit(self, a, b, c):
        return a * b * c


class Circle:
    def surface_area(self, r):
        return math.pi * math.pow(r,2)
    def circuit(self, r):
        return 2 * math.pi * r


class Cone:
    pass


'''
chose = int(input('What figure you want to calculate?\n 1 - Square\n 2 - Rectangle\n'))
print(chose)
'''
