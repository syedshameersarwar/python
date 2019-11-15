from QueueLinkedList import Queue
from StackLinkedList import Stack
from collections import defaultdict 
import sys
import threading


class Graph(object):


    def __init__(self,graph = defaultdict(list)):

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

        self.__checkVertex(int(vertex1))
        self.__checkVertex(int(vertex2))
        #self.__checkVertex(-int(vertex2))
        
        self.graph[int(vertex1)].append(int(vertex2))
        #self.graph[int(vertex2)].append(int(vertex1))
        




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
            self.sc.append(source_vertex)
                        
        for v in self.graph[source_vertex]:
            '''
            if strongly_connected:
                if v<0:
                    v = -v
                else:
                    continue
            else:
                if v<0:
                    continue
            '''
            if not self.visited[v]:
                self.DFS(v,topological_ordering,strongly_connected)




        if topological_ordering:  #Application 1
            self.topological_ordering[source_vertex] = \
                                                     self._current_label
            self._current_label -= 1


        if strongly_connected: #Application 2
            self.__stack.push(source_vertex)

        




    def get_topologicl_ordering(self):

        self.init_visited()
        self._current_label = len(self.graph)

        for vertex in self.graph:

            if not self.visited[vertex]:
                self.DFS(vertex,topological_ordering=True)

        return self.topological_ordering





    def strongly_connected_components(self):
        '''
        
        #geeksforgeeks implementation alias
        self.init_visited()
        
        for v in self.graph:
            if not self.visited[v]:
                self.DFS(v,strongly_connected = True)

        reverse = self.__getReverse()

        reverse.init_visited()

        self.__stack.displayStack()
        reverse.sizes = []
        reverse.sc = []
        while not self.__stack.isEmpty():

            vertex =  self.__stack.pop()
            
            if not reverse.visited[vertex]:
                reverse.DFS(vertex)
                print()
                print()
                reverse.sizes.append(len(reverse.sc))
                reverse.sc = []
        '''

        
        self.init_visited()    #course implementation

        reverse = self.__getReverse()

        reverse.init_visited()
        
        for v in reverse.graph: #use self.__getReverse().graph instead of 
                                #reverse.graph if throw runtime error of dict 
                                #modifying, or use geeksforgeeks method
            if not reverse.visited[v]:
                reverse.DFS(v,strongly_connected = True)
                
        self.__stack = reverse.__stack
        #self.__stack.displayStack()

        self.sizes = []
        self.sc = []
        
        while not self.__stack.isEmpty():

            vertex = self.__stack.pop()

            if not self.visited[vertex]:
                self.DFS(vertex)
                print()
                self.sizes.append(len(self.sc))
                self.sc = []
        
        print(sorted(self.sizes,reverse=True))
        
            
     


        
    def displayGraph(self):
        print()
        print(self.graph)


    



def main():

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
    g.strongly_connected_components()
    
if __name__ == '__main__':
    '''
    threading.stack_size(67108864*2) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
    '''
    main()
