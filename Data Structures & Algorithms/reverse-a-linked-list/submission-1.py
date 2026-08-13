# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Goal is to reverse a linked list
        '''
        - set the previous to none and the current to head
        - 4 main operations
        - set next_node = curr.next
        - curr.next = prev
        - prev = curr
        - curr = next_node
        '''
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
