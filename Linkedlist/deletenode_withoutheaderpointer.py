def deleteNode(curr_node):
    #code here
    curr_node.data = curr_node.next.data
    curr_node.next = curr_node.next.next
    
