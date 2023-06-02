from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        mp = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            mp[src].append([dst,succProb[i]])
            mp[dst].append([src,succProb[i]])
        vis = set()
        heap = [[-1,start]]
        while heap:
            front = heapq.heappop(heap)
            prob, curr = front
            if curr==end:
                return prob*-1
            vis.add(curr)
            for nei, edgeprob in mp[curr]:
                if nei not in vis:
                    heapq.heappush(heap,[edgeprob*prob,nei]) 
        return 0               



