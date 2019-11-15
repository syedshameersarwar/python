import sys


class MinHeap:

    def __init__(self,capacity):

        self.capacity = capacity
        self.size = 0
        self.list = []


    def parent(self,index):
        return (index-1)//2


    def left(self,index):
        return (2*index)+1


    def right(self,index):
        return (2*index)+2


    def heapify(self,index):

        left = self.left(index)
        right = self.right(index)
        smallest = index

        if left < self.size and self.list[left] < self.list[index]:
            smallest = left

        if right < self.size and self.list[right] < self.list[smallest]:
            smallest = right

        if smallest != index:
            self.list[smallest],self.list[index] = \
                                            self.list[index],self.list[smallest]
            self.heapify(smallest)


    def get_min(self):
        return self.list[0]


    def decrease_key(self,index,new_value):

        self.list[index] = new_value
        self.fix_heap(index)


    def fix_heap(self,index):
        #print(index)
        while index != 0 and self.list[self.parent(index)] > self.list[index]:
            self.list[self.parent(index)],self.list[index] = \
                                self.list[index],self.list[self.parent(index)]

            index = self.parent(index)


    def insert_key(self,value):

        if self.size == self.capacity:
            print("Overflow: Could not insert Key.")
            return

        self.size += 1
        index = self.size-1

        self.list.append(value)
        #print(value)
        self.fix_heap(index)


    def extract_min(self):

        if self.size <= 0:
            return None

        if self.size == 1:
            self.size -= 1
            return self.list[0]

        root = self.list[0]
        self.list[0] = self.list[self.size-1]
        self.size -= 1
        self.list.pop()
        self.heapify(0)

        return root


    def delete_key(self,index):

        self.decrease_key(index,(-sys.maxsize -1))
        self.extract_min()


    def display(self):

        print(self.list)



if __name__ == '__main__':
    
    heapObj = MinHeap(11) 
    heapObj.insert_key(3) 
    heapObj.insert_key(2) 
    heapObj.delete_key(1) 
    heapObj.insert_key(15) 
    heapObj.insert_key(5) 
    heapObj.insert_key(4) 
    heapObj.insert_key(45) 
  
    print(heapObj.extract_min(),end = ' ') 
    print(heapObj.get_min(),end = ' ')
    heapObj.decrease_key(2, 1) 
    print(heapObj.get_min()) 
    heapObj.display()
    

                                            
        
