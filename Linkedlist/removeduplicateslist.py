def removeduplicateslist(self):
        if self.head == None:
            print("No element")
        else:
            llist = self.head
            while llist and llist.next:
                if llist.data == llist.next.data:
                    llist.next = llist.next.next
                else:
                    llist = llist.next
