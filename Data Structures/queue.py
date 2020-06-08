#complexity O(1)
class queue(object):


    def __init__(self):
        self.q = []


    def enqueue(self , element):
        self.q.append(element)

    def dequeue(self):
        if not self.isEmpty():
            del self.q[0]
            return self.q

    def isEmpty(self):
        if len(self.q) == 0:
            print("Queue is empty!")
        return (len(self.q) == 0)

    def peek(self):
        print(self.q[0])

    def see(self):
        for i in self.q:
            print(i)

a = queue()
a.enqueue(1)
a.peek()
a.enqueue(2)
a.dequeue()
a.isEmpty()
a.peek()
a.dequeue()
a.dequeue()
