class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        - set res
        - backtrack with start and path
        - if start == len(s) -> append a copy of path to res
        - for end from start till len(s)
        - substring = [start,end+1]
        - if substring == [::-1]
        - append(substring) to path
        - backtrack with end+1
        - pop path
        - backtrack with 0,[]
        - return res
        '''
        res = []

        def backtrack(start,path):
            if start == len(s):
                res.append(path.copy())
                return
            
            for end in range(start,len(s)):
                substring = s[start:end+1]

                if substring == substring[::-1]:
                    path.append(substring)

                    backtrack(end + 1, path)

                    path.pop()

        backtrack(0,[])

        return res