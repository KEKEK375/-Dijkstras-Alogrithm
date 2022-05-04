import random as r

class Node:
    ID = 0
    def __init__(self):
        self.id = Node.ID
        Node.ID += 1
        self._CHECKED = False

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
                    if item == -1 and r.random() < 5 / self.size:    
                        num = r.randint(1, 99)
                        self._AM[index][iIndex] = num
                        self._AM[iIndex][index] = num
    
    def __repr__(self) -> str: #Called by print()
        OutputStr = " " * (len(str(self.size)) + 1)
        for i in range(0,self.size):
            OutputStr += " " * (len(str(self.size)) - len(str(i)) + 1) + str(i)
        OutputStr += "\n\n"
        tempI = 0
        for row in self._AM:
            aRow = str(tempI) + " " * (len(str(self.size)) - len(str(tempI)) + 1)
            tempI += 1
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
    for i in range(60):
        nodes.append(Node())
    AM = AdjacencyMatrix(nodes)
    print(AM)