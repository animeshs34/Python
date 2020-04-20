class Node:
    # Constructor to initialize data
    # If data is not given by user,its taken as None 
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    # method for setting the data field of the node    
    def set_data(self, data):
        self.data = data
    # method for getting the data field of the node   
    def get_data(self):
        return self.data
    # method for setting the next field of the node
    def set_next(self, next):
        self.next = next
    # method for getting the next field of the node    
    def get_next(self):
        return self.next
    # returns true if the node points to another node
    def has_next(self):
            return self.next != None
    # method for setting the next field of the node
    def setPrev(self, prev):
        self.prev = prev
       # method for getting the next field of the node    
    def getPrev(self):
        return self.prev
    # returns true if the node points to another node
    def hasPrev(self):
            return self.prev != None	    
    # __str__ returns string equivalent of Object
    def __str__(self):
        return "Node[Data = %s]" % (self.data,)


    


class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def fwd_print(self):
        current = self.head
        if current == None:
            print("No elements")
            return False
        while (current != None):
            print (current.data) 
            current = current.next
        return True

    def insert(self,data):
        if self.head is None:
            self.head = self.tail = Node(data)
            return True
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data,None,current)
        self.tail = current.next

    def delete(self,data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return True
        
        if self.head is None:
            print("List is Empty...")
        
        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return True

        current = self.head
        while current is not None:
            if current.data == data:
                current.prev.set_next(current.next)
                current.next.setPrev(current.prev)
                return True
            current = current.next
        return False

    
    def insertAtBeginning(self,data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.head = Node(data,self.head,None)
    
    def getNode(self,index):
        current = self.head

        if current == None:
            return None
        i = 0
        while current.next is not None and i < index:
            current = current.next
            if current == None:
                 break
            i += 1
        return current
    

    def insertAtGivenPosition(self,index,data):
        if self.head == None or index == 0:
            self.insertAtBeginning(data)
        else index > 0:
        temp = self.getNode(index)
        if temp == None or temp.get_next() == None:
            self.insert(data)
        else:
            newNode = Node(data,temp.get_next(),temp)
            temp.get_next().setPrev(newNode)
            temp.set_next(newNode)
        
    

        


if __name__ == '__main__':
    # Initializing list
    l = DoubleLinkedList()

    # Inserting Values
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insertAtBeginning(45)
    print("animesh ",l.getNode(0))

    l.fwd_print()

        
