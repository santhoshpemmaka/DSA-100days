class Node:
    def __init__(self,data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insertion_beginning(self,element):
        node = Node(element)
        if self.head == None:
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            llist = self.head
            node.next = llist
            node.prev = llist.prev
            llist.prev.next = node
            llist.prev = node
            
    def insertion_ending(self,element):
        node = Node(element)
        if self.head == None:
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            llist = self.head
            while llist.next != self.head:
                llist = llist.next
            node.next = llist.next
            node.prev = llist
            llist.next.prev= node
            llist.next = node
    
    def print_elements(self):
        if self.head == None:
            print("No element")
        else:
            llist = self.head
            while True:
                print(llist.data,end=" ")
                llist = llist.next
                if llist == self.head:
                    break
            print()
            
l1 = Linkedlist()
l1.insertion_beginning(1)
l1.insertion_beginning(2)
l1.insertion_beginning(3)
l1.insertion_beginning(4)
l1.insertion_ending(5)
l1.insertion_ending(6)
l1.print_elements()
