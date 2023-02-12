"""Module to test the eratosthenes sieve implementations."""

from unittest import TestCase

from algorithms.number_theory.eratosthenes_sieve import EratosthenesSieve


class TestEratosthenesSieve(TestCase):
    """Class to test the eratosthenes sieve implementation."""

    def setUp(self):
        self.n = 1000000
        self.eratosthenes_sieve = EratosthenesSieve(self.n)
        self.primes = self.eratosthenes_sieve.eratosthenes_sieve()

    def test_eratosthenes_sieve(self):
        """Check eratosthenes sieve algorithm."""
        self.assertEqual(self.primes[1], False)
        self.assertEqual(self.primes[101], True)
        self.assertEqual(self.primes[307], True)
        self.assertEqual(self.primes[863], True)
        self.assertEqual(self.primes[7735], False)
        self.assertEqual(self.primes[88643], True)
        self.assertEqual(self.primes[92567], True)
        self.assertEqual(self.primes[99991], True)
        self.assertEqual(self.primes[99999], False)

    def test_get_count_cousins(self):
        """Check the count of prime numbers in an interval."""
        dp = self.eratosthenes_sieve.accum_primes()
        self.assertEqual(self.eratosthenes_sieve.get_count(dp, 1, 100), 25)
        self.assertEqual(self.eratosthenes_sieve.get_count(dp, 1, 1000), 168)
        self.assertEqual(self.eratosthenes_sieve.get_count(dp, 100, 10000), 1204)
        self.assertEqual(self.eratosthenes_sieve.get_count(dp, 1024, 1024), 0)
        self.assertEqual(self.eratosthenes_sieve.get_count(dp, 1, 1000000), 78498)
        self.assertEqual(self.eratosthenes_sieve.get_count(dp, 345, 874), 82)
        self.assertEqual(self.eratosthenes_sieve.get_count(dp, 101, 101), 1)
        self.assertEqual(self.eratosthenes_sieve.get_count(dp, 3762, 96108), 8737)
