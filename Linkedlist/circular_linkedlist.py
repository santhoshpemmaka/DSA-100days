class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def append_elements(self,element):
        node = Node(element)
        if self.head == None:
            self.head = node
            node.next = self.head
        else:
            llist = self.head
            while llist.next != self.head:
                llist = llist.next
            llist.next = node
            node.next = self.head
            

    
    def insertion_beginning(self,element):
        node = Node(element)
        if self.head == None:
            self.head = node
            node.next = self.head
        else:
            node.next = self.head.next
            self.head.next = node
            self.head.data,node.data = node.data,self.head.data
          
    def deleted_headnode(self):
        if self.head == None:
            print("No element in the list")
        elif self.head.next == self.head:
            self.head = None
        else:
            llist = self.head
            llist.data = llist.next.data
            llist.next = llist.next.next
            
    def deleted_kthnode(self,k):
        if self.head == None:
            print("No element")
        if self.head.next == self.head:
            self.head = None
        if k == 1:
            llist = self.head
            llist.data = llist.next.data
            llist.next = llist.next.next
        else:
            count = 1
            llist = self.head
            while llist.next != self.head:
                count = count+1
                if k == count:
                    llist.next = llist.next.next
                llist = llist.next
                    
    def print_elements(self):
        if self.head == None:
            print("No element in the circular linked list")
        else:
            llist = self.head
            while llist:
                print(llist.data,end=" ")
                llist = llist.next
                if llist == self.head:
                    break
                
            print()

l1 = Linkedlist()

l1.append_elements(1)
l1.append_elements(2)
l1.append_elements(3)
l1.append_elements(4)
l1.print_elements()
l1.insertion_beginning(0)
l1.insertion_beginning(-1)
l1.insertion_beginning(-2)
l1.deleted_headnode()
l1.deleted_headnode()
l1.print_elements()
l1.deleted_kthnode(5)
l1.print_elements()
