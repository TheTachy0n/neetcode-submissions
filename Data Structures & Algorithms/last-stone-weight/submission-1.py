class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        - convert all elements to -ve
        - heapify them
        - in a while loop pop the 1st and 2nd largest element
        - if the 1st != 2nd -> push the -difference into stones
        - return the - of the 0th element of stones if stones has any element left, else 0
        '''
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, -(first - second))
        return -stones[0] if stones else 0