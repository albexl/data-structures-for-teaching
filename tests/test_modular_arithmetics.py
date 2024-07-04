"""Module to test the modular arithmetic implementations."""

from unittest import TestCase

from algorithms.number_theory.modular_arithmetics import Modular


class TestModularAdd(TestCase):
    """Class to test the 'add' method of modular arithmetic implementation."""

    def setUp(self):
        self.modular = Modular(10)

    def test_add(self):
        """Test the `add` method with various inputs."""
        test_cases = [
            (3, 4, 7),  # Simple addition
            (5, 5, 0),  # Addition resulting in modulus
            (8, 5, 3),  # Addition wrapping around modulus
            (0, 0, 0),  # Edge case: adding zeros
            (-1, 2, 1),  # Negative numbers
            (10, 10, 0),  # Inputs equal to modulus
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(self.modular.add(a, b), expected)


class TestNaive(TestCase):
    """Class to test the modular arithmetics implementation."""

    def setUp(self):
        self.modular = Modular(10)

    def test_sub(self):
        """Test the `sub` method."""
        self.assertEqual(self.modular.sub(3, 4), 9)
        self.assertEqual(self.modular.sub(5, 5), 0)
        self.assertEqual(self.modular.sub(8, 5), 3)

    def test_mult(self):
        """Test the `mult` method."""
        self.assertEqual(self.modular.mult(3, 4), 2)
        self.assertEqual(self.modular.mult(5, 5), 5)
        self.assertEqual(self.modular.mult(8, 5), 0)

    def test_pow(self):
        """Test the `pow` method."""
        self.assertEqual(self.modular.pow(3, 4), 1)
        self.assertEqual(self.modular.pow(5, 5), 5)
        self.assertEqual(self.modular.pow(8, 5), 8)
