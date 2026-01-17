def bubble_sort(list):
    size = len(list)
    for j in range (size - 1):
        swapped = False
        for i in range(size - 1):
            if list[i] > list[i + 1]:
                tmp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = tmp
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    list = [8,15,4,2,56,1,6,9]
    bubble_sort(list)
    print(list)