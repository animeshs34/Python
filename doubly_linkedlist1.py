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
    
    def insertBeg(self,data):
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            self.head.prev = Node(data,self.head,None)
            self.head = Node
    
    def insertEnd(self,data):
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            self.tail.set_next(Node(data,None,self.tail))
            self.tail = self.tail.next
    

if __name__ == '__main__':
    # Initializing list
    l = DoubleLinkedList()

    # Inserting Values
    l.insertBeg(1)
    l.fwd_print()
    l.insertEnd(2)
    l.fwd_print()
    l.insertBeg(3)
    l.fwd_print()
    l.insertEnd(4)
    # Forward Print
    l.fwd_print()
        