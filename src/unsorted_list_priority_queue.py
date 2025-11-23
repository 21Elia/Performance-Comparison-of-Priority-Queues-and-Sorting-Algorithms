class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class UnsortedLinkedListPQ:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, value):
        newNode = Node(value)
        if self.head == None:
            self.tail = newNode
            self.head = self.tail
        else:
            self.tail.next = newNode
            self.tail = newNode

    def extractMax(self):
        if self.head == None:
            raise IndexError("extractMax from empty queue")
        
        current = self.head
        maxValue = current.value
        maxNode = current
        prev = None
        prevMax = None

        while current != None:
            if current.value > maxValue:
                maxValue = current.value
                maxNode = current
                prevMax = prev
            prev = current
            current = current.next

        # removing the node

        if prevMax == None: # maxNode is head edge-case
            self.head = self.head.next
            if self.head == None:  # list became empty edge-case
                self.tail = None 
        else:
            prevMax.next = maxNode.next # removed last node edge-case
            if maxNode == self.tail:
                self.tail = prevMax

        return maxValue
    
    def extractMin(self):
        if self.head == None:
            raise IndexError("extractMin from empty queue")
        
        current = self.head
        minValue = current.value
        minNode = current
        prev = None
        prevMin = None

        while current != None:
            if current.value < minValue:
                minValue = current.value
                minNode = current
                prevMin = prev
            prev = current
            current = current.next

        # removing the node
        if prevMin == None: # means maxNode is head
            self.head = self.head.next
            if self.head == None:
                self.tail = None
        else:
            prevMin.next = minNode.next
            if minNode == self.tail:
                self.tail = prevMin
        return minValue
    
    def peekMax(self):
        if self.head == None:
            raise IndexError("peekMax from empty queue")
        
        current = self.head
        maxValue = current.value
        while current != None:
            if current.value > maxValue:
                maxValue = current.value
            current = current.next
        return maxValue
    
    def peekMin(self):
        if self.head == None:
            raise IndexError("peekMin from empty queue")
        
        current = self.head
        minValue = current.value
        while current != None:
            if current.value < minValue:
                minValue = current.value
            current = current.next
        return minValue
    
    def isEmpty(self):
        return self.head == None

    def removeAtIndex(self, index):
        if self.head == None:
            raise IndexError("Impossible to remove from empty list.")

        current = self.head
        prev = None
        count = 0

        while current != None and count < index:
            prev = current
            current = current.next
            count += 1
        
        if current == None:
            raise IndexError("Index out of range")
        
        if prev == None:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
        else:
            prev.next = current.next
            if current == self.tail:
                self.tail = prev
        
        return current.value
    
    def clear(self):
        self.head = None
        self.tail = None

    def remove(self, value):
        if self.head == None:
            raise IndexError("Impossible to remove from empty list.")
        
        current = self.head
        prev = None
        while current != None:
            if current.value == value:
                if prev == None: # head edge-case
                    self.head = self.head.next
                    if self.head == None: # list becomes empty edge-case
                        self.tail = None
                else:
                    prev.next = current.next
                    if current == self.tail: # node is the tail edge-case
                        self.tail = prev
                return current.value
            
            prev = current
            current = current.next
        
        raise IndexError("Value" + str(value) + " not found in the list")

