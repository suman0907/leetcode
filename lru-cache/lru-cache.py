from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.mp = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.mp:
            val = self.mp[key]
            del self.mp[key]
            self.mp[key]=val
            return self.mp[key]
        else:
            return -1    



    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            del self.mp[key]
            self.mp[key]=value
        else:
            if len(self.mp)<self.capacity:
                self.mp[key]=value
            else:
                self.mp.popitem(last=False)
                self.mp[key]=value        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)