from matrix import AdjacencyMatrix as AM
from matrix import Node as N

def Dijkstras():
    nodes = []
    for i in range(6):
        nodes.append(N())
    AdMat = AM(nodes)
    print(AdMat)
    print(AdMat[1][2])