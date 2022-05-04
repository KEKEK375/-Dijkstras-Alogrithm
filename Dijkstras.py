from matrix import AdjacencyMatrix as AM
from matrix import Node as N
from errors import *
import random as r

def Dijkstras(fromID, toID):
    nodes = [] #type: list[N]
    for i in range(60):
        nodes.append(N())
    ## creates new adjacency matrix object
    AdMat = AM(nodes)

    print(AdMat)

    ## list that traces best path for each node
    TraceDict = {} #type: dict[list[N, int, N]]
    for i,node in enumerate(nodes):
        TraceDict[i] = []
        TraceDict[i].append(node)
        if fromID == node.id:
            TraceDict[i].append(0)
            TraceDict[i].append(node)
        else:
            TraceDict[i].append(float("inf")) # Changed this from -1 to infinity - KEKEK
            TraceDict[i].append(None)
        node.SetChecked(False)

    #print(TraceDict)

    while not TraceDict[toID][0].GetChecked():
        ## finds the unchecked node with the shortest current path
        shortestPath = [float("inf"), float("inf")]
        for i in(TraceDict):
            if TraceDict[i][1] >= 0: # I don't think this line is necessary anymore - KEKEK
                if not TraceDict[i][0].GetChecked():
                    if TraceDict[i][1] < shortestPath[0]:
                        shortestPath[0],shortestPath[1] = TraceDict[i][1],TraceDict[i][0]
        currentNode = shortestPath
        #print(currentNode)

        ''' Pseudocode for the trace table type thing:
            for differentNode in nodes
                if currentNode has path to differentNode
                    if differentNode[bestPath] > currentNode[bestPath] + pathBetweenNodes
                        differentNode[bestPath] = currentNode[bestPath] + pathBetweenNodes'''

        #Problem case when the fromNode has no arcs to other nodes, or there is no way of getting from A to B. In this case it should output -1? -J

        #This is my attempt at the algorithm, it does not work :( but I think its close -J

        #I think it doesn't work because i messed up the currentNode bit, but i think I've fixed it now so it might work - KEKEK

        #Actually having looked at it I think it's because TraceDict[i][0] is Node: i, not just i - KEKEK
        #I've changed __repr__ in the Node class so that it just return the id - KEKEK
        #Third and hopefully final problem - all the best paths are set to -1 so they don't get improved - KEKEK
        #I've now also changed this

        # Slightly altered and I think it works - KEKEK
        
        for i in TraceDict:
            if not TraceDict[i][0].GetChecked():
                if AdMat[TraceDict[i][0].id][currentNode[1].id] >= 0:
                    if TraceDict[i][1] > currentNode[0] + AdMat[TraceDict[i][0].id][currentNode[1].id]:
                        TraceDict[i][1] = currentNode[0] + AdMat[TraceDict[i][0].id][currentNode[1].id]
                        TraceDict[i][2] = currentNode[1]
        
        currentNode[1].SetChecked(True)
    
    print(TraceDict[toID][1])
    path = []
    node = TraceDict[toID][0]
    while node.id != fromID:
        path.append(str(node.id))
        node = TraceDict[node.id][2]
        if node == float("inf"):
            raise NoConnection()
    path.append(str(node.id))
    string = " -> ".join(path[::-1])
    print(string)

if __name__ == "__main__":
    Dijkstras(0, r.randint(1, 59))