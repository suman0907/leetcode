class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        no_island = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    no_island += 1
                    grid[i][j]= "0"
                    qu=[(i,j)]
                    while qu:
                        row = qu[0][0]
                        col = qu[0][1]
                        qu.pop(0)
                        if row-1>=0 and grid[row-1][col]=="1":
                            grid[row-1][col]="0"
                            qu.append((row-1,col))
                        if row+1<n and grid[row+1][col]=="1":
                            grid[row+1][col]="0"
                            qu.append((row+1,col))
                        if col-1>=0 and grid[row][col-1]=="1":
                            grid[row][col-1]="0"
                            qu.append((row,col-1))
                        if col+1<m and grid[row][col+1]=="1":
                            grid[row][col+1]="0"
                            qu.append((row,col+1)) 
        return no_island                               


        