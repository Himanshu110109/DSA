## Shell Sort (Brief Explanation)

**Shell Sort** is an optimization of **Insertion Sort** that allows the exchange of elements that are far apart.

### How It Works
- The array is divided using a **gap** value.
- Elements at a distance of `gap` are compared and sorted.
- The gap is gradually reduced until it becomes `1`.
- When gap = `1`, the algorithm behaves like a normal Insertion Sort on a nearly sorted array.

### Why It’s Faster Than Insertion Sort
- Insertion Sort is slow for large, unsorted arrays.
- Shell Sort reduces large displacements early using bigger gaps.
- Final pass becomes very fast because the array is almost sorted.

### Time Complexity
- Worst case: **O(n²)** (depends on gap sequence)
- Average case: **~O(n^1.5)**
- Best case: **O(n log n)** (practically)

### Space Complexity
- **O(1)** (in-place sorting)

### Key Points
- Uses multiple passes with decreasing gaps
- Not a stable sort
- Faster than Insertion Sort for large datasets
