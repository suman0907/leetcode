class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        length = len(citations)
        count = 0
        for i in range(len(citations)):
            if citations[i]>length:
                count +=1
                continue
            if  count>=citations[i]:
                return count 
            count +=1     
        return count        

        