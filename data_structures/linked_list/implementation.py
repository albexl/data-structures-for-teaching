"""
Linked List implementation

At the core of the linked list data structure is the Node class.
"""


from typing import List


class Node:
    """
    A node is a container that provides the ability to both store data and connect to other nodes.

    +-----+------+
    |  3  | None +
    +-----+------+
    first = Node(3)

    +-----+------+   +-----+------+
    |  3  | None +   |  5  | None +
    +-----+------+   +-----+------+
    second = Node(5)

    +-----+------+    +-----+------+
    |  3  |  *---+--->|  5  | None +
    +-----+------+    +-----+------+
    first.next = second

    +-----+------+    +-----+------+   +-----+------+
    |  3  |  *---+--->|  5  |  *---+-->|  7  | None +
    +-----+------+    +-----+------+   +-----+------+
    third = Node(7)
    second.next = third

    """

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    """
    Linked List implementation
    Methods implemented
    - add(item: _type_) -> None
    - insert(item: _type_, index:int) -> None
    - get(index: int) -> _type_
    - clear() -> None
    - contains(item: _type_) -> bool
    - copy_to(list: List, index: int) -> None
    - remove(item: _type_) -> None
    - is_empty() -> bool
    - length() -> int
    """

    def __init__(self) -> None:
        self._first = None
        self._count = 0

    def add(self, item) -> None:
        """
        Adds a new element to the end of the linked list
        Performance: O(n)

        Args:
            item (_type_): Element to be added
        """
        node = Node(item)
        cursor = self._first
        if cursor:
            while cursor:
                previous = cursor
                cursor = cursor.next
            previous.next = node
        else:
            self._first = node
        self._count += 1

    def insert(self, item, index: int) -> None:
        """
        Insert a new element in a given position
        Performance: O(n)

        Args:
            item (_type_): New element to be inserted
            index (int): Position where it will be inserted

        Raises:
            ValueError: Index out of range
        """
        if index <= 0:
            raise ValueError("Index out of range")
        node = Node(item)
        cursor = self._first
        if cursor:
            current = 1
            while cursor and current != index:
                previous = cursor
                cursor = cursor.next
                current += 1
            previous.next = node
            node.next = cursor
        else:
            cursor = node
        self._count += 1

    def get(self, index: int):
        """
        Returns the element located at the given position
        Performance: O(n)

        Args:
            index (int): Position of the element to return

        Raises:
            ValueError: Index out of range
        """
        if index <= 0 or index > self._count:
            raise ValueError("index out of range")
        cursor = self._first
        if cursor:
            current = 1
            while cursor and index != current:
                current += 1
                cursor = cursor.next
            return cursor.data
        return None

    def clear(self) -> None:
        """
        Removes all the items from the list.
        Performance: O(1)

        """
        self._first = None
        self._count = 0

    def contains(self, item) -> bool:
        """Checks whether the provided value exists within the linked list.
        Performance: O(n)

        Returns:
            bool: Bool value indicating the existence of a given element.
        """
        cursor = self._first
        while cursor:
            if cursor.data == item:
                return True
            cursor = cursor.next
        return False

    def copy_to(self, to_copy_list: List, index: int) -> None:
        """Updates the list passed as a parameter with the elements of the linked list starting at `index`.
        Performance: O(n)

        Args:
            to_copy_list (List): List to be updated
            index (int): Starting position

        Raises:
            ValueError: Index out of range
        """
        if index <= 0 or index > self._count:
            raise ValueError("Index out of range")
        cursor = self._first
        current = 1
        while cursor:
            if current >= index:
                to_copy_list.append(cursor.data)
            cursor = cursor.next
            current += 1

    def remove(self, index: int):
        """
        Removes and return the element located at the given position.
        Performance: O(n)

        Args:
            index (int): Position of the element to be deleted

        Raises:
            ValueError: Index out of range
        """
        if index <= 0 or index > self._count:
            raise ValueError("Index out of range")
        cursor = self._first
        if cursor:
            current = 1
            while index != current:
                current += 1
                previous = cursor
                cursor = cursor.next
            previous.next = cursor.next
            self._count -= 1
        return cursor.data

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        Performance: O(1)

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self._count == 0

    def length(self) -> int:
        """
        Returns the total number of elements contained in the linked list
        Performance: O(1)

        Returns:
            int: Total number of elements contained in the linked list

        """
        return self._count
