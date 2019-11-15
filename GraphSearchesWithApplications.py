from QueueLinkedList import Queue
from StackLinkedList import Stack
from collections import defaultdict 



class Graph(object):


    def __init__(self,graph = dict()):

        self.graph = graph
        self.visited = defaultdict(list)
        self.__queue = Queue()

        self.shortest_path_distance = dict() #Application 1 BFS

        self.topological_ordering = {} #Application DFS 1
        self._current_label = None

        self.__stack = Stack() #Application DFS 2



    def __checkVertex(self,vertex):

        if vertex not in self.graph:
            
            self.graph[vertex] = []



    def init_visited(self):

        for v in self.graph:
                self.visited[v] = False
        



    def add_edge(self,vertex1,vertex2):

        self.__checkVertex(vertex1)
        self.__checkVertex(vertex2)
        
        self.graph[vertex1].append(vertex2)
        




    def BFS(self,source_vertex,shortest_path = False,\
                          connected_component = False): #both applications


        if not connected_component:
            self.init_visited()

        
        self.visited[source_vertex] = True
        self.__queue.enqueue(source_vertex)


        if shortest_path:
            self.shortest_path_distance[source_vertex] = 0

            
        while not self.__queue.isEmpty():

            v = self.__queue.dequeue()

            if not shortest_path:
                print(v,end = ' ')

            for vertex in self.graph[v]:

                if not self.visited[vertex]:

                    if shortest_path:
                        self.shortest_path_distance[vertex] = \
                                     self.shortest_path_distance[v] + 1   

                    self.visited[vertex] = True

                    self.__queue.enqueue(vertex)
        print()




    def shortest_path(self,source_vertex):

        self.BFS(source_vertex,shortest_path = True)


        for v in self.shortest_path_distance:

            print("Shortest path distance from " \
                  ,source_vertex," to vertex ",v,
                  " = ",self.shortest_path_distance[v])




    def connected_components(self):

        self.init_visited()

        count = 1
        
        for vertex in self.graph:
            
            if not self.visited[vertex]:

                print("Connected Component ", \
                                count,": ",end = '')

                self.BFS(vertex,connected_component = True)

                count += 1





    def __getReverse(self):
        
        g = defaultdict(list)  #will never throw KeyError

        for vertex in self.graph:
            for v in self.graph[vertex]:
                g[v].append(vertex)

        
        return Graph(g)
        

        


            
    def DFS(self,source_vertex,topological_ordering=False, \
                               strongly_connected=False): 

        self.visited[source_vertex]= True
        
        if (not topological_ordering) and (not strongly_connected):
            print(source_vertex,end = ' ')

            
        for v in self.graph[source_vertex]:
            
            if not self.visited[v]:
                self.DFS(v,topological_ordering,strongly_connected)




        if topological_ordering:  #Application 1
            self.topological_ordering[source_vertex] = \
                                                     self._current_label
            self._current_label -= 1


        if strongly_connected: #Application 2
            self.__stack.push(source_vertex)

        




    def get_topological_ordering(self):

        self.init_visited()
        self._current_label = len(self.graph)

        for vertex in self.graph:

            if not self.visited[vertex]:
                self.DFS(vertex,topological_ordering=True)

        return self.topological_ordering





    def strongly_connected_components(self):

        '''
        geeksforgeeks implementation alias
        self.init_visited()

        for v in self.graph:
            if not self.visited[v]:
                self.DFS(v,strongly_connected = True)

        reverse = self.__getReverse()

        reverse.init_visited()

        self.__stack.displayStack()

        while not self.__stack.isEmpty():

            vertex =  self.__stack.pop()
            
            if not reverse.visited[vertex]:
                reverse.DFS(vertex)
                print()
       '''

                     
        self.init_visited()    #course implementation

        reverse = self.__getReverse()

        reverse.init_visited()

        for v in self.__getReverse().graph: #using self.__getReverse() cuz of error
                                           # equivalent to reverse.graph
            if not reverse.visited[v]:
                reverse.DFS(v,strongly_connected = True)
                
        self.__stack = reverse.__stack
        #self.__stack.displayStack()
        
        while not self.__stack.isEmpty():

            vertex = self.__stack.pop()

            if not self.visited[vertex]:
                self.DFS(vertex)
                print()
           
            
     


        
    def displayGraph(self):
        print()
        print(self.graph)




if __name__ == '__main__':
    '''
    g = Graph()
    ***
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)
    g.add_edge(3,3)
    
    g.add_edge(0,4)
    g.add_edge(4,6)
    g.add_edge(5,7)
    g.add_edge(2,2)
    g.add_edge(8,12)
    '''
    #data for checking topological ordering
    g = Graph()
    g.add_edge(1,2) 
    g.add_edge(1,3)
    g.add_edge(2,4)
    g.add_edge(3,4)
    
    

    #print("Breadth First Traversal(starting from vertex 2): ")

    #g.init_visited() #initalizing explored nodes with False,for DFS
    #g.DFS(2)

    print(g.get_topological_ordering())
    #print(dir(g))
    #g._Graph__checkVertex(2) # name mangling
    g.displayGraph()

    #g.shortest_path(2) #Application 1 BFS
    
    print()
    '''
    #g.connected_components() ##Application 2 BFS
    
    #testing for strongly connected components
    g = Graph()
    g.add_edge(1, 0) 
    g.add_edge(0, 2) 
    g.add_edge(2, 1) 
    g.add_edge(0, 3) 
    g.add_edge(3, 4)
    print('Strongly Connected Components of Graph are : ')
    g.strongly_connected_components()
    '''
    '''
    g = Graph()
    file = open("test.txt")
    count = 0
    for line in file:
        count += 1
        words = line.split()
        print(words[0],words[1])
        g.add_edge(words[0],words[1])

    g.displayGraph()
    print(len(g.graph))
    print(count)
    print("hello world")
    g.strongly_connected_components() #[507, 119, 109, 28, 21, 16]
    ''' 
