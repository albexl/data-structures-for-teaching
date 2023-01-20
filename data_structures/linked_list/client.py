"""Client code for LinkedList implementation."""

from implementation import LinkedList

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