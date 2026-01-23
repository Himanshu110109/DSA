def merge_sort(list):
    if len(list) <= 1:
        return

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    merge_sort(left)
    merge_sort(right)
    sorter(left, right, list)

def sorter(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

if __name__ == "__main__":
    list = [1,5,2,5,7,3,34,3,98,2,34]
    merge_sort(list)
    print(list)