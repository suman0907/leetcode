class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key= lambda x:(-x[0],x[1]))
        output = []
        for key in people:
            output.insert(key[1],key)
        return output    
        