class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        - base condition if not digit -> return []
        - set a dict of each number and the letter it is mapped to
        - set res
        - backtrack with i and path
        - if i == len(digits) -> res.append(path.copy())
        - for letter in the phone dict
        - path.append(letter)
        - backtrack(i+1,path)
        - path.pop()
        - backtrack(0,[])
        - return res
        '''

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(i, path):
            # We've chosen one letter for every digit
            if i == len(digits):
                res.append("".join(path))
                return

            # Try every letter corresponding to digits[i]
            for letter in phone[digits[i]]:
                path.append(letter)

                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])

        return res