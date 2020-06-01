def recursiveSum(array):
    if array == []:
        return 0
    else:
        return(array[0] + recursiveSum(array[1:]))

print(recursiveSum([6,1,10]))
