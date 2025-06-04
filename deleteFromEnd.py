def removeNthFromEnd(head, n):
    slow, fast = head, head

    for _ in range(n):
        fast = fast.next
    
    if fast is None:
        return head.next
    
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    
    return head

"""
LeetCode Problem: 19 "Delete nth node from the end" 

- use two pointers, fast and slow, to traverse the linked list. 
- the fast pointer is moved n steps ahead
- then both pointers are moved together until fast reaches the end
- now, slow will be just before the node to be deleted
- we can delete the node
"""