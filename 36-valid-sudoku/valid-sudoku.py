class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for  i in range(0,9):
            for j in range(0,9):
                if board[i][j]!=".":
                    val = board[i][j]
                    res+=[(i,val),(val,j),(i//3,j//3,val)]
        print(res)
        return len(res)==len(set(res))            
        