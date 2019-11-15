from linkedList import LinkedList


class Queue(object):

    def __init__(self):

        self.List = LinkedList()


    def enqueue(self,data):

        self.List.add_tail(data)


    def dequeue(self):

        return self.List.delete_head()

    def displayQueue(self):
        self.List.display()


    def isEmpty(self):

        return self.List.isEmpty()


    def getSize(self):

        return self.List.getSize()


if __name__ == '__main__':
    
    Q = Queue()
    Q.enqueue(10)
    Q.enqueue(20)
    Q.dequeue()
    Q.dequeue()
    Q.enqueue(30)
    Q.enqueue(40)
    Q.enqueue(50)
    print(Q.dequeue())
    
    #Q = Queue()
    print(Q.displayQueue())
    
    
