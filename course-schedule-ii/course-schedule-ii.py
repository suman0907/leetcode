class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        vis = set()
        cycle = set()
        result = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in vis:
                return True
            cycle.add(crs)    
            for pre in preMap[crs]:
                if dfs(pre)==False:
                    return False
            cycle.remove(crs)
            vis.add(crs)
            result.append(crs)
            return True                

        for crs in  range(numCourses):
            if dfs(crs)==False:
                return []
        return result        
