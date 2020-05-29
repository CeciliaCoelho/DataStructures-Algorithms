print("In what range is the number you want me to find?")
low = int(input("low:"))
high = int(input("high:"))
c = False

guess = ((low + high) // 2)

while c == False:
    t = ""
    lh = ""
    print(guess)
    while t != "Y" and t != "N":
        t = input("Is this your number? (Y/N)")

    if t == "Y":
        c = True
        print("Found it!")
    if t == "N":
        while lh != "l" and lh != "h":
            lh = input("Is is lower or higher? (l/h)")

        if lh == "h":
            low = guess + 1
        if lh == "l":
            high = guess - 1
        guess = ((low + high) // 2)
