import random as r

class Node:
    ID = 0
    def __init__(self):
        self.id = Node.ID
        Node.ID += 1
        self._PATH = []
        self._PATHLENGTH = -1
        self._NODELISTPATH = []
        self._CHECKED = False

    def UpdatePath(self, NodeList: list[tuple["Node", int]]):
        """Takes in a List containing a tuple in the form (Node, weight)"""
        self._PATH = NodeList
        self._NODELISTPATH = []
        self._PATHLENGTH = 0
        for node, weight in NodeList:
            self._PATHLENGTH += weight
            self._NODELISTPATH.append(node)
    
    def GetCurrentFastestPath(self) -> list[tuple["Node", int]]:
        "Return a list containing the path in the form [(Node, Weight), ..., ...]"
        return self._PATH.copy()
    
    def GetCurrentPathLength(self) -> int:
        "Return the total path length"
        return self._PATHLENGTH
    
    def GetCurrentNodePath(self) -> list["Node"]:
        "Return the nodes (in order) of the path"
        return self._NODELISTPATH.copy()

    def SetChecked(self, checked: bool):
        self._CHECKED = checked
    
    def GetChecked(self) -> bool:
        return self._CHECKED

    def __repr__(self) -> str: #Called by print()
        return str(self.id) # Changed this to get rid of the 'Node: ' part as it messed with just getting the id - KEKEK

class AdjacencyMatrix:

    def __init__(self, nodes: list[Node]):
        self.size = len(nodes)
        self._AM = []
        for i in range(self.size):
            self._AM.append([-1]*self.size)
        for index, tempList in enumerate(self._AM):
            for iIndex, item in enumerate(tempList):
                if index == iIndex:
                    self._AM[index][iIndex] = 0
                else:
                    if item == -1 and r.random() > 0.5:    
                        num = r.randint(1, 20)
                        self._AM[index][iIndex] = num
                        self._AM[iIndex][index] = num
    
    def __repr__(self) -> str: #Called by print()
        OutputStr = ""
        for row in self._AM:
            aRow = ""
            for item in row:
                item = str(item)
                if len(item) == 1:
                    aRow += " "
                aRow += " " + item
            OutputStr += aRow + "\n"
        return OutputStr

    def __getitem__(self, index: int) -> list[int]: #Called by AM[index]
        return self._AM[index]
    
    def __iter__(self): #Called by for i in AM:
        for i in self._AM:
            for j in i:
                yield j



if __name__ == "__main__":
    nodes = []
    for i in range(6):
        nodes.append(Node())
    AM = AdjacencyMatrix(nodes)
    print(AM)