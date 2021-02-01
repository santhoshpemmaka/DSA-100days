def countNodesinLoop(head):
    #Your code here
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return 0
    count = 1
    slow = slow.next
    while slow != fast:
        count = count + 1
        slow = slow.next
    return count
