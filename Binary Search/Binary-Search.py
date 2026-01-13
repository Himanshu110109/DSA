from utils import time_it

@time_it
def linear_search(num_list, target):
    for id, num in enumerate(num_list):
        if num == target:
            return id

@time_it
def binary_search(num_list, target):
    left = 0
    right = len(num_list) - 1
    middle = 0

    while left <= right:
        middle = (right + left) // 2
        mid_num = num_list[middle]

        if mid_num == target:
            return middle

        if mid_num < target:
            left = middle + 1

        if mid_num > target:
            right = middle - 1

    return -1

@time_it
def binary_search_recursive(num_list, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if mid >= len(num_list) or mid < 0:
        return -1

    if num_list[mid] == target:
        return num_list[mid]

    if num_list[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

    return binary_search_recursive(num_list, target, left, right)

if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    target = 8

    r3 = binary_search_recursive(num_list, target, 0, len(num_list))
    print(f"{target} found at {r3} using recursive binary search")
    result = binary_search(num_list, target)
    print(f"{target} found at {result} using binary search")
    r2 = linear_search(num_list, target)
    print(f"{target} found at {r2} using linear search")
