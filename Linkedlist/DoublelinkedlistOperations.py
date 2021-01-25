class Node:
    def __init__(self,data = None,prev = None,next = None):
        self.data = data
        self.prev = prev
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insertion_elements(self,data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            llist = self.head
            node = Node(data)
            while llist.next:
                llist = llist.next
            llist.next = node
            node.prev = llist
    
    def insertionelement_begin(self,data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data,None,self.head)
            self.head.prev = node
            self.head = node
            
    def reverselinkedlist(self):
        if self.head == None:
            print("No element")
        llist = self.head
        while llist.next:
            llist = llist.next
        while llist:
            print(llist.data,end=" ")
            llist = llist.prev
        print()   
    
    def deletedfirstelement(self):
        if self.head == None:
            print("No element")
        else:
            self.head = self.head.next
            self.head.prev = None
            
    def deletedlastelement(self):
        if self.head == None:
            print("No element")
        else:
            llist = self.head
            while llist.next.next:
                llist = llist.next
            llist.next = None
            # llist.prev = None
            
    def deleteparticular_element(self,element):
        if self.head.data == element:
            self.head = self.head.next
            self.head.prev = None
        llist = self.head
        while llist:
            if llist.data == element:
                llist.prev.next = llist.next
                llist.next.prev = llist.prev
            llist = llist.next
                
        
    def printelementslist(self):
        if self.head == None:
            print("No element")
        else:
            llist = self.head
            while llist:
                print(llist.data,end=" ")
                llist = llist.next
            print()
                
l1 = Linkedlist()
l1.insertion_elements(1)
l1.insertion_elements(2)
l1.insertion_elements(3)
l1.insertion_elements(4)
l1.insertionelement_begin(0)
l1.insertionelement_begin(-1)


l1.printelementslist()
l1.deletedfirstelement()
l1.deletedlastelement()
l1.reverselinkedlist()
l1.deleteparticular_element(0)
l1.printelementslist()
l1.reverselinkedlist()
