# Merge Sort

## Definition
Merge Sort is a **divide and conquer** sorting algorithm that splits an array into halves, recursively sorts them, and then merges the sorted halves.

## Working Principle
1. Divide the array into two halves.
2. Recursively sort the left half.
3. Recursively sort the right half.
4. Merge the two sorted halves into one sorted array.

## Key Idea
Merging two sorted arrays is easy and efficient. By repeatedly dividing the array, the sorting becomes manageable.

## Time Complexity
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

## Space Complexity
- O(n) (extra space required for merging)

## Characteristics
- Stable sorting algorithm
- Not strictly in-place
- Uses recursion
- Predictable performance (no worst-case degradation)

## Applications
- Used when stable sorting is required
- Suitable for sorting linked lists
- Used in external sorting (large datasets)
