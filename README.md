# Data Structures and Algorithms in Python

Implementations of some Data Structures, with different approaches and some
practical applications. Designed to be used as consulting material for those who want to learn about Data Structures and Algorithms and have a preference for the [Python](https://www.python.org/) programming language.

Here is a checklist of the Data Structures and Algorithms we have or we are planning to add. If you would like to add more to the checklist, just create a Pull Request with your additions and we will review it.

## Data Structures:

- [x] [Stack](./data_structures/stack/implementation.py): A stack is an abstract data type that serves as a collection of elements, with two main operations: Push, which adds an element to the collection, and Pop, which removes the most recently added element that was not yet removed.

- [x] [Trie](./data_structures/trie/implementation.py):
A trie is an ordered data structure, a type of search tree used to store associative data structures.

- [x] [Heap](./data_structures/heap/implementation.py):
A heap is a specialized tree-based data structure which is essentially an almost complete tree that satisfies the heap property

- [x] [Union-Find](./data_structures/union_find/implementation.py)

- [x] [Graphs](./data_structures/graphs/implementation.py):
A graph is a non-linear kind of data structure made up of nodes or vertices and edges.

- [x] [Linked List](./data_structures/linked_list/implementation.py):
A linked list consists of a data element known as a node. And each node consists of two fields: one field has data, and in the second field, the node has an address that keeps a reference to the next node.

## Algorithms:

### Sorting Algorithms:

- [x] [Bubble Sort](./algorithms/sorting/bubblesort.py):
A sorting algorithm that repeatedly steps through the input list element by element, comparing the current element with the one after it, swapping their values if needed

- [x] [Heap Sort](./algorithms/sorting/heapsort.py):
A comparison-based sorting technique based on Binary Heap data structure. Is used when the smallest (shortest) or highest (longest) value is needed instantly

- [x] [Merge Sort](./algorithms/sorting/mergesort.py):
A sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array
 
- [x] [Quick Sort](./algorithms/sorting/quicksort.py):
A divide and sort algorithm

- [x] [Insertion Sort](./algorithms/sorting/insertionsort.py):
A simple sorting algorithm that builds the final sorted array (or list) one item at a time by comparisons.

- [x] [Selection Sort](./algorithms/sorting/selectionsort.py):
An effective and efficient sort algorithm based on comparison operations.

- [ ] Radix Sort:
A non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into buckets according to their radix.
- [x] [Counting Sort](./algorithms/sorting/counting_sort.py):
A a sorting technique based on keys between a specific range

- [x] [Shell Sort](./algorithms/sorting/shell_sort.py):
A sorting algorithm that is highly efficient and is based on the insertion sort algorithm

- [x] [Bogo Sort](./algorithms/sorting/bogo_sort.py):
A sorting algorithm based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted

- [ ] Tim Sort:
A hybrid, stable sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data.

- [x] [Gnome Sort](./algorithms/sorting/gnome_sort.py)

### Search Algorithms:

- [x] [Linear Search](./algorithms/searching/linear_search.py):
A method for finding an element within a list where sequentially the code checks each element of the list until a match is found or the whole list has been searched.
- [ ] Binary Search:
A method for finding an element that finds a position of a target value within a sorted array, and compares the target element to the middle element of the array.
- [ ] Ternary Search:
A search algorithm is a technique in computer science for finding the minimum or maximum of a unimodal function

### String Algorithms

- [x] [Knuth-Morris-Pratt](./algorithms/strings/kmp.py):
An algorithm campares character by character from left to right. But whenever a mismatch occurs, it uses a preprocessed table called "Prefix Table" to skip characters comparison while matching.

- [x] [Naive](./algorithms/strings/naive.py):
An algorithm  used to find the longest palindromic substring in any given string

- [ ] Manacher
- [ ] Z-Function

### Number Theory Algorithms

- [ ] Greatest Common Divisor

- [ ] Extended Greatest Common Divisor
- [ ] Euler's Phi Function
- [x] [Eratosthenes Sieve](./algorithms/number_theory/eratosthenes_sieve.py)
- [ ] Miller-Rabin
- [x] [Modular Arithmetics](./algorithms/number_theory/modular_arithmetics.py)

### Algebra/Numerical Algorithms

- [ ] Gauss
- [ ] Simplex
- [ ] Simpson
- [ ] Fast Fourier Transform

### Graph Algorithms:

- [ ] Breadth-First Search
- [ ] Depth-First Search

## Contributing

We would love to see you contribute to this project. No matter if it is fixing a bug, adding some tests, improving documentation, or implementing new algorithms and data structures. See [CONTRIBUTING.md](./CONTRIBUTING.md) so you can have a better understanding of our contribution guidelines.
