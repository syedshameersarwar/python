def SolveMaze(maze,size):
    possiblePath = [[0 for x in range(size)] for y in range(size)]
    if SolveMazeSub(maze,0,0,possiblePath,size)==False:
        print("Possible path does not exist.")
        return False
    printPossiblePath(possiblePath)
    return True
    

def isSafeBlock(maze,x,y,size):
    if (x >= 0 and x<size) and (y>=0 and y <size) and maze[x][y] == 1:
        return True
    return False

def SolveMazeSub(maze,x,y,possiblePath,size):
    if x==size-1 and y == size-1:
        possiblePath[x][y] = 1
        return True
    if isSafeBlock(maze,x,y,size) == True:
        possiblePath[x][y] = 1
        if SolveMazeSub(maze,x+1,y,possiblePath,size) == True:
            return True
        if SolveMazeSub(maze,x,y+1,possiblePath,size) == True:
            return True
        possiblePath[x][y] = 0
        return False

def printPossiblePath(path):
    for i in path:
        for j in i:
            print(str(j)+ " ",end = "")
        print("")

if __name__ == "__main__": 
    # Initialising the maze 
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ]
    SolveMaze(maze,4)


''' Rat in a maze Problem

https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/

'''
