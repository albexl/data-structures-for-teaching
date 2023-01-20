""" 
Linked List implementation

At the core of the linked list data structure is the Node class.
"""

class Node():
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
    first._next = second

    +-----+------+    +-----+------+   +-----+------+
    |  3  |  *---+--->|  5  |  *---+-->|  7  | None +
    +-----+------+    +-----+------+   +-----+------+
    third = Node(7)
    second._next = third

    """

    def __init__(self, data) -> None:
        self._data = data
        self._next = None


class LinkedList():
    """
    Linked List implementation
    Methods implemented
    - add(item: _type_) -> None
    - insert(item: _type_, index:int) -> None
    - get(index: int) -> _type_
    - clear() -> None
    - contains(item: _type_) -> bool
    - copy_to(collection: list(), index: int) -> None
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
                cursor = cursor._next
            previous._next = node
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
 
        """
        if index <= 0:
            raise ValueError
        node = Node(item)
        cursor = self._first
        if cursor:
            current = 1
            while cursor and current != index:
                previous = cursor
                cursor = cursor._next
                current += 1
            previous._next = node
            node._next = cursor
        else:
            cursor = node
        self._count += 1
        
    def get(self, index: int):
        """
        Returns the element located at the given position
        Performance: O(n)

        Args:
            index (int): Position of the element to return

        """
        if index <= 0 or index > self._count:
            raise ValueError
        cursor = self._first
        if cursor:
            current = 1
            while cursor and index != current:
                current += 1
                cursor = cursor._next
            return cursor._data
        return None

    def clear(self) -> None:
        """
        Removes all the items from the list.
        Performance: O(1)

        """
        self._first = None
        self._count = 0

    def contains(self, item) ->bool:
        """
        Returns a bool value (True or False) that indicates whether the provided value exists within the linked list.
        Performance: O(n)

        Returns:
            bool: bool value indicating existence of a given element
        """
        cursor = self._first
        while cursor:
            if cursor._data == item:
                return True
            cursor = cursor._next
        return False

    def copy_to(self, list: list(), index: int) -> None:
        if index <= 0 and index > self._count:
            raise ValueError
        cursor = self._first
        current = 1
        while cursor:
            if current >= index:
                list.append(cursor._data)
            cursor = cursor._next
            current += 1
        
    def remove(self, index: int):
        """
        Removes and return the element located at the given position.
        Performance: O(n)

        Args:
            index (int): Position of the element to be deleted
        """
        if index <= 0 or index > self._count:
            raise ValueError
        cursor = self._first
        if cursor:
            current = 1
            while index != current:
                current += 1
                previous = cursor
                cursor = cursor._next
            previous._next = cursor._next
            self._count -= 1
        return cursor._data

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



if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add("Carlos")
    linked_list.add(4)

    print("Before insert")
    print(f'Total items: {linked_list.length()}')
    for i in range(1, linked_list.length()+1):
        print(linked_list.get(i))

    linked_list.insert(5, 2)

    print("After insert")
    print(f'Total items: {linked_list.length()}')
    for i in range(1, linked_list.length()+1):
        print(linked_list.get(i))

    aux = []
    linked_list.copy_to(aux, 2)
    print("Copy to...")
    for i in range(0, len(aux)):
        print(aux[i])
    
    print(f'Contain 2: {linked_list.contains(2)}')
    print(f'Contain 6: {linked_list.contains(6)}')
    print(f'Contain "Carlos": {linked_list.contains("Carlos")}')
    print(f'Is Empty: {linked_list.is_empty()}')

    print(f'Removing item 3: {linked_list.remove(3)}')
    
    print("After remove")
    print(f'Total items: {linked_list.length()}')
    for i in range(1, linked_list.length()+1):
        print(linked_list.get(i))

    linked_list.clear()

    print("After clear")
    print(f'Total items: {linked_list.length()}')
    for i in range(1, linked_list.length()+1):
        print(linked_list.get(i))
