## Selection Sort Algorithm

### What is Selection Sort?
Selection Sort is a simple comparison-based sorting algorithm that divides the array into two parts:
- Sorted part (left side)
- Unsorted part (right side)

In each pass, it finds the minimum element from the unsorted part and places it at the correct position in the sorted part.

### Steps
1. Start from the first index.
2. Find the smallest element in the remaining unsorted array.
3. Swap it with the element at the current index.
4. Move the boundary of the sorted part one step right.
5. Repeat until the array is sorted.

### Example
Array: `[64, 25, 12, 22, 11]`  
After first pass → `[11, 25, 12, 22, 64]`

### Time Complexity
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)

### Space Complexity
- O(1) (In-place sorting)

### Key Points
- Simple and easy to understand
- Not stable by default
- Inefficient for large datasets
