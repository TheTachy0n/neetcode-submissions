class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        - sort the candidates
        - store res in an array
        - define the backtrack function  with params start, path and total
        - if total == target -> append to res
        - if total > target -> return
        - for i in range from start to len(candidates)
        - skip duplicates at the same level -> if condition -> if [i] == [i-1] -> continue
        - since its already sorted -> break if total+candidates[i] > target
        - append it to path
        - now backtrack with i+1
        - and finally pop from the path
        - outside the definition -> backtrack(0,[],0)
        - return res
        '''
        candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                #skip duplicates at the same level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                #since the list is already sorted, nothing will work after a specific combination
                if total + candidates[i] > target:
                    break
                path.append(candidates[i])
                #i+1 cause each number can only be used once
                backtrack(i+1,path,total+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return res
            