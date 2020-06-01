
class Node():

    def __init__(self , element):
        self.get = element
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None

    def display(self):
        cur = self.head
        while cur != None:
            print(cur.get)
            cur = cur.next

    def insert(self , element):
        new = Node(element)
        new.next = self.head
        self.head = new

    def append(self , element):
        new = Node(element)
        last = self.head
        if self.head == None:
            self.head = new
        while last.next:
            last = last.next
        last.next = new

    def custom_insert(self , element , position):
        new = Node(element)
        new.next = position.next
        position.next = new

    def remove(self , element):
        temp = self.head

        if temp != None:
            if temp.get == element:
                self.head = temp.next
                temp = None
                return
        while temp != None:
            if temp.get == element:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None






a = LinkedList()
a.head = Node(1)
e2 = Node(2)
e3 = Node(3)
a.head.next = e2
e2.next = e3
#a.display()
a.insert(5)
#a.display()
a.append(10)
a.custom_insert(11,a.head.next)
#a.display()
a.remove(5)
a.display()
