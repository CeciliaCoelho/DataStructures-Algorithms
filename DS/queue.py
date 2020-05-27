def create():
    q = []
    return q

def enqueue(q , element):
    q.append(element)

def dequeue(q):
    if not isEmpty(q):
        del q[0]
        return q

def isEmpty(q):
    if len(q) == 0:
        print("Queue is empty!")
    return (len(q) == 0)

def peek(q):
    print(q[0])

def see(q):
    for i in q:
        print(i)

a = create()
enqueue(a,1)
peek(a)
enqueue(a,2)
dequeue(a)
isEmpty(a)
peek(a)
dequeue(a)
dequeue(a)
