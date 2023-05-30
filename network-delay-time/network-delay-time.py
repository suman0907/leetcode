import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for s,d, t in times:
            mp[s].append([t,d])
        heap = []
        heapq.heappush(heap,[0,k])
        total_time = 0
        vis  = set()
        while heap: 
            front = heapq.heappop(heap)
            time = front[0]
            src = front[1]
            if src in vis:
                continue
            vis.add(src)
            for t,d in mp[src]:
                if d not in vis:
                    heapq.heappush(heap,[t+time,d]) 
            total_time = max(total_time,time)
        return total_time if len(vis)==n else -1             



        