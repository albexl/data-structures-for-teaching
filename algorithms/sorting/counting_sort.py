"""Module with the implementation of the CountingSort algorithm."""


from typing import Dict, List

from .sort import Sort


class CountingSort(Sort):
    """Class that represents a CountingSort implementation."""

    def _sort(self, items: List[Dict]) -> List[Dict]:
        max_key = max(items, key=lambda x: x["key"])["key"]
        count = [0] * (max_key + 1)
        sorted_items: List[Dict] = [{}] * len(items)

        for item in items:
            count[item["key"]] += 1

        for i in range(1, max_key + 1):
            count[i] += count[i - 1]

        for item in reversed(items):
            count[item["key"]] -= 1
            sorted_items[count[item["key"]]] = item

        return sorted_items
