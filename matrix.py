import random as r

class Node:
    ID = 0
    def __init__(self):
        self.id = Node.ID
        Node.ID += 1

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
    
    def __repr__(self) -> str:
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

    def __getitem__(self, index: int) -> list[int]:
        return self._AM[index]
    
    def __iter__(self):
        for i in self._AM:
            for j in i:
                yield j



if __name__ == "__main__":
    nodes = []
    for i in range(6):
        nodes.append(Node())
    AM = AdjacencyMatrix(nodes)
    print(AM)