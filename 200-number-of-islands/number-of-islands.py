class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_island = 0
        m= len(grid)
        n = len(grid[0])
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j]=="1":
                    no_island +=1
                    qu = [(i,j)]
                    grid[i][j]="0"
                    self.bfs(qu,m,n,grid)
        return no_island            
    def bfs(self, qu, m,n,grid):
        while qu:
            row,col = qu.pop(0)
            if row-1>=0 and grid[row-1][col]=="1":
                qu.append((row-1,col))
                grid[row-1][col]="0"
            if row+1<m and grid[row+1][col]=="1":
                qu.append((row+1,col))
                grid[row+1][col]="0"
            if col-1>=0 and grid[row][col-1]=="1":
                qu.append((row,col-1))
                grid[row][col-1]="0"
            if col+1<n and grid[row][col+1]=="1":
                qu.append((row,col+1))
                grid[row][col+1]="0"            

        