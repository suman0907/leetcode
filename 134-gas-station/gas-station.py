class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        index = 0
        gc = 0
        cc=0
        for i in range(len(gas)):
            gc +=gas[i]
            cc +=cost[i]
            total += gas[i]-cost[i]
            if total<0:
                total =0
                index = i+1
        if gc<cc:
            return -1
        return index            

        