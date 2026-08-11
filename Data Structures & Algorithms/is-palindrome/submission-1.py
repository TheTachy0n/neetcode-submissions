class Solution:
    def isPalindrome(self, s: str) -> bool:
        #input is a string, output is a boolean values
        '''
        1) Brute Force
        We could apply the brute force method could be reversing the string and comparing it to the normal string
        - we have to make sure to convert all the chars to lower case before comaprison 
        '''
        '''
        new = ''
        for i in s:
            if i.isalnum():
                new += i.lower()
        return new == new[::-1]
        '''
        '''
        2) 2 pointer approach
        - O(n) complexity
        - set l and r pointers on either side of the string
        - if the char is not alnum either increment or decrement l/r respectively
        - compare the s[l] and s[r] as lower case characters
        '''
        l = 0
        r = len(s) - 1
        while l<r:
            while l<r and not s[l].isalnum(): #edge cases
                l += 1

            while l<r and not s[r].isalnum(): #edge cases
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        
        return True