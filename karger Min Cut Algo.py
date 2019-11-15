import random
from copy import deepcopy


def readData(filename= "kargerMinCut.txt"):
    file = open(filename)

    graph = {}
    for line in file:
        sequence = line.split()
        graph[sequence[0]] = sequence[1:]

    return graph



class Graph(object):

    def __init__(self,graph = {}):

        self.graph = graph
        self.copy = None




    def kargerMinCut(self):

        length = []

        while len(self.copy) > 2:

            (v1,v2) = self.choose_random_edge()

            self.copy[v1].extend(self.copy[v2])


            for v in self.copy[v2]:  #replacing adjacent edges of v2 to v1
                self.copy[v].remove(v2) # and removing v2 from them
                self.copy[v].append(v1)


            while v1 in self.copy[v1]:  #removing self loops
                    self.copy[v1].remove(v1)

            del (self.copy[v2])

        for v in self.copy:
            length.append(len(self.copy[v]))

        return length[0]

            



    def choose_random_edge(self):

        v1 = random.choice(list(self.copy.keys()))
        v2 = random.choice(list(self.copy[v1]))

        return (v1,v2)



    def getMinCut(self,n = None):

        if not n:
            n = len(self.graph)

        i = 0
        min_count = (len(self.graph)*(len(self.graph)-1))//2 #no of max edges
        while i < n:

            self.copy = deepcopy(self.graph)

            min_cut = self.kargerMinCut()

            if min_cut < min_count:
                min_count = min_cut

            i += 1

        return min_count
            
        
        
        
if __name__ == '__main__':

    G = readData()
    graph = Graph(G)
    print(graph.getMinCut())
