from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = collections.defaultdict(list)
        for s,d,t in times:
            mp[s].append([d,t])
        heap = []    
        heapq.heappush(heap,[0,k])
        total_time = 0
        vis = set()
        while heap:
            front = heapq.heappop(heap)
            src = front[1]
            time = front[0]
            if src in vis:
                continue
            vis.add(src)
            for dst,t in mp[src]:
                if dst not in vis:
                    heapq.heappush(heap,[t+time,dst])
            total_time= max(total_time,time) 
        return total_time  if len(vis)==n else -1    


