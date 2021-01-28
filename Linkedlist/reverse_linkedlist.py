def reverselinked_list(self):
        if self.head == None:
            return 
        else:
            prev = None
            curr = self.head
            while curr:
                llist1 = curr.next
                curr.next = prev
                prev = curr
                curr = llist1
                
            return prev
