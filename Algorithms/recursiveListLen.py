def recursiveListLen(array):
    if array == []:
        return 0
    else:
        return(1 + recursiveListLen(array[1:]))

print(recursiveListLen([1,2,3,6,4,6,7,43,2,22,6,7,2]))
