from matrix import AdjacencyMatrix as AM
from matrix import Node as N

def Dijkstras():
    nodes = []
    for i in range(6):
        nodes.append(N())
    ## creates new adjacency matrix object
    AdMat = AM(nodes)

    ## Layout: TraceList = [[CurrentNode, CurrentBestPathLength, NodeFrom], [...], [...] ... ]

    TraceList = [[]]*len(nodes)
    for i,node in enumerate(nodes):
        TraceList[i].append(node)
        TraceList[i].append(-1)
        TraceList[i].append(None)




Dijkstras()