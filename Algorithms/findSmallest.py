def findSmall(array):
    small = array[0]
    s_index = 0
    for i in range(0 , len(array)):
        if array[i] < small:
            small = array[i]
            s_index = i
    return (small,s_index)

print(findSmall([347,234,13,1334,13,74,4]))
