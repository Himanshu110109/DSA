## 📝 Python Dictionary as a Hash Map

A Python dictionary is an implementation of a hash map that stores data in key–value pairs using an internal array and a hash function. The hash function converts each key into a numeric value based on its characters and maps it to a valid index in the array. The value is stored at that index, and this direct mapping allows fast access.

## 📝 How Hashing Works

When a key is used, it is passed through the same hash function to generate the same index every time. This makes it possible to store and retrieve values directly from the array without searching through all elements, which is why dictionary operations are efficient.

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/39b11a8f-f535-4a9e-ace0-c5d06007d72b" />
