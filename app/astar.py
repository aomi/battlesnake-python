#Determines distance via manhattan style
def manhattanWeight(current, goal):
    return abs(current.x - goal.x) + abs(current.y - goal.y)

def astar(start, goal):

    print("start: ", start.x, start.y)
    print("goal: ", start.x, start.y)
    start.netWeight = 0
    lastTurnWeight = 0
    openList = [start]
    closedList = []
    start.parent = 0

    while(len(openList)>0):

        centreNode = findSmallestWeightedNode(openList, lastTurnWeight)
        openList.remove(centreNode)
        successors = []
        if (centreNode.up != 0) and (centreNode.up.content != "wall") and not (centreNode.up in closedList): successors.append(centreNode.up)
        if (centreNode.down != 0) and (centreNode.down.content != "wall")and not (centreNode.down in closedList): successors.append(centreNode.down)
        if (centreNode.left != 0) and (centreNode.left.content != "wall")and not (centreNode.left in closedList): successors.append(centreNode.left)
        if (centreNode.right != 0) and (centreNode.right.content != "wall")and not (centreNode.right in closedList): successors.append(centreNode.right)

        for successor in successors:

            successor.parent = centreNode
            successor.distance = manhattanWeight(successor, goal)
            successor.netWeight = successor.weight + successor.distance
            if (checkNodeEquality(successor, goal)): return goal

            if (not(successor in openList and successor.netWeight < openList[openList.index(successor)].netWeight)):
                if (not(successor in closedList and successor.netWeight < closedList[closedList.index(successor)].netWeight)):
                    openList.insert(0,successor)

        closedList.insert(0,centreNode)
        lastTurnWeight = centreNode.netWeight

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

def calculatePathWeight(start, goal):

    totalWeight = 0
    currentNode = astar(start, goal)

    while (currentNode.parent != 0):
        totalWeight += currentNode.netWeight
        lastNode = currentNode
        currentNode = currentNode.parent

    totalWeight += currentNode.netWeight
    print("currentNode: ", currentNode.x, currentNode.y)
    print("lastNode: ", lastNode.x, lastNode.y)
    if lastNode.x == currentNode.x :
        if (currentNode.y - lastNode.y == 1): direction = "up"
        else: direction = "down"
    elif (currentNode.x - lastNode.x == 1): direction = "left"
    else: direction = "right"

    return [totalWeight, direction]
