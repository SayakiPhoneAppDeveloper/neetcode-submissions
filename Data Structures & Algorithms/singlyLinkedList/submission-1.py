class LinkedList:
    
    def __init__(self):
        self.ll = []
        self.size = 0
    
    def get(self, index: int) -> int:
        if self.size <= index:
            return -1
        return self.ll[index]

    def insertHead(self, val: int) -> None:
        self.size = self.size+1
        new_ll = [0]*self.size
        new_ll[0] = val
        for i in range(1, self.size):
            new_ll[i] = self.ll[i-1]
        self.ll = new_ll

    def insertTail(self, val: int) -> None:
        self.size = self.size + 1
        new_ll = [0]*self.size
        new_ll[self.size-1] = val
        for i in range(self.size-1):
            new_ll[i] = self.ll[i]
        self.ll = new_ll

    def remove(self, index: int) -> bool:
        if self.size <= index:
            return False
        self.size = self.size-1
        new_ll = [0]*self.size
        for i in range(self.size):
            if i<index :
                new_ll[i]=self.ll[i]
            elif i>=index:
                new_ll[i] = self.ll[i+1]
            
        self.ll = new_ll

        return True

    def getValues(self) -> List[int]:
        return self.ll
