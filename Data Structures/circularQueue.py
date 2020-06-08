#complexity O(1)

class circularQueue(object):

    def __init__(self , x):
        self.queue = [None] * x
        self.length = 0
        self.size = x
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return (self.length == 0)

    def isFull(self):
        if self.length == self.size:
            print("Full")
        return (self.length == self.size)

    def enqueue(self , element):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
            self.length += 1
        if self.length == 1:
            self.front = 0

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            self.length -= 1
        if self.isEmpty():
            self.front == -1
            self.rear == -1

    def front_peek(self):
        if not self.isEmpty():
            print(self.queue[self.front])
        else:
            return -1

    def rear_peek(self):
        if not self.isEmpty():
            print(self.queue[self.rear])
        else:
            return -1

    def display(self):
        for i in range(self.front , self.rear+1):
            print(self.queue[i] , end = " ")



a = circularQueue(5)
a.isEmpty()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
a.remove()
a.front_peek()
a.enqueue(6)
a.dequeue()
a.front_peek()
a.rear_peek()
