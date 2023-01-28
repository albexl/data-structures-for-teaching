class BinarySearchBase:
    """
    Binary Search Base Class containing a general implemenation.

    Given a monotonic Boolean function `func`,
    it finds the first `x` in the range `[left, right)`
    such that `func(x) == True`

    Assumptions:
    - `func(x) == True` implies `f(y) == True` for every `y > x`.
    - `func(right) == True` always. Thus, if no `x in [left, right)` holds `f(x) == True`,
    it returns `right`

    ---

    Example usecase:
    >>> array = list(2**i for i in range(10))
    >>> search = BinarySearchBase(lambda x : array[x] > 4)
    >>> search(0, len(array))
    3
    >>> search = BinarySearchBase(lambda x : array[x] > 512)
    >>> search(0, len(array))
    10
    >>> search = BinarySearchBase(lambda x : x * x > 2)
    >>> search(left=0, right=2, stop_length=1e-6, floating_division=True)
    1.4142141342163086
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, left, right, max_iter=None, stop_length=1, floating_division=False):
        """
        Performs the search.
        """

        if self.func(left):
            return left

        while right - left > stop_length:
            if floating_division:
                mid = (left + right) / 2
            else:
                mid = (left + right) // 2
            if self.func(mid):
                right = mid
            else:
                left = mid
            if max_iter is not None:
                max_iter -= 1
                if max_iter <= 0:
                    break
        return right
