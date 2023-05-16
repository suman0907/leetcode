class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows-1):
            temp_list = [0]+result[-1]+[0]
            res = []
            for i in range(0,len(temp_list)-1):
                res.append(temp_list[i]+temp_list[i+1])
            result.append(res) 
        return result       



        