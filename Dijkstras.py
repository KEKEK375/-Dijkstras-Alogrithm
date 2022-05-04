from matrix import AdjacencyMatrix as AM
from matrix import Node as N

def Dijkstras(fromID, toID):
    nodes = []
    for i in range(6):
        nodes.append(N())
    ## creates new adjacency matrix object
    AdMat = AM(nodes)

    ## list that traces best path for each node
    TraceList = [] #type: list[tuple[N, int, N]]
    for i,node in enumerate(nodes):
        TraceList.append([])
        TraceList[i].append(node)
        if fromID == node.id:
            TraceList[i].append(0)
        else:
            TraceList[i].append(-1)
        TraceList[i].append(None)

    #print(TraceList)





Dijkstras(0,4)