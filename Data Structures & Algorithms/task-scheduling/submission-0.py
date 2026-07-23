from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # Max heap (negative counts)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()      # (available_time, remaining_count)
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)   # reduce remaining count

                if cnt:
                    q.append((time + n, cnt))

            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q.popleft()[1])

        return time