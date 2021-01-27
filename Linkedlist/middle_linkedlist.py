def middle_linkedlist(self):
        method 1
        if self.head == None:
            print("No element")
        else:
            llist = self.head
            count = 0
            while llist:
                count = count+1
                llist = llist.next
            llist1 = self.head
            for i in range(count//2):
                llist1 = llist1.next
            return llist1.data
        
        # method2
        if self.head == None:
            print("No element")
        else:
            slow = self.head
            fast = self.head
            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
            return slow.data
            
