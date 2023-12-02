import unittest

from algorithms.number_theory.eratosthenes_sieve import EratosthenesSieve


class EratosthenesSieveTest(unittest.TestCase):
    def test_get_primes_count(self):
        sieve = EratosthenesSieve(100)

        # Test case 1: Range with prime numbers
        self.assertEqual(sieve.get_primes_count(10, 30), 6)

        # Test case 2: Range with no prime numbers
        self.assertEqual(sieve.get_primes_count(44, 46), 0)

        # Test case 3: Range with single prime number
        self.assertEqual(sieve.get_primes_count(23, 23), 1)

        # Test case 4: Range with negative limits
        with self.assertRaises(ValueError):
            sieve.get_primes_count(-10, 20)

        # Test case 5: Range with invalid limits
        with self.assertRaises(ValueError):
            sieve.get_primes_count(50, 40)

    def test_is_prime(self):
        sieve = EratosthenesSieve(100)

        # Test case 1: Prime number
        self.assertTrue(sieve.is_prime(17))

        # Test case 2: Non-prime number
        self.assertFalse(sieve.is_prime(20))

        # Test case 3: Negative number
        self.assertFalse(sieve.is_prime(-7))

        # Test case 4: Zero
        self.assertFalse(sieve.is_prime(0))

        # Test case 5: One
        self.assertFalse(sieve.is_prime(1))
