

class StringAlgorithm:
    '''
    Base class for string algorithms.
    '''

    def __init__(self, text: str, pattern: str) -> None:
        '''
        Class constructor.

        Parameters
        ----------
        text : str
            String on which the search is performed.
        pattern : str
            Pattern to search in the text.
        '''
        self.text = text
        self.pattern = pattern

    def find_occurrences(self) -> list:
        '''
        Find the occurrences of the pattern with respect to 
        the text. Assumes indexing at 1.

        Return
        ------
            List with ocurrences.
        '''
        pass
