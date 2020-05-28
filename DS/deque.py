#complexity O(1)

class Deque():

    def __init__(self):
        self.deque = []

    def insertFront(self , element):
        self.deque = [element] + self.deque

    def insertBack(self , element):
        self.deque.append(element)

    def display(self):
        if not self.isEmpty():
            print(self.deque)
        else:
            print("Queue is Empty")

    def isEmpty(self):
        return (len(self.deque) == 0)

    def deleteFront(self):
        if not self.isEmpty():
            del self.deque[0]
            return True

    def deleteBack(self):
        if not self.isEmpty():
            del self.deque[-1]
            return True

    def getFront(self):
        if not self.isEmpty():
            print(self.deque[0])

    def getBack(self):
        if not self.isEmpty():
            print(self.deque[-1])





a = Deque()
a.insertFront(1)
a.insertFront(2)
a.insertBack(5)
a.display()
a.deleteFront()
a.display()
a.deleteBack()
a.display()
a.deleteBack()
a.deleteBack()
a.display()
a.insertFront(10)
a.insertFront(11)
a.insertBack(9)
a.getFront()
