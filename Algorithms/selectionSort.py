def findSmall(array):
    small = array[0]
    s_index = 0
    for i in range(0 , len(array)):
        if array[i] < small:
            small = array[i]
            s_index = i
    return s_index

def selectionSort(array):
    ordered = []
    for i in range(0 , len(array)):
        item = findSmall(array)
        ordered.append(array[item])
        del array[item]
    return ordered

print(selectionSort([4,2,6,26,7,6,56,24,85]))
