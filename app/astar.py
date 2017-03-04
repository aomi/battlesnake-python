#Matts Node Init

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


# A*
#initialize the open list
#initialize the closed list
#put the starting node on the open list (you can leave its f at zero)

#while the open list is not empty
#    find the node with the least f on the open list, call it "q"
#    pop q off the open list
#    generate q's 8 successors and set their parents to q
#    for each successor
#    	if successor is the goal, stop the search
#        successor.g = q.g + distance between successor and q
#        successor.h = distance from goal to successor
#        successor.f = successor.g + successor.h
#
#        if a node with the same position as successor is in the OPEN list \
#            which has a lower f than successor, skip this successor
#        if a node with the same position as successor is in the CLOSED list \
#            which has a lower f than successor, skip this successor
#        otherwise, add the node to the open list
#    end
#    push q on the closed list
#end


#Determines distance via manhattan style
def manhattanWeight(current, goal):
    return abs(current.x - goal.x) + abs(current.y - goal.y)


#Determine smallest weight Node in OpenList
def smallestWeight(openNodeList, previousWeighting):
    if (len(openNodeList)<=3):
        return compareMinimums(openNodeList)
    else:
        currentSmallestWeighting = compareMinimums(openNodeList[:3])
        if (currentSmallestWeighting <= previousWeighting):
            return currentSmallestWeighting
        else:
            return compareMinimums(openNodeList)


#Compares list of nodes for smallest minimum weight
def compareMinimums(openNodeList):
    for openNode in openNodeList:
        if openNode.weight < minimumWeight:
            minimumWeight = openNode.weight
            minimumWeightNode = openNode
    return minimumWeightNode



def astar(start, goal, grid):

    start.weight = 0
    openList = [start]
    closedList = []
