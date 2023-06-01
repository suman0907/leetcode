import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for s,d,t in times:
            mp[s].append([t,d])
        heap = []
        heapq.heappush(heap,[0,k])
        vis = set()
        total_time = 0
        while heap:
            front = heapq.heappop(heap)
            node = front[1]
            time = front[0]
            if node in vis:
                continue
            vis.add(node)
            for t, d in mp[node]:
                if d not in vis:
                    heapq.heappush(heap,[t+time,d])
            total_time = max(total_time,time)
        return total_time if len(vis)==n  else -1          

        