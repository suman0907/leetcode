class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        index = 0
        gs =0
        cs = 0
        for i in range(len(gas)):
            gs +=gas[i]
            cs +=cost[i]
            total +=gas[i]-cost[i]
            if total<0:
                total = 0
                index =i+1
        if gs<cs:
            return -1        
        return index        

        