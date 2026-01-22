def Insertion_Sort(elements):
    for i in range (1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor

if __name__ == "__main__":
    elements = [3, 6, 2, 6, 2, 12, 43, 2, 7, 3]
    Insertion_Sort(elements)
    print(elements)