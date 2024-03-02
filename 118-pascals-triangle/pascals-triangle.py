class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows-1):
            temp = [0]+result[-1]+[0]
            temRes = []
            for j in range(0,len(temp)-1):
                temRes.append(temp[j]+temp[j+1])
            result.append(temRes)
        return result    


        