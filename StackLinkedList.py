from linkedList import LinkedList


class Stack(object):

    def __init__(self):

        self.List = LinkedList()


    def push(self,data):

        self.List.add_head(data)


    def pop(self):

        return self.List.delete_head()


    def displayStack(self):
        
        self.List.display()


    def isEmpty(self):

        return self.List.isEmpty()


    def getSize(self):

        return self.List.getSize()



if __name__ == '__main__':
    
    S = Stack()
    S.push(10)
    S.push(20)
    print(S.pop())
    S.pop()
    S.push(30)
    S.push(40)
    S.push(50)
    print(S.pop())
    
    #Q = Queue()
    #print(S.displayStack())
