def Shell_sort(list):
    size = len(list)
    gap = size//2
    while gap > 0:
        for i in range(gap, size):
            anchor = list[i]
            j = i
            while j>=gap and list[j-gap]>anchor:
                list[j] = list[j-gap]
                j-=gap
            list[j] = anchor
        gap = gap // 2

if __name__ == "__main__":
    list = [3,2,6,3,787,31,1,4]
    Shell_sort(list)
    print(list)