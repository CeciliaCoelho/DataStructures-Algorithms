class Node():

    def __init__(self , element):
        self.get = element
        self.next = None

class circularLinkedList():

    def __init__(self):
        self.head = None

a = circularLinkedList()
a.head = Node(1)
e2 = Node(2)
e3 = Node(3)
a.head.next = e2
e2.next = e3
e3.next = a.head

print(a.head.next.next.next.get)
