# Linked List

Linked Lists are the most sought-after data structure when it comes to handling dynamic data elements. Unlike arrays, which are static in nature and operations like insertion & deletion are costly. To counter that problem Linked List comes into picture.

A linked list is a **linear** data structure, in which the elements are not stored at *contiguous* memory locations, rather they are stored randomly in the memory, connected with the help of links. So in simple terms, Linked List is a collection of nodes connected to each other. 

Each node consists of a data field and a pointer field. The data field is used to store the required data and the pointer field is used to store the address of the next node(to point to the next node).

Each node is stored randomly in the memory. Lets see how a node is stored in memory-
![how_nodes_are_stored_in_meomry](https://2.bp.blogspot.com/-Q7DbZCYQwbo/UvkTWyBt9rI/AAAAAAAAAHY/AOK6bYcYnw4/s1600/22.JPG)

The first node of a linked list is called the Head, and it acts as an entry point to the linked list. On the other hand, the last node is called the Tail, and it marks the end of a linked list by pointing to a NULL value.

#### There are 3 types of Linked List - 
![types_of_linked_list](https://devopedia.org/images/article/409/6269.1647166159.png)


## Time Complexity for Basic Operations
- For *searching* and accessing any element the time complexity is **O(N)** as you have to traverse the list to access the elements.

- For *insertion* in the linked list, the time complexity is **O(1)** if done on the head, **O(N)** if done at any other location, as we need to reach that location by traversing the linked list.

- For *deletion*, the time complexity is **O(1)**, if done on the head, **O(N)**, if done at any other location, as we need to reach that location by traversing the linked list.

|        | Best Case | Average Case | Worst Case |
|--------|-----------|--------------|------------|
| Search | O(1)      | O(N)         | O(N)       |
| Insert | O(1)      | O(N)         | O(N)       |
| Delete | O(1)      | O(N)         | O(N)       |

Also the *space complexity* for all the basic operations mentioned above is **O(1)** as no extra space is required for any operation.

## Advantages of Linked Lists
- **Insertion and deletion** - Insertion and deletion in linked lists are very *efficient*. Insertion and deletion of a node in a linked list remain efficient as the nodes are stored in random locations, and we only need to update the next pointer of a constant number of nodes. Linked list can be expanded in constant time.
- **Dynamic in nature** - Linked lists are dynamic in nature, and their size can be adjusted according to our requirements.
- **Memory efficient** - Overall Memory consumption of a linked list is efficient as its size can grow or shrink dynamically according to our requirements. Since the memory is dynamically allocated to the Linked List, we can remove the memory that is not in use, and no memory is wasted. 

## Disadvantages of Linked List
- **Memory usage** - A node in a linked list occupies more memory than an element in an array as each node occupies at least two kinds of variables.
- **Accessing a node** - If you want to access a node in a linked list, you have to traverse starting from the head. We cannot access any random nodes directly except for the head itself. Random access is not possible due to dynamic memory allocation.
- **complex implementation** - Linked lists can be more complex to implement than other data structures, such as arrays or stacks. They require knowledge of dynamic memory allocation and pointer manipulation, which can be difficult for novice programmers.

## Why use Linked List over Array
![array_VS_linkedList](https://miro.medium.com/v2/resize:fit:3454/1*G43FVT5xJ1n1QDKVNZUxXQ.jpeg)
- Till now, we were using array data structure to organize the group of elements that are to be stored individually in the memory. However, Array has several advantages and disadvantages which must be known in order to decide the data structure which will be used throughout the program.
- Array contains following limitations:
    1. The *size of array* must be known in advance before using it in the program.
    2. *Increasing size of the array* is a time taking process. It is almost impossible to expand the size of the array at run time.
    3. All the elements in the array need to be *contiguously stored in the memory*. Inserting or deleting any element in the array needs shifting of all its predecessors.
- Linked list is the data structure which can overcome all the limitations of an array. Using linked list is useful because - 
    1. *It allocates the memory dynamically*. All the nodes of linked list are non-contiguously stored in the memory and linked together with the help of pointers.
    2. *Sizing is no longer a problem* since we do not need to define its size at the time of declaration. List grows as per the program's demand and limited to the available memory space.
    3. *Inserting or deleting* an element is efficient as we only need to update the next pointer of our node.

##### At last a simple question:
What is the smallest linked list possible? and don't cop out by saying it's *NULL* :unamused:
That's right, a single node. *A node that is both head and tail of the linked list!* Remember what head and tail means. If the linked list contains only one element then the first (head) and last (tail) element is the same.