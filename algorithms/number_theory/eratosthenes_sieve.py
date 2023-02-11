"""Module with the implementation of eratosthenes sieve algorithm."""


from typing import List


class EratosthenesSieve:
    """Class implementation of the eratosthenes sieve algorithm."""

    def __init__(self, n: int):
        self._n = n
        self._primes = [True for _ in range(self._n + 1)]

    def eratosthenes_sieve(self) -> List[bool]:
        """
        Eratosthenes sieve algorithm.

        Returns
        -------
        primes : List[bool]
            Boolean array such that prime[i] = True if and only if i is prime.
        """
        self._primes[0] = self._primes[1] = False

        for i in range(2, self._n + 1):
            if self._primes[i]:
                for j in range(i + i, self._n + 1, i):
                    self._primes[j] = False

        return self._primes

    def accum_primes(self) -> List[int]:
        """
        Applies acumulative sum according to the primes array.

        Returns
        -------
        dp : List[int]
            Acumulative sum according to the primes array.
        """
        dp = [0 for _ in range(self._n + 1)]
        for i in range(1, self._n + 1):
            dp[i] = dp[i - 1]
            if self._primes[i]:
                dp[i] += 1
        return dp

    def get_count(self, dp: List[int], left: int, right: int) -> int:
        """
        Returns the count of prime numbers in the interval [left, right].

        Parameters
        ----------
        dp : List[int]
            Acumulative sum according to the primes array.
        left : int
            Lower limit of range.
        right : int
            Upper limit of range.

        Returns
        -------
        count_primes : int
            Count of prime numbers in the interval [left, right].
        """
        count_primes = 0

        if left == 0:
            count_primes = dp[right]
        else:
            count_primes = dp[right] - dp[left - 1]

        return count_primes
