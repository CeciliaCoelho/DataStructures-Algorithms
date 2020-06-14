class Node():

    def __init__(self , element):
        self.get = element
        self.next = None
        self.prev = None

class doublyLinkedList():

    def __init__(self):
        self.head = None

    def display(self):
        cur = self.head
        while cur != None:
            print(cur.get)
            cur = cur.next

    def append(self , element):
        new = Node(element)
        last = self.head
        if self.head == None:
            self.head = new
        while last.next:
            last = last.next
        last.next = new

    def insert(self , element):
        new = Node(element)
        new.next = self.head
        self.head = new




a = doublyLinkedList()
a.head = Node(1)
e2 = Node(2)
e3 = Node(3)
a.head.next = e2
e2.prev = a.head
e2.next = e3
e3.prev = e2
print(a.head.next.next.prev.get)
print("-------------")
a.insert(6)
a.append(9)
a.display()
