class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.mp:
            self.mp[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False         

    def remove(self, val: int) -> bool:
        if val in self.mp:
            index = self.mp[val]
            last_ele = self.arr[-1]
            self.mp[last_ele]=index
            self.arr[index]=last_ele
            self.arr[-1]= val
            del self.mp[val]
            self.arr.pop()
            return True
        else:
            return False    

        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()