class LinkedList():

    def __init__(self):
        self.linkedList = []
        self.head = None
        self.current = 1

    def isEmpty(self):

        return(len(self.linkedList) == 0)

    def node(self , element):

        if self.isEmpty():
            self.head = element
            self.linkedList.append(element)
        else:
            self.linkedList.append(element)

    def see_head(self):
        print(self.head)

    def display(self):
        print(self.linkedList)

    def next(self ):
        if self.current < len(self.linkedList):
            print(self.linkedList[self.current])
            self.current += 1
        else:
            print("No more values in linkedList")





a = LinkedList()
a.node(4)
a.see_head()
a.node(5)
a.node(6)
a.display()
a.next()
a.next()
a.next()
