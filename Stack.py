import numpy

class Stack:
    def __init__ (self):
        self.__size = 10
        self.__top = - 1
        self.__items = numpy.zeros(self.__size)

    def getTop(self) -> int:
        return self.__top

    def isEmpty(self) -> bool:
        return self.getTop() == -1

    def isFull(self) -> bool:
        return self.getTop() == self.__size - 1
    
    def push(self,x):
        if self.isFull():
            raise Exception("Stack is full")
        self.__top = self.getTop() + 1
        self.__items[self.getTop()] = x

    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        
        x = self.__items[self.getTop()]
        self.__items[self.getTop()] = 0
        self.__top = self.getTop() - 1
        return x
    
    def show(self):
        print(self.__items)