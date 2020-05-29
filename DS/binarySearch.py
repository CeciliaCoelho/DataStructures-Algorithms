import math

def binary_search(list , item):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = math.floor((low + high) / 2)
        guess = list[middle]

        if guess == item:
            print("The number is: " + str(guess))
            return guess
        if guess > item:
            high = middle -1
        else:
            low = middle + 1
    return None





list = [1,2,3,4,5,6,7,8,9,10]
binary_search(list , 9)
