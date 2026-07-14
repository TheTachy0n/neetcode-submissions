"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}

        # Pass 1: Create all copied nodes
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: Connect next and random pointers
        curr = head
        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next]
            copy.random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]