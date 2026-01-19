def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end
def Quick_sort(elements, start, end):
    if start < end:
        p1 = partition(elements, start, end)
        partition(elements, start, p1 - 1)
        partition(elements, p1 + 1, end)

if __name__ == "__main__":
    elements = [5,2,6,9,3,15,2,18]
    Quick_sort(elements, 0, len(elements) - 1)
    print(elements)