class EratosthenesSieve:
    """Class implementation of the Eratosthenes sieve algorithm."""

    def __init__(self, n: int):
        self._n = n
        self._primes = [True] * (self._n + 1)
        self._compute_primes()
        self._accumulate_primes()

    def _compute_primes(self):
        """Eratosthenes sieve algorithm."""
        self._primes[0] = self._primes[1] = False
        for i in range(2, self._n + 1):
            if self._primes[i]:
                for j in range(i * i, self._n + 1, i):
                    self._primes[j] = False

    def _accumulate_primes(self):
        """Applies cumulative sum to the primes array."""
        self.cum_sum = [0] * (self._n + 1)
        for i in range(1, self._n + 1):
            self.cum_sum[i] = self.cum_sum[i - 1] + int(self._primes[i])

    def get_primes_count(self, left: int, right: int) -> int:
        """Returns the count of prime numbers in the interval [left, right].

        Args:
            left (int): Lower limit of the range.
            right (int): Upper limit of the range.

        Returns:
            int: Count of prime numbers in the interval [left, right].
        """
        if left < 0 or right < 0 or left > right:
            raise ValueError("Invalid range")

        return self.cum_sum[right] - (self.cum_sum[left - 1] if left > 0 else 0)

    def is_prime(self, number: int) -> bool:
        """Checks if the param `number` is a prime number.

        Args:
            number (int): The integer number to check for primality.

        Returns:
            bool: True if `number` is prime. False otherwise.
        """
        return self.get_primes_count(number, number) == 1
