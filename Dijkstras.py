from matrix import AdjacencyMatrix as AM
from matrix import Node as N
from time import sleep

def Dijkstras(fromID, toID):
    nodes = [] #type: list[N]
    for i in range(6):
        nodes.append(N())
    ## creates new adjacency matrix object
    AdMat = AM(nodes)

    ## list that traces best path for each node
    TraceDict = {} #type: dict[list[N, int, N]]
    for i,node in enumerate(nodes):
        TraceDict[i] = []
        TraceDict[i].append(node)
        if fromID == node.id:
            TraceDict[i].append(0)
            TraceDict[i].append(node)
        else:
            TraceDict[i].append(-1)
            TraceDict[i].append(None)
        node.SetChecked(False)

    #print(TraceDict)

    while not TraceDict[toID][0].GetChecked():
        ## finds the unchecked node with the shortest current path
        shortestPath = [float("inf"), float("inf")]
        for i in(TraceDict):
            if TraceDict[i][1] >= 0:
                if not TraceDict[i][0].GetChecked():
                    if TraceDict[i][1] < shortestPath[0]:
                        shortestPath = TraceDict[i]
        currentNode = shortestPath
        print(currentNode)

        ''' Pseudocode for the trace table type thing:
            for differentNode in nodes
                if currentNode has path to differentNode
                    if differentNode[bestPath] > currentNode[bestPath] + pathBetweenNodes
                        differentNode[bestPath] = currentNode[bestPath] + pathBetweenNodes'''

        """             
        for i in TraceDict:
            if not TraceDict[i][0].GetChecked():
                if AdMat[TraceDict[i][0].id][currentNode[0].id] >= 0:
                    if TraceDict[i][1] > currentNode[1] + AdMat[TraceDict[i][0].id][currentNode[0].id]:
                        TraceDict[i][1] = currentNode[1] + AdMat[TraceDict[i][0].id][currentNode[0].id]
                        TraceDict[i][2] = currentNode[0]
        
        currentNode[0].SetChecked(True)
        
        print(currentNode[0].id,TraceDict)
        """

        ##Remove this sleep, its just for testing purposes
        sleep(1)

Dijkstras(0,4)