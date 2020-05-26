def create():
    stack = []
    return stack

def isEmpty(stack):
    if len(stack) == 0:
        print("Stack is empty!")
    return(len(stack) == 0)

def push(stack , element):
    stack.append(element)

def pop(stack):
    if not isEmpty(stack):
        print(stack[-1])
        del stack[-1]

def peek(stack):
    if not isEmpty(stack):
        print(stack[-1])

def see(stack):
    for i in range(0,len(stack)):
        print(stack[i])



a = create()
push(a,1)
push(a,2)
peek(a)
pop(a)
peek(a)
pop(a)
peek(a)
