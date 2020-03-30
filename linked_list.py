class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def setData(self,data):
        self.data = data 
    def getData(self):
        return self.data
    def setNext(self,next):
        self. next = next
    def getNext(self): 
        return self.next
    def hasNext(self): 
        return self.next != None 
    
class LinkedList(object):
    def __init__(self):
        self.lenght = 0
        self.head = None
    
    def addNode(self,node):
        if self.lenght == 0:
            self.addBeg(node)
        else:
            self.addLast(node)

    def addBeg(self,node):
        newNode = node
        newNode.next = self.head
        self.head = newNode
        self.lenght += 1

    def addAfterValue(self,data,node):
        newNode = node
        currentNode = self.head

        while currentNode.next != None or currentNode.data != data:
            if currentNode.data == data:
                newNode.next = currentNode.next
                currentNode.next = newNode
                self.lenght += 1
                return
            else:
                currentNode = currentNode.next