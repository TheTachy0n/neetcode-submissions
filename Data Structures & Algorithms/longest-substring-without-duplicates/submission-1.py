class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Brute Force Approach
        - set a res
        - 2 nested for loops
        - inside the 1st one set a charSet
        - inside the 2nd one if a letter already exists in charset -> break
        - else add it to charset
        - result = max(res, and len(charset))
        '''
        '''
        res = 0
        for i in range(len(s)):
            char_set = set()
            for j in range(i+1, len(s)):
                if s[j] in char_set:
                    break
                char_set.add(s[j])
            res = max(res, len(char_set))

        return res
        '''
        '''
        2. Sliding Window
        - set a char_set, left = 0 and max_length =0
        - for loop with the right as the pointer
        - while s[right] is in the char_set -> remove the left most element and perform left + 1
        - add the right most element to the char_set
        - max_length is the max of itself and right-left+1
        '''
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length,(right-left+1))
        return max_length
