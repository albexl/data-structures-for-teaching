'''
    Module with the implementation of the Knuth-Morris-Pratt (KMP) 
    string algorithm.
'''
from .base_string import StringAlgorithm


class KMP(StringAlgorithm):
    '''
    Class implementation of the Knuth-Morris-Pratt (KMP) 
    string algorithm.
    '''

    def __init__(self, text: str, pattern: str) -> None:
        super().__init__(text=text, pattern=pattern)
        self._text = '$' + text
        self._pattern = '$' + pattern
        self._pi = [0 for _ in range(len(self.pattern)+1)]

        self._prefix_function()

    def _prefix_function(self) -> None:

        k = 0

        for i in range(2, len(self._pattern)):
            while (k > 0) and (self._pattern[k+1] != self._pattern[i]):
                k = self._pi[k]

            if self._pattern[k+1] == self._pattern[i]:
                k += 1

            self._pi[i] = k

    def find_occurrences(self) -> list:

        occurrences, k = [], 0

        for i in range(1, len(self._text)):
            while (k > 0) and (self._text[i] != self._pattern[k+1]):
                k = self._pi[k]

            if self._text[i] == self._pattern[k+1]:
                k += 1

            if k == (len(self._pattern)-1):
                occurrences.append(i - len(self._pattern) + 2)
                k = self._pi[k]

        return occurrences
