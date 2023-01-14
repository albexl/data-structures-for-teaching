"""Module to test the Searching algorithms."""


from unittest import TestCase

from parameterized import parameterized

from algorithms.searching.search import Search
from algorithms.searching.linear_search import LinearSearch
from algorithms.searching.binary_search import BinarySearch

class TestSearch(TestCase):
    """Base class to test Searching implementations."""

    @parameterized.expand(
        [
            (
                LinearSearch,
                lambda x, y: x - y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                4,
                1
            ),
            (
                BinarySearch,
                lambda x, y: x - y,
                [1, 1, 2, 2, 3, 4, 4, 9],
                4,
                5
            ),
            (
                BinarySearch,
                lambda x, y: x - y,
                [1, 1, 2, 2, 3, 4, 4, 9],
                0,
                -1
            )
        ]
    )


    def test_searching(self, search_method: Search, comp_func, items, item_find, expected):
        """Test the Searching algorithms.

            Args:
                search_method (Search): Search method to test.
                comp_func (function): Function to compare items.
                items (list): List of items to find the items.
                item_find (int): Item to find.
                expected (int): Expected index of the item.
        """

        original_items = items.copy()
        search = search_method(comp_func, items)
        index_search = search.search(item_find)
        self.assertEqual(index_search, expected)
        self.assertEqual(original_items, items)
