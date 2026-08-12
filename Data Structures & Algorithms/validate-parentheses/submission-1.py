class Solution:
    def isValid(self, s: str) -> bool:
        #Goal- To check whether all the brackets are closed correctly
        '''
        1. Brute Force Approach
        - within a while loop essentially remove each layer of parenthesis from the string
        - compare s to an empty string
        - O(n^2) time complexity
        '''
        '''
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()','')
            s = s.replace('{}','')
            s = s.replace('[]','')
        return s == ''
        '''
        '''
        2. Stacks
        - create an empty stack
        - create a dictionary with all close & open bracket key value pairs
        - for each character in s, if it is am open bracket -> append it to the stack
        - else if not stack or stack[-1] is not in the pairs -> return False
        - pop from the stack
        - compare the length of the stack to 0 and return
        '''
        stack = []

        pairs = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return len(stack) == 0

