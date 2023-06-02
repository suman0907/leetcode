class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mp = {i:[] for i in range(n)}
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                mp[i].append([dist,j])
                mp[j].append([dist,i])
        heap = [[0,0]]
        res = 0
        vis = set()
        while len(vis)<n:
            front = heapq.heappop(heap)
            cost = front[0]
            point = front[1]
            if point in vis:
                continue
            vis.add(point)
            res +=cost 
            for dist, nei in mp[point]:
                if nei not in vis:
                    heapq.heappush(heap,[dist,nei])
        return res                       

        