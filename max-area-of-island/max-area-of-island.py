class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    curr_area = 1
                    grid[i][j]=0
                    qu = [(i,j)]
                    while qu:
                        front = qu.pop(0)
                        row,col = front[0],front[1]
                        if row-1>=0 and grid[row-1][col]==1:
                            qu.append((row-1,col))
                            grid[row-1][col]=0
                            curr_area +=1
                        if row+1<n and grid[row+1][col]==1:
                            qu.append((row+1,col))
                            grid[row+1][col]=0
                            curr_area +=1
                        if col-1>=0 and grid[row][col-1]==1:
                            qu.append((row,col-1))
                            grid[row][col-1]=0
                            curr_area +=1
                        if col+1<m and grid[row][col+1]==1:
                            qu.append((row,col+1))
                            grid[row][col+1]=0 
                            curr_area +=1
                    max_area = max(max_area,curr_area)  
        return max_area                             
        