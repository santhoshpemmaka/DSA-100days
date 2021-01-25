class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insertionbegin(self,element):
        if self.head == None:
            node = Node(element)
            self.head = node
        else:
            node = Node(element,self.head)
            self.head= node
            
    def insertionend(self,element):
        if self.head == None:
            node = Node(element)
            self.head = node
        else:
            llist = self.head
            while llist.next != None:
                llist = llist.next
            node = Node(element)
            llist.next = node
            
    def deletefirstnode(self):
        if self.head == None:
            print("No element")
        self.head = self.head.next
        
    def deletelastnode(self):
        if self.head == None:
            print("No element")
        llist = self.head
        while llist.next.next != None:
            llist = llist.next
        llist.next = None
        
    def insertiongivenposition(self,element,position):
        if position == 0:
            node = Node(element,self.head)
            self.head = node
        if self.head == None:
            print("No element")
        count = 1
        llist = self.head
        while llist:
            count = count+1
            if count == position:
                node = Node(element,llist.next)
                llist.next = node
            
            llist = llist.next
        return self.head
        
    
    def printelements(self):
        if self.head == None:
            print("No element")
        llist = self.head
        while llist:
            print(llist.data,end=" ")
            llist = llist.next
            
l1 = Linkedlist()
l1.insertionbegin(1)
l1.insertionbegin(2)
l1.insertionend(3)
l1.insertionend(4)
l1.deletefirstnode()
l1.deletelastnode()
l1.insertiongivenposition(2,2)
l1.insertiongivenposition(0,0)
l1.insertiongivenposition(5,6)
l1.printelements()
