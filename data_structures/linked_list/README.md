# Linked List

_Linked Lists_ are the most sought-after data structure when it comes to handling dynamic data elements. Unlike arrays, which are static in nature and operations like insertion & deletion are costly. To counter that problem Linked List comes into picture.

A linked list is a **linear** data structure, in which the elements are not stored at _contiguous_ (adjacent) memory locations, rather they are stored randomly in the memory, connected to each other with the help of links. So in simple terms, Linked List is a collection of nodes connected to each other.

Each node consists of a data field and a pointer field (also called _link_). The data field is used to store the required data and the pointer field is used to store the address of the next node(to point to the next node).

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--hRoBhSsZ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/sbzf3hz07azamnxapyp1.png " width=250 height=200 >

Each node is stored randomly in the memory. Lets see how nodes are stored in memory-

![how_nodes_are_stored_in_memory](https://2.bp.blogspot.com/-Q7DbZCYQwbo/UvkTWyBt9rI/AAAAAAAAAHY/AOK6bYcYnw4/s1600/22.JPG)

The head of our linked list stores the address 1005, which acts as an entry point to our linked list. The data 1005 contains is 'I' and the link field of that node stores the address 1007. Now go to the address 1007. The data 1007 contains is 'N' and the link field of that node stores address 1009. Repeat this process until NULL or 0 (or -1) is encountered. You will see that the characters when read in this sequence forms the word "**INDIA**".

### Head and Tail of Linked List

The first node of a linked list is called the Head, and it acts as an entry point to the linked list. On the other hand, the last node is called the Tail, and it marks the end of a linked list by pointing to a NULL value. A tail pointer is a must if we want to insert the node at the end of the list in constant time ( _i.e._ **O(1)** ). Linked lists are not indexable so for inserting any node we need to traverse the whole list to get the location to insert the node.

### There are 3 types of Linked List -

1. **Singly Linked List** - Singly linked list is a type of linked list in which a node contains a pointer to the next node in the sequence. Therefore, in a singly linked list, a node consists of two parts - _node data_ and _pointer to the next node_ in sequence (next pointer). It can be traversed in only _one direction_.
2. **Doubly Linked List** - Doubly linked list is a type of linked list in which a node contains a pointer to the next as well as the previous node in the sequence. Therefore, in a doubly linked list, a node consists of three parts: _node data_, _pointer to the next node_ in sequence (next pointer) , _pointer to the previous node_ (previous pointer). It can be traversed in _both directions_.
3. **Circular Linked List** - All nodes are connected to form a circle. In a circular linked list, the _first node and the last node are connected_ to each other which forms a circle. There is no **NULL** at the end. Both Singly and Doubly linked list can be made into circular linked list.

<img src="https://devopedia.org/images/article/409/6269.1647166159.png">

## Time Complexity for Basic Operations

- For _searching_ and accessing any element the time complexity is **O(N)** as you have to traverse the list to access the elements.

- For _insertion_ in the linked list, the time complexity is **O(1)** if done on the head, **O(N)** if done at any other location, as we need to reach that location by traversing the linked list. If you're using tail pointer, then inserting at the end will have the time complexity **O(1)**.

- For _deletion_, the time complexity is **O(1)**, if done on the head, **O(N)**, if done at any other location, as we need to reach that location by traversing the linked list. If you're using tail pointer, then deleting at the end will have the time complexity **O(1)**.

  |        | Best Case | Average Case | Worst Case |
  | ------ | --------- | ------------ | ---------- |
  | Search | O(1)      | O(N)         | O(N)       |
  | Insert | O(1)      | O(N)         | O(N)       |
  | Delete | O(1)      | O(N)         | O(N)       |

Also the _space complexity_ for all the basic operations mentioned above is **O(1)** as no extra space is required for any operation.

## Advantages of Linked Lists

- **Insertion and deletion** - Insertion and deletion in linked lists are very _efficient_. Insertion and deletion of a node in a linked list remain efficient as the nodes are stored in random locations, and we only need to update the next pointer of a constant number of nodes. Linked list can be expanded in constant time.
- **Dynamic in nature** - Linked lists are dynamic in nature, and their size can be adjusted according to our requirements.
- **Memory efficient** - Overall Memory consumption of a linked list is efficient as its size can grow or shrink dynamically according to our requirements. Since the memory is dynamically allocated to the Linked List, we can remove the memory that is not in use, and no memory is wasted.

## Disadvantages of Linked List

- **Memory usage** - A node in a linked list occupies more memory than an element in an array as each node occupies at least two kinds of variables.
- **Accessing a node** - If you want to access a node in a linked list, you have to traverse starting from the head. We cannot access any random nodes directly except for the head itself. Random access is not possible due to dynamic memory allocation.
- **Complex implementation** - Linked lists can be more complex to implement than other data structures, such as arrays or stacks. They require knowledge of dynamic memory allocation and pointer manipulation, which can be difficult for novice programmers.

## Why use Linked List over Array

<img src="https://miro.medium.com/v2/resize:fit:3454/1*G43FVT5xJ1n1QDKVNZUxXQ.jpeg"  width="900" height="500">

- Till now, we were using array data structure to organize the group of elements that are to be stored individually in the memory. However, Array has several advantages and disadvantages which must be known in order to decide the data structure which will be used throughout the program.
- Array contains following limitations:
  1. The _size of array_ must be known in advance before using it in the program.
  2. _Increasing size of the array_ is a time taking process. It is almost impossible to expand the size of the array at run time.
  3. All the elements in the array need to be _contiguously stored in the memory_. Inserting or deleting any element in the array needs shifting of all its predecessors.
- Linked list is the data structure which can overcome all the limitations of an array. Using linked list is useful because -
  1. _It allocates the memory dynamically_. All the nodes of linked list are non-contiguously stored in the memory and linked together with the help of pointers.
  2. _Sizing is no longer a problem_ since we do not need to define its size at the time of declaration. List grows as per the program's demand and limited to the available memory space.
  3. _Inserting or deleting_ an element is efficient as we only need to update the next pointer of our node.

##### At last a simple question:

What is the smallest linked list possible? and don't cop out by saying it's _NULL_ :unamused:
That's right, a single node. _A node that is both head and tail of the linked list!_ Remember what head and tail means. If the linked list contains only one element then the first (head) and last (tail) element is the same.
