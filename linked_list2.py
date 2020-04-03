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
    
    def insertAtBeginning(self,node):
        node.next = self.head
        self.head = node
        self.length += 1
    
    def insertAtEnd(self,node):
        currentnode = self.head

        while currentnode.next != None:
            currentnode = currentnode.next
        
        currentnode.next = node
        self.length += 1
    
    def insertAtPos(self,node,pos):
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print("position does not exists..")
        else:
            while currentnode.next != None or count < pos:
                count += 1
                if pos == count:
                    previousnode.next = node
                    node.next = currentnode
                    self.length += 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

    def print_list(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next 
             
        print(nodeList)
    
    def insertAfterValue(self,data,node):
        if self.length == 0:
            print("List is Empty..")
        else:
            currentnode = self.head
            while currentnode.next != None or currentnode.data == data:
                if currentnode.data == data:
                    node.next = currentnode.next
                    currentnode.next = node
                    self.length += 1
                    return
                else:
                    currentnode = currentnode.next
            print("The data provided in not present")
    
    def deleteAtBeginning(self):
        if self.length == 0:
            print("List is Empty..")
        else:
            self.head = self.head.next
            self.length -= 1
            return
    
    def deleteAtEnd(self):
        if self.length == 0:
            print("List is Empty..")
        else:
            currentnode = self.head
            previousnode = self.head
            while currentnode.next != None:
                previousnode = currentnode
                currentnode = currentnode.next
            
            previousnode.next = None
    
    def deleteAtPos(self,pos):
        count = 0
        currentnode = self.head
        previousnode  = self.head

        if pos < self.length or pos < 0:
            print("Position does not exists..")
        else:
            while currentnode.next != None or count < pos:
                count += 1
                if pos == count:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next


    def deleteValue(self,data):
        currentnode = self.head
        previousnode = self.head
        while currentnode.next != None or currentnode.data == data:
            if currentnode.data == data:
                previousnode.next = currentnode.next
                self.length -= 1
                return
            else:
                previousnode = currentnode
                currentnode = currentnode.next
        print("Data with value {} not found".format(data))

            


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
l1.insertAtBeginning(node1)
l1.print_list()
l1.insertAtEnd(node2)
l1.print_list()
l1.insertAtPos(node3,2)
l1.print_list()
l1.insertAtEnd(node6)
l1.print_list()
l1.insertAfterValue(6,node5)
l1.print_list()
