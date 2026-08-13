# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Goal is to determine whether there is a cycle in the list
        '''
        - Use the concept of slow and fast pointers
        - set both the slow and fast to head initially
        - while the fast and fast.next exists increment the slow pointer by 1 and the fast pointer by 2
        - if slow == fast -> return True
        - else return false
        '''

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False