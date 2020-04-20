class Node:
    def __init__(self):
        self.data = None
        self.next = None
    
    def setData(self,data):
        self.data = data
    
    def getData(self):
        return self.data
    
    def setNext(self,next):
        self.next = next
    
    def getNext(self):
        return self.next
    

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    
    def insertAtBeg(node:Node):
        node.setNext(self.head)
        self.head = node
        self.length += 1
    
    def insertAtLast(self,node):
        if self.head == None:
            self.insertAtBeg(node)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next.setNext(node)
            self.length += 1

    
    def addAfterValue(self,node,data):
        if self.length == 0:
            print("List is Empty")
            return None
        else:
            current = self.head
            while current.next is not None or current.data == data:
                if current.data == data:
                    node.setNext(current.next)
                    current.next.setNext(node)
                    self.length += 1
                    return
                else:
                    current = current.next
            print("The Data Provided is not present in list..")
            return None
        
    def addatPos(self,pos,node):
        if pos == 0:
            self.insertAtBeg(node)
        else:
            current = self.head
            previous = self.head
            if pos > self.length or pos < 0:
                print("Invalid Position entered..")
                return None
            count = 0
            while current.next is not None or count < pos:
                count += 1
                if pos == count:
                    previous.next = node
                    node.setNext(current)
                    self.length += 1
                    return
                else:
                    previous = current
                    current = current.next
    def deleteBeg(self):
        if self.length == 0 :
            print("List is Empty")
        else:
            self.head = self.head.getNext()
            self.length -= 1
    
    def deleteLast(self):
        if self.length == 0:
            print("List is Empty..")
            return None
        else:
            current = previous = self.head
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
            self.length -= 1
    
    def deleteValue(self,data):
        if self.head is None or self.length == 0:
            print("List is Empty")
            return None
        current = previous = self.head
        while current.next is not None or current.data == data:
            if current.data == data:
                previous.next = current.next
                self.length -= 1
                return
            
            previous = current
            current = current.next
    
    def deleteAtPos(self,pos):
        if pos > self.length or pos < 0:
            print("The position does not exists")
        elif pos == 1:
            self.deleteBeg()
        else:
            count = 0
            current = self.head
            previous = self.head
            while current.next is not None or count < pos:
                count += 1
                if count == pos:
                    previous.next = current.getNext()
                    self.length -= 1
                    return
                previous = current
                current = current.getNext()

    def getAtPos(self,pos):
        if pos > self.length or pos < 0:
            print("The position does not exists")
            return
        count = 0
        current = self.head
        while current.next is not None or count < pos:
            count += 1
            if count == pos:
            return current.data
            current = current.getNext()
        
    def print_list(self):
        if self.length == 0 or self.head is None:
            return []
        Nodes = []
        current = self.head
        while current.next is not None:
            Nodes.append(current.data)
            current = current.next
        
        return Nodes
                

