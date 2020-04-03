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

    def insertAtBeg(self,node: Node) -> bool:
        if self.head == None:
            self.head = node
            self.length += 1
            return True
        else:
            node.next = self.head
            self.head = node
            self.length += 1
            return True
        return False
    
    def insertAtEnd(self,node:Node) -> bool:
        if self.head is None:
            self.head = node
            self.length += 1
            return True
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            node.next = None
            self.length += 1
            return True
        return False
    
    def insertAfterValue(self,data,node):
        if self.length == 0:
            print("List is Empty")
            return False
        else:
            current = self.head
            while current.next != None or current.data == data:
                if current.data == data:
                    node.next = current.next
                    current.next = node
                    self.length += 1
                    return True
                else:
                    current = current.next
            print("Value not Found..")
            return True
    
    def insertAtPos(self,node: None,pos: int) -> bool:
        if self.length == 0:
            print("List is Empty")
            return False
        else:
            
            if pos == 0:
                return self.insertAtBeg(node) 
            elif pos > self.length or pos < 0:
                print("Invalid Position..")
                return True
            else:
                count = 0
                current = self.head
                previous = self.head
                while current.next != None or count < pos:
                    count += 1
                    if count == pos:
                        previous.next = node
                        node.next = current
                        self.length += 1
                        return True
                    else:
                        previous = current
                        current = current.next
        return False
    

    def deleteAtBeg(self):
        if self.length == 0:
            print("List is Empty")
            return False
        else:
            self.head = self.head.next
            self.length -= 1
            return True
    
    def deleteAtEnd(self):
        if self.length == 0:
            print("List is Empty")
            return False
        else:
            current = self.head
            previous = self.head
            while current.next != None:
                previous = current
                current = current.next
            previous.next = None
            self.length -= 1
            return True
        
        return False
    
    def deleteValue(self,value):
        if self.length == 0:
            print("List is Empty")
            return False
        else:
            current = self.head
            previous = self.head
            while current.next != None or current.data == value:
                if current.data == value:
                    previous.next = current.next
                    self.length -= 1
                    return True
                else:
                    previous = current
                    current = current.next
            print("Value not Found")
            return True

        return False


    def deleteAtPos(self,pos):
        if self.length == 0:
            print("List is Empty..")
            return False
        else:
            if pos == 0:
                return self.deleteAtBeg()
            elif pos > self.length or pos < 0:
                print("Invalid position..")
            else:
                count = 0
                current = self.head
                previous = self.head
                while current.next != None and count < pos:
                    count += 1
                    if count == pos:
                        previous.next = current.next
                        self.length -= 1
                        return True
                    else:
                        previous = current
                        current = current.next
                return False

    def print_list(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next 
             
        print(nodeList)
    

node1 = Node()
node1.setData(1)
node2 = Node()
node2.setData(2)
node3 = Node()
node3.setData(3)
node4 = Node()
node4.setData(4)
node5 = Node()
node5.setData(5)
node6 = Node()
node6.setData(6)


l1 = LinkedList()
l1.insertAtBeg(node1)
l1.print_list()
l1.insertAtEnd(node2)
l1.print_list()
l1.insertAtPos(node3,2)
l1.print_list()
l1.insertAtEnd(node6)
l1.print_list()
l1.insertAfterValue(6,node5)
l1.print_list()
