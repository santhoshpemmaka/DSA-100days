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
        llist1 = self.head

        
            
            
    def print_elements(self):
        if self.head == None:
            print("No element in the circular linked list")
        else:
            llist = self.head
            while True:
                print(llist.data,end=" ")
                llist = llist.next
                if llist.next == self.head:
                    print(llist.data)
                    break
            print()

l1 = Linkedlist()
l1.append_elements(1)
l1.print_elements()
l1.append_elements(2)
l1.print_elements()
l1.append_elements(3)
l1.print_elements()
l1.append_elements(4)
l1.print_elements()
