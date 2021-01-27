def nthnodefrom_linkedlist(self,num):
        method 1
        if self.head == None:
            print("No element")
        else:
            count = 0
            llist = self.head
            while llist:
                count = count+1
                llist = llist.next
            if count < num:
                return None
            llist = self.head
            for i in range(0,count-num):
                llist = llist.next
            return llist.data
        # method2:
        if self.head == None:
            return None
        else:
            first = self.head
            for i in range(0,num):
                first = first.next
            second = self.head
            while first:
                first = first.next
                second = second.next
            return second.data
                
