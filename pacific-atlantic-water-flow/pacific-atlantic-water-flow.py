class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        def dfs(r,c,vis,preheight):
            if (r,c) in vis or r<0 or c<0 or r==rows or c==cols or heights[r][c]<preheight:
                return
            vis.add((r,c))
            dfs(r-1,c,vis,heights[r][c])  
            dfs(r+1,c,vis,heights[r][c])
            dfs(r,c-1,vis,heights[r][c])
            dfs(r,c+1,vis,heights[r][c])  

        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result                

        