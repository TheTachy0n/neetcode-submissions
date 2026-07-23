import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = x*x + y*y
            heapq.heappush(heap,(dist,x,y))
        
        res = []

        while k:
            _,x,y = heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res