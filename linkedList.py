class Node(object):

    def __init__(self,data=None):

        self.data = data
        self.next = None


    def setData(self,data):
        self.data = data

    def setNext(self,node):
        self.next = node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next




class LinkedList(object):


    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0


    def add_head(self,data):

        temp = Node(data)

        if self.head == None:
            self.tail = temp
        else:
            temp.setNext(self.head)

        self.head = temp


    def add_tail(self,data):

        temp = Node(data)

        if self.tail == None:
            self.head = temp
        else:
            self.tail.setNext(temp)
            
        self.tail = temp


    def delete_head(self):

        temp = self.head

        if temp == None:
            print("List Empty,deletion failed")
            return
        data = self.head.getData()

        
        self.head = self.head.getNext()

        if self.head == None:
            self.tail = None

        del(temp)

        return data


        
    def isEmpty(self):
        return self.head == None



    def getSize(self):
        
        current = self.head

        while current != None:
            self.size += 1
            current = current.getNext()

        return self.size

        
        
    def display(self):

        current = self.head

        if current == None:
            print("List Empty")
            return

        List = []
        while current != None:
            List.append(current.getData())
            current = current.getNext()

        print(List)
        


    

if __name__ == '__main__':
    L = LinkedList()
    #L.add_head(7)
    L.add_head(5)
    L.add_head(3)
    L.add_head(4)
    L.add_head(7)
    L.add_head(5)
    L.delete_head()
    L.display()
    print(L.getSize())
            
            
