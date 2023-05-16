class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = []
        for i in range(0,9):
            for j in range(0,9):
                val = board[i][j]
                if val !=".":
                    result +=[(i,val),(val,j),(i//3,j//3,val)]
        return len(result)==len(set(result))            
        