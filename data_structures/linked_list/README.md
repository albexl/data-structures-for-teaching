# Linked List

Linked Lists are the most sought-after data structure when it comes to handling dynamic data elements. Unlike arrays, which are static in nature and operations like insertion & deletion are costly. To counter that problem Linked List comes into picture.

A linked list is a **linear** data structure, in which the elements are not stored at *contiguous* memory locations, rather they are stored randomly in the memory, connected with the help of links. So in simple terms, Linked List is a collection of nodes connected to each other. 

Each node consists of a data field and a pointer field (also called *link*). The data field is used to store the required data and the pointer field is used to store the address of the next node(to point to the next node).
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--hRoBhSsZ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/sbzf3hz07azamnxapyp1.png " width=330 height=300 >


Each node is stored randomly in the memory. Lets see how a node is stored in memory-
![how_nodes_are_stored_in_meomry](https://2.bp.blogspot.com/-Q7DbZCYQwbo/UvkTWyBt9rI/AAAAAAAAAHY/AOK6bYcYnw4/s1600/22.JPG)
The head of our linked list stores the address 1005, which acts as an entry point to our linked list. The data 1005 contains is 'I' and the link field of that node stores the address 1007. Now go to the address 1007. The data 1007 contains is 'N' and the link field of that node stores address 1009. Repeat this process until NULL or 0 (or -1) is encountered.

### Head and Tail of Linked List

The first node of a linked list is called the Head, and it acts as an entry point to the linked list. On the other hand, the last node is called the Tail, and it marks the end of a linked list by pointing to a NULL value.
<img src="data:image/png;base64,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">

### There are 3 types of Linked List -
<img src="https://devopedia.org/images/article/409/6269.1647166159.png">


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
- **Complex implementation** - Linked lists can be more complex to implement than other data structures, such as arrays or stacks. They require knowledge of dynamic memory allocation and pointer manipulation, which can be difficult for novice programmers.

## Why use Linked List over Array
<img src="https://miro.medium.com/v2/resize:fit:3454/1*G43FVT5xJ1n1QDKVNZUxXQ.jpeg"  width="800" height="450">

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