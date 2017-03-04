
#class NodeAnalysis:
#    def __init__(self, centreNode, up, down, left, right):
#        self.mainNode = centreNode


#http://web.mit.edu/eranki/www/tutorials/search/
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

def astar(start, goal):

    start.netWeight = 0
    lastTurnWeight = 0
    openList = [start]
    closedList = []

    while(len(openList)>0):

        centreNode = findSmallestWeightedNode(openList, lastTurnWeight)
        openList.remove(centreNode)

        successors = []
        if (centreNode.up != 0): successors.append(centreNode.up)
        if (centreNode.down != 0): successors.append(centreNode.down)
        if (centreNode.left != 0): successors.append(centreNode.left)
        if (centreNode.right != 0): successors.append(centreNode.right)

        for successor in successors:

            successor.parent = centreNode
            if (checkNodeEquality(successor, goal)): return
            successor.distance = manhattanWeight(successor, goal)
            successor.netWeight = successor.weight + successor.distance

            if (not(successor in openList and successor.netWeight < openList[openList.index(successor)].netWeight)):
                if (not(successor in closedList and successor.netWeight < closedList[closedList.index(successor)].netWeight)):
                    openList.insert(0,successor)

        closedList.insert(0,centreNode)

def checkNodeEquality(nodeA, nodeB):
    return nodeA.x == nodeB.x and nodeA.y == nodeB.y

def findSmallestWeightedNode(openNodeList, previousWeighting):
    if (len(openNodeList)<=4):
        return compareMinimums(openNodeList)
    else:
        smallestWeightedNode = compareMinimums(openNodeList[:4])
        if (smallestWeightedNode.netWeight <= previousWeighting):
            return smallestWeightedNode
        else:
            return compareMinimums(openNodeList)

def compareMinimums(openNodeList):
    minimumWeight = 10000000
    for openNode in openNodeList:
        if openNode.netWeight < minimumWeight:
            minimumWeight = openNode.netWeight
            minimumWeightNode = openNode
    return minimumWeightNode