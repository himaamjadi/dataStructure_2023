import array as arr

class Queue:
    def __init__(self) -> None:
        self.__max_size = 10
        self.__rear = -1
        self.__front = -1
        self.__cells = arr.array("i", [0] * self.__max_size)

    def getRear(self) -> int:
        return self.__rear
    
    def getFront(self) -> int:
        return self.__front
    
    def getMax_size(self) -> int:
        return self.__max_size

    def isFull(self) -> bool:
        return self.getRear() - self.getFront() == self.getMax_size()
    
    def isEmpty(self) -> bool:
        return self.getRear() == self.getFront()
    
    def Add(self, item) -> None:
        if self.isFull():
            raise Exception("Queue is full")
        self.__rear = self.getRear() + 1
        self.__cells[self.__rear] = item

    def Delete(self) -> int:
        if self.isEmpty():
            raise Exception("Queue is empty")
        self.__front = self.getFront() + 1
        x = self.__cells[self.getFront()]
        self.__cells[self.getFront()] = 0 
        return x
    
    def show(self) -> str:
        return ",".join([str(items) for items in self.__cells])
    
