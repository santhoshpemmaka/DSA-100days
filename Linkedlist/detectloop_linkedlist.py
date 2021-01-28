def detectlooplist(self):
        # method 1 will be modified the node structure
        if self.head == None:
            print("No element")
        else:
            llist = self.head
            while llist:
                if llist.visted != 0:
                    return "No"
                else:
                    llist = llist.next
                    llist.visted = 1
            return "Yes"
            
        # method 2 will using hashing set
        
        if self.head == None:
            print("No element")
        else:
            l = set()
            llist = self.head
            while llist:
                if llist in l:
                    return True
                l.add(llist)
                llist = llist.next
            return False

        # method 3 will using two pointers
        
        if self.head == None:
            print("No element")
        else:
            slow_pointer = self.head
            fast_pointer = self.head
            while fast_pointer and fast_pointer.next:
                slow_pointer = slow_poniter.next
                fast_pointer = fast_pointer.next.next
                
                if slow_pointer == fast_pointer:
                    return True
        return False
