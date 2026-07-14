# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        #create the n+1 gap between slow and fast
        for i in range(n+1):
            fast = fast.next

        #Maintain the Gap
        while fast:
            fast = fast.next
            slow = slow.next
        
        #delete the target node
        slow.next = slow.next.next

        return dummy.next