"""Implementation of the Binary Search algorithm."""

# Binary search is the optimized searching algorithm when compared to Linear search. But binary search is only used when the data is sorted. Binary search algorithm can't be performed on unsorted data.
# The time complexity of the binary search algorithm is O(log n), where "n" is the number of elements in the sorted array.
# To implement binary search, let us consider an example: Let us find whether an element 'k' is present in any integer array 'sorted_array'.

class binarySearch:
    def __init__(self, sorted_array):
        self.array = sorted_array

    def search(self, k):
        #left and right are two pointers which are placed at starting and last element of the array.
        left, right = 0, len(self.array) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Check if the target element is present at the middle
            if self.array[mid] == k:
                return mid

            # If the target element is greater, ignore the left half
            elif self.array[mid] < k:
                left = mid + 1

            # If the target element is smaller, ignore the right half
            else:
                right = mid - 1

        # If the target is not present in the array
        return -1

# Example usage 1:

#initialized an array with 8 random elements 
sorted_array = [3, 12, 17, 23, 43, 46, 57, 71]

#'k' is the target element that we are going to search in sorted_array using binary search.
k = 56

# Create an instance of the BinarySearch class
binary_search_instance = binarySearch(sorted_array)

# Perform binary search and print the result
result = binary_search_instance.search(k)
if result != -1:
    print(f"Element {k} is present at index {result}.")
else:
    print(f"Element {k} is not present in the array.")


# Example usage 2:

#initialized an array with 8 random elements 
sorted_array = [3, 12, 17, 23, 43, 46, 57, 71]

#'k' is the target element that we are going to search in sorted_array using binary search.
k = 57

# Create an instance of the BinarySearch class
binary_search_instance = binarySearch(sorted_array)

# Perform binary search and print the result
result = binary_search_instance.search(k)
if result != -1:
    print(f"Element {k} is present at index {result}.")
else:
    print(f"Element {k} is not present in the array.")
