import math


class Fraction:
    def __init__(self, num: int, den: int):
        if den == 0:
            raise ValueError("Denominator cannot be zero")

        self.num = int(num)
        self.den = int(den)

        self.__reduce()

    def __reduce(self):
        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g

    def __add__(self, other):
        n = self.num * other.den + other.num * self.den
        d = self.den * other.den
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.num * other.den - other.num * self.den
        d = self.den * other.den
        return Fraction(n, d)

    def __mul__(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Fraction(n, d)

    def __truediv__(self, other):
        if other.num == 0:
            raise ZeroDivisionError
        n = self.num * other.den
        d = self.den * other.num
        return Fraction(n, d)

    def __str__(self):
        return f"{self.num}/{self.den}"
