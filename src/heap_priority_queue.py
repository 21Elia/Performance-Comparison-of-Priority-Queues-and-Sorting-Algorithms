class MaxHeap:
    def __init__(self):
        self.data = []
        self.heapSize = len(self.data)

    def maxHeapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        if left < self.heapSize and self.data[left] > self.data[i]:
            max = left
        else:
            max = i
        if right < self.heapSize and self.data[right] > self.data[max]:
            max = right
        if max != i:
            tmp = self.data[max]
            self.data[max] = self.data[i]
            self.data[i] = tmp
            self.maxHeapify(max)

    def buildMaxHeap(self):
        self.heapSize = len(self.data)
        for i in range(self.heapSize//2 - 1, -1, -1):
            self.maxHeapify(i)

    def peekMax(self):
        return self.data[0]

    def extractMax(self):
        if self.heapSize < 1:
            raise IndexError("Error: heap underflow")
    
        max = self.data[0]
        self.data[0] = self.data[self.heapSize - 1]
        self.heapSize -= 1
        self.data.pop()
        self.maxHeapify(0)
        return max
    
    def getSize(self):
        return self.heapSize
    
    def increaseKey(self, i, value):
        if value < self.data[i]:
            raise ValueError("Error: new key < current key")
        
        self.data[i] = value
        while i > 0 and self.data[(i-1)//2] < self.data[i]:
            tmp = self.data[i]
            self.data[i] = self.data[(i-1)//2]
            self.data[(i-1)//2] = tmp
            i = (i-1)//2
    
    def insert(self, value):
        self.heapSize += 1
        self.data.append(float("-inf"))
        self.increaseKey(self.heapSize - 1, value)
    
    def removeAtIndex(self, i):
        if i < 0 or i >= self.heapSize:
            raise IndexError("index out of range")
        
        removedValue = self.data[i]
        lastValue = self.data[self.heapSize-1]
        self.data[i] = lastValue
        self.heapSize -= 1
        self.data.pop()
        self.maxHeapify(i)
        return removedValue
    
    def clear(self):
        self.data.clear()
        self.heapSize = 0

    def isEmpty(self):
        return self.heapSize == 0
    
    def remove(self, value):

        index = -1
        for i in range(self.heapSize):
            if(self.data[i] == value):
                index = i
                break
        
        if index < 0:
            raise ValueError("Value not found in heap")

        lastValue = self.data[self.heapSize - 1]
        self.data[index] = lastValue

        self.heapSize -= 1
        self.data.pop()

        self.maxHeapify(index)