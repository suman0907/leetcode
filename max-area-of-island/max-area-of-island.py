class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        no_island = 0
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]==1:
                    no_island +=1
                    grid[i][j]=0
                    queue = []
                    queue.append([i,j])
                    area = 1
                    
                    while queue:
                        front = queue[0]
                        queue.pop(0)
                        row = front[0]
                        col = front[1]
                        if row-1>=0 and grid[row-1][col]==1:
                            grid[row-1][col]=0
                            queue.append([row-1,col])
                            area +=1
                        if row+1<n and grid[row+1][col]==1:
                            grid[row+1][col]=0
                            queue.append([row+1,col])
                            area +=1
                        if col-1>=0 and grid[row][col-1]==1:
                            grid[row][col-1]=0
                            queue.append([row,col-1]) 
                            area +=1
                        if col+1<m and grid[row][col+1]==1:
                            grid[row][col+1]=0
                            queue.append([row,col+1])  
                            area +=1 
                    max_area = max(max_area,area)        
        return max_area                          