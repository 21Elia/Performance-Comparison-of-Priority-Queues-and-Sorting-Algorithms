class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SortedLinkedListPQ: # (descending order => max priority)
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        newNode = Node(value)
        current = self.head
        prev = None
        while current != None and value < current.value:
            prev = current
            current = current.next
        
        if prev == None: # head-insert edge case
            newNode.next = self.head
            self.head = newNode
        else: # middle/end-insert case
            newNode.next = current
            prev.next = newNode
    
    def extractMax(self):
        if self.head == None:
            raise IndexError("extractMax from empty queue")

        maxNode = self.head
        self.head = self.head.next
        return maxNode.value
        

    def extractMin(self):
        if self.head == None:
            raise IndexError("extractMin from empty queue")
        
        current = self.head
        prev = None
        while current.next != None:
            prev = current
            current = current.next
        
        if prev == None:
            self.head = None
        else:
            prev.next = None
        
        return current.value
        
    
    def peekMax(self):
        if self.head == None:
            raise IndexError("peekMax from empty queue")
        
        return self.head.value

    def peekMin(self):
        if self.head == None:
            raise IndexError("peekMin from empty queue")

        current = self.head
        while current.next != None:
            current = current.next
        
        return current.value
    
    def isEmpty(self):
        return self.head == None
    
    def removeAtIndex(self, i):
        if self.head == None:
            raise IndexError("Impossible to remove from empty list.")

        current = self.head
        prev = None
        count = 0

        while current != None and count < i:
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

    def remove(self, value):
        if self.head == None:
            raise IndexError("Impossible to remove from empty list.")
        
        current = self.head
        prev = None
        
        while current != None:
            if current.value == value:
                if prev == None:  # head edge-case
                    self.head = self.head.next
                else:
                    prev.next = current.next
                return current.value

            prev = current
            current = current.next
        
        raise ValueError(f"Value {value} not found in the list.")