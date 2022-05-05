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

    def __init__(self, size: int):
        self.size = size
        self._NODES = []
        for i in range(size):
            self._NODES.append(Node())
        self._AM = []
        for i in range(1, self.size+1):
            self._AM.append([-1]*i)
        for index, tempList in enumerate(self._AM):
            for iIndex, item in enumerate(tempList):
                if index == iIndex:
                    self._AM[index][iIndex] = 0
                else:
                    if item == -1 and r.random() < 5 / self.size:    
                        num = r.randint(1, 99)
                        try:
                            self._AM[index][iIndex] = num #If that index doesnt exist, just flips the indexes
                        except:
                            self._AM[iIndex][index] = num
    
    def GetNodes(self) -> list[Node]:
        return self._NODES.copy()
    
    def __repr__(self) -> str: #Called by print()
        digits = len(str(self.size))
        OutputStr = ""
        tempI = 0
        for row in self._AM:
            aRow = str(tempI) + " " * (digits - len(str(tempI)) + 1)
            tempI += 1
            for item in row:
                item = str(item)
                if len(item) == 1:
                    aRow += " "
                aRow += " " + item
            OutputStr += aRow + "\n"
        OutputStr += "\n"
        OutputStr += " " * (digits+1)
        for i in range(self.size):
            OutputStr += " " * (digits - len(str(i)) + 1) + str(i)
        return OutputStr

    def __getitem__(self, index: int) -> list[int]: #Called by AM[index]
        return self._AM[index]
    
    def __iter__(self): #Called by for i in AM:
        for i in self._AM:
            for j in i:
                yield j



if __name__ == "__main__":
    AM = AdjacencyMatrix(60)
    print(AM)