class Stack(object):

    def __init__(self):
        self.stack = []


    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        return(len(self.stack) == 0)

    def push(self , element):
        self.stack.append(element)

    def pop(self):
        if not self.isEmpty():
            print(self.stack[-1])
            del self.stack[-1]
        return self.stack

    def peek(self):
        if not self.isEmpty():
            print(self.stack[-1])

    def see(self):
        for i in range(0,len(self.stack)):
            print(self.stack[i])



a = Stack()
a.push(1)
a.pop()
a.pop()
