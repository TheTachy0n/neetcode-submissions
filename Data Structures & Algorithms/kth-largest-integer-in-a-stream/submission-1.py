import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        '''
        - initialize k and nums as a head
        - make it into a heap
        - while lenngth of heap > k:
        - pop the min element of the head
        '''
        self.k = k
        self.heap = nums

        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        '''
        - push the value into the head
        - if the heap value exceeds k -> pop the lowest value
        - return self.heap[0] 
        '''

        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        
