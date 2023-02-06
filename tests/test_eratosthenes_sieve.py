"""Module to test the eratosthenes sieve implementations."""

from unittest import TestCase

from algorithms.number_theory.eratosthenes_sieve import EratosthenesSieve


class TestEratosthenesSieve(TestCase):
    """Class to test the eratosthenes sieve implementation."""

    def setUp(self):
        self.n = 1000000
        self.eratosthenes_sieve = EratosthenesSieve(self.n)
        self.no_cousins = self.eratosthenes_sieve.eratosthenes_sieve()

    def test_eratosthenes_sieve(self):
        """Check eratosthenes sieve algorithm."""
        self.assertEqual(self.no_cousins[1], True)
        self.assertEqual(self.no_cousins[101], False)
        self.assertEqual(self.no_cousins[307], False)
        self.assertEqual(self.no_cousins[863], False)
        self.assertEqual(self.no_cousins[7735], True)
        self.assertEqual(self.no_cousins[88643], False)
        self.assertEqual(self.no_cousins[92567], False)
        self.assertEqual(self.no_cousins[99991], False)
        self.assertEqual(self.no_cousins[99999], True)

    def test_get_count_cousins(self):
        """Check the count of prime numbers in an interval."""
        self.assertEqual(self.eratosthenes_sieve.get_count_cousins(1, 100), 25)
        self.assertEqual(self.eratosthenes_sieve.get_count_cousins(1, 1000), 168)
        self.assertEqual(self.eratosthenes_sieve.get_count_cousins(100, 10000), 1204)
        self.assertEqual(self.eratosthenes_sieve.get_count_cousins(1024, 1024), 0)
        self.assertEqual(self.eratosthenes_sieve.get_count_cousins(1, 1000000), 78498)
        self.assertEqual(self.eratosthenes_sieve.get_count_cousins(345, 874), 82)
        self.assertEqual(self.eratosthenes_sieve.get_count_cousins(101, 101), 1)
        self.assertEqual(self.eratosthenes_sieve.get_count_cousins(3762, 96108), 8737)
