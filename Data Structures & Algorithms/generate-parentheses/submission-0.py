class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        - set res
        - set backtrack with params path,open,close
        - if len(path)== 2*n -> re.append("".join(path))
        - case 1:if open < n ->
        - path.append("("), backtrack(path,open+1,close), path.pop()
        - case 2:if close < open ->
        - path.append(")"), backtrack(path,open,close+1), path.pop()
        - backtrack([],0,0)
        - return res
        '''

        res = []
        def backtrack(path,open,close):
            if len(path) == 2*n:
                res.append("".join(path))

            if open < n:
                path.append("(")
                backtrack(path,open+1,close)
                path.pop()

            if close < open:
                path.append(")")
                backtrack(path,open,close+1)
                path.pop()

        backtrack([],0,0)
        return res