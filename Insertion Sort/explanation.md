# Insertion Sort Algorithm

## What is Insertion Sort?
Insertion Sort is a simple comparison-based sorting algorithm that works by building the sorted array one element at a time.

It follows the idea of inserting each new element into its correct position in the already sorted part of the array.

---

## Core Idea
- Assume the first element is already sorted
- Pick the next element (called key or anchor)
- Compare it with elements on the left
- Shift larger elements one position to the right
- Insert the key at its correct position

---

## Step-by-Step Example

**Input Array:**  
[8, 3, 5, 2]

### Step 1
- Sorted part: [8]
- Key = 3
- Shift 8 to the right and insert 3

Result:  
[3, 8, 5, 2]

---

### Step 2
- Sorted part: [3, 8]
- Key = 5
- Shift 8 and insert 5 after 3

Result:  
[3, 5, 8, 2]

---

### Step 3
- Sorted part: [3, 5, 8]
- Key = 2
- Shift all elements to the right
- Insert 2 at the beginning

Result:  
[2, 3, 5, 8]

---

## Time Complexity
- Best Case (Already Sorted): O(n)
- Average Case: O(n²)
- Worst Case (Reverse Sorted): O(n²)

---

## Space Complexity
- O(1) (In-place sorting algorithm)

---

## Advantages
- Simple and easy to understand
- Efficient for small datasets
- Works well with nearly sorted arrays
- Stable sorting algorithm

---

## Disadvantages
- Very slow for large datasets
- Not suitable for performance-critical applications

---

## When to Use Insertion Sort?
- When the dataset size is small
- When the array is nearly sorted
- For educational purposes
- When memory usage must be minimal
