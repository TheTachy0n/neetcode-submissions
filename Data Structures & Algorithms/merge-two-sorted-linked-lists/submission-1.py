# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        - Create a Dummy node and set the tail pointer to dummy
        - Compare the 2 given lists in a while loop
        - if l1<l2 -> add it to tail next and move to the next value in l1
        - else -> vice verse
        - then move the tail pointer to the next value within the loop
        - now outside the loop -> attach whatever remains to the tail whether its l1 or l2
        - and return dummy.next
        '''
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if (list1.val < list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next
