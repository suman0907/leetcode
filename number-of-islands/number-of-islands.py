class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        no_island = 0
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]=="1":
                    grid[i][j] = "0"
                    no_island +=1
                    qu = []
                    qu.append([i,j])
                    while qu:
                        front = qu[0]
                        row= front[0]
                        col = front[1]
                        qu.pop(0)
                        if row-1>=0 and grid[row-1][col]=="1":
                            grid[row-1][col]= "0"
                            qu.append([row-1,col])
                        if row+1<n and grid[row+1][col]=="1":
                            grid[row+1][col]= "0"
                            qu.append([row+1,col])
                        if col-1>=0 and grid[row][col-1]=="1":
                            grid[row][col-1]= "0"
                            qu.append([row,col-1])
                        if col+1<m and grid[row][col+1]=="1":
                            grid[row][col+1]= "0"
                            qu.append([row,col+1]) 
        return no_island                           


        
        