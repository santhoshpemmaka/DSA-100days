def removeLoop(head):
    # code here
    # remove the loop without losing any nodes
    if head == None:
        return 0
    else:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return 0
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
