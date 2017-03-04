MAPSIZEX = 20       #Global variable for X size of map (up-down)
MAPSIZEY = 20       #Global variable for Y size of map (left-right)

class Node:         #Class for spaces on the board, refered to as Nodes
    def __init__(self, xcoord, ycoord):
        self.x = xcoord     #X coordinate of this node
        self.y = ycoord     #Y coordinate of this node
        self.up = 0         #Reference to node up (0 if wall)
        self.down = 0       #Reference to node down (0 if wall)
        self.left = 0       #Reference to node to the left (0 if wall)
        self.right = 0      #Reference to node to the right (0 if wall)
        self.content = 0    #Content of node (eg fruit, empty, enemy, etc.)
        self.weight = 0     #Relative safety of node
        self.distance = 0   #Distance from current fruit
        self.netWeight = 0  #Total weighting of node
        self.parent = 0     #Previous Pathway for Astar


class NodeList:
    def __init__(self, gameID):
        self.gameID = gameID
        #initialize the 2D array of Nodes. empty
        print("Initializing NodeList")
        self.data = [[0 for x in range(MAPSIZEX)] for y in range(MAPSIZEY)]

        # fill the 2d array with empty node instances
        for x in range(MAPSIZEX): #populate
            for y in range(MAPSIZEY):
                self.data[x][y] = Node(x,y)


    def addNode(self,x,y,content):
        self.data[x][y].content = content
        self.data[x][y].x = x
        self.data[x][y].y = y


    def getList(self):
        return self.data

    def clear(self):
        for x in range(MAPSIZEX):
            for y in range(MAPSIZEY):
                self.data[x][y].content = 0

    def connect(self):
        for x in range(MAPSIZEX):
            for y in range(MAPSIZEY):
                if self.data[x][y].x > 0:                  #Checks if node is at the top wall
                    self.data[x][y].up = self.data[x-1][y]
                if self.data[x][y].x < MAPSIZEX-1:         #Checks if node is at the bottom wall
                    self.data[x][y].down = self.data[x+1][y]
                if self.data[x][y].y > 0:                  #Checks if node is at the left wall
                    self.data[x][y].left = self.data[x][y-1]
                if self.data[x][y].y < MAPSIZEY-1:         #Checks if node is at the right wall
                    self.data[x][y].right = self.data[x][y+1]



#This function prints the contents of the map as a grid.
#def printMap(a):
#    for x in a.getList():
#        for y in x:
#            print('',point.content,'',end='')
#        print("\n")


#This function connects all the Nodes in the NodeList (up, down, left, right)
