def  Selection_Sort(list):
    size = len(list)
    for i in range(size-1):
        min_index = i
        for j in range(i+1, size):
            if list[j] < list[min_index]:
                min_index = j
        if i != min_index:
            list[i], list[min_index] = list[min_index], list[i]

if __name__ == "__main__":
    list = [5,3,5,2,9,78,4,2]
    Selection_Sort(list)
    print(list)