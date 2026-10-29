import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)

        time = 0
        queue = deque()  # (remaining_count_negated, time_when_ready)

        while heap or queue:
            time += 1

            if heap:
                remaining = heapq.heappop(heap) + 1  # run one instance
                if remaining < 0:
                    queue.append((remaining, time + n))

            if queue and queue[0][1] <= time:
                heapq.heappush(heap, queue.popleft()[0])

        return time