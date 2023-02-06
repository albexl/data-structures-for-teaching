"""Module with the implementation of eratosthenes sieve."""


from typing import List


class EratosthenesSieve:
    """Class implementation of the eratosthenes sieve algorithm."""

    def __init__(self, n: int):
        self._n = n
        self._no_cousins = [False for _ in range(self._n + 1)]

    def eratosthenes_sieve(self) -> List[bool]:
        """
        Eratosthenes sieve algorithm.
        """
        self._no_cousins[0] = self._no_cousins[1] = True

        for i in range(2, self._n + 1):
            if not self._no_cousins[i]:
                for j in range(i, self._n + 1):
                    if i * j >= self._n + 1:
                        break
                    self._no_cousins[i * j] = True

        return self._no_cousins

    def _accum_cousins(self) -> List[int]:
        """
        Applies acumulative sum according to the no_cousins array.
        """
        dp = [0 for _ in range(self._n + 1)]
        for i in range(1, self._n + 1):
            dp[i] = dp[i - 1]
            if not self._no_cousins[i]:
                dp[i] += 1
        return dp

    def get_count_cousins(self, left: int, right: int) -> int:
        """
        Returns the count of prime numbers in the interval [left, right].

        Parameters
        ----------
        left : int
            Lower limit of range.
        right : int
            Upper limit of range.
        """
        count_cousins = 0
        dp = self._accum_cousins()

        if left == 0:
            count_cousins = dp[right]
        else:
            count_cousins = dp[right] - dp[left - 1]

        return count_cousins
