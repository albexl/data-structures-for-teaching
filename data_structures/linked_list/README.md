# Linked List

Linked Lists are the most sought-after data structure when it comes to handling dynamic data elements. Unlike arrays, which are static in nature and operations like insertion & deletion are costly. To counter that problem Linked List comes into picture.

A linked list is a **linear** data structure, in which the elements are not stored at *contiguous* memory locations, rather they are stored randomly in the memory, connected with the help of links. So in simple terms, Linked List is a collection of nodes connected to each other. 

Each node consists of a data field and a pointer field. The data field is used to store the required data and the pointer field is used to store the address of the next node(to point to the next node).

Each node is stored randomly in the memory. Lets see how a node is stored in memory-

The first node of a linked list is called the Head, and it acts as an entry point to the linked list. On the other hand, the last node is called the Tail, and it marks the end of a linked list by pointing to a NULL value.

At last a simple question:
What is the smallest linked list possible? and don't cop out by saying it's *NULL* :unamused:
That's right, a single node. *A node that is both head and tail of the linked list!* Remember what head and tail means. If the linked list contains only one element then the first(head) and last(tail) element is the same.