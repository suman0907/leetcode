class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        comp_list = [[c2-c1,c1,c2] for c1,c2 in costs]
        comp_list.sort()
        res = 0
        n = len(costs)//2
        for i in range(len(comp_list)):
            print(i)
            if i<n:
                res+=comp_list[i][2]
            else:
                res+=comp_list[i][1]    
       
        return res