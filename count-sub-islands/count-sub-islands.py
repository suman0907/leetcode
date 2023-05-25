class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        vis = set()

        def dfs(r,c):
            if r<0 or c<0 or r==rows or c==cols or (r,c) in vis or grid2[r][c]==0:
                return True
            vis.add((r,c))
            res = True
            if grid1[r][c]==0:
                res= False
            res = dfs(r-1,c) and res
            res = dfs(r+1,c) and res
            res = dfs(r,c+1) and res
            res = dfs(r,c-1) and res

            return res       
        count = 0 
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] and (r,c) not in vis and dfs(r,c):
                    count +=1
        return count            



