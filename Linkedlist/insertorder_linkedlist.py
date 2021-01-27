def insert_order(self,element):
        node = Node(element)
        if self.head == None:
            self.head = node
        else:
            llist = self.head
            if llist.data > element:
                node.next = self.head.next
                self.head = node
            while llist.next:
                if llist.next.data > element:
                    node.next = llist.next
                    llist.next = node
                    break
                llist = llist.next

            else:
                llist.next = node
