"""Module to test the eratosthenes sieve implementations."""

from unittest import TestCase

from algorithms.number_theory.eratosthenes_sieve import EratosthenesSieve


class TestEratosthenesSieve(TestCase):
    """Class to test the eratosthenes sieve implementation."""

    def setUp(self):
        self.prime_finder = EratosthenesSieve(1000000)

    def test_primality_check(self):
        """Check eratosthenes sieve algorithm."""
        self.assertEqual(self.prime_finder.is_prime(1), False)
        self.assertEqual(self.prime_finder.is_prime(101), True)
        self.assertEqual(self.prime_finder.is_prime(307), True)
        self.assertEqual(self.prime_finder.is_prime(863), True)
        self.assertEqual(self.prime_finder.is_prime(7735), False)
        self.assertEqual(self.prime_finder.is_prime(88643), True)
        self.assertEqual(self.prime_finder.is_prime(92567), True)
        self.assertEqual(self.prime_finder.is_prime(99991), True)
        self.assertEqual(self.prime_finder.is_prime(99999), False)

    def test_get_primes_count(self):
        """Check the count of prime numbers in an interval."""
        self.assertEqual(self.prime_finder.get_primes_count(1, 100), 25)
        self.assertEqual(self.prime_finder.get_primes_count(1, 1000), 168)
        self.assertEqual(self.prime_finder.get_primes_count(100, 10000), 1204)
        self.assertEqual(self.prime_finder.get_primes_count(1024, 1024), 0)
        self.assertEqual(self.prime_finder.get_primes_count(1, 1000000), 78498)
        self.assertEqual(self.prime_finder.get_primes_count(345, 874), 82)
        self.assertEqual(self.prime_finder.get_primes_count(101, 101), 1)
        self.assertEqual(self.prime_finder.get_primes_count(3762, 96108), 8737)
