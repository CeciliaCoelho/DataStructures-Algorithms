def create():
    stack = []
    return stack

def push(stack , element):
    stack.append(element)

def see(stack):
    for i in range(0,len(stack)):
        print(stack[i])

a = create()
push(a,1)
see(a)
