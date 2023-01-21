"""Module with the implementation of modular arithmetics."""


class Modular:
    """Class handling arithmetic operations under a given modulo."""

    def __init__(self, modulo: int) -> None:
        self.modulo = modulo

    def add(self, a: int, b: int) -> int:
        return (a + b) % self.modulo

    def sub(self, a: int, b: int) -> int:
        return (a - b + self.modulo) % self.modulo

    def mult(self, a: int, b: int) -> int:
        return a * b % self.modulo

    def pow(self, a: int, b: int) -> int:
        result = 1
        while b > 0:
            if b % 2 == 1:
                result = self.mult(result, a)
            a = self.mult(a, a)
            b = b // 2

        return result
