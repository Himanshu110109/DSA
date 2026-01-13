# Binary Search Algorithm

Binary Search is an efficient searching algorithm used on **sorted arrays or lists**.  
It works by repeatedly dividing the search space into half until the target element is found or the range becomes empty.

## How it Works

1. Take the middle element of the sorted list.
2. Compare it with the target value.
3. If it matches, return the index.
4. If the target is smaller, search the left half.
5. If the target is larger, search the right half.
6. Repeat until found or the range is empty.

## Time Complexity

- Best Case: O(1)  
- Average Case: O(log n)  
- Worst Case: O(log n)

## Key Requirement

- The data must be **sorted** before applying Binary Search.

## Example

List: `[2, 4, 6, 8, 10, 12]`  
Target: `8`

Middle element is `6` → target is larger → search right half → find `8`.
