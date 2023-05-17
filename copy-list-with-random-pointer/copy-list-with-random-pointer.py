"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        mp = {None:None}
        while curr:
            mp[curr]= Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = mp[curr]
            copy.next = mp[curr.next]
            copy.random = mp[curr.random]
            curr = curr.next
        return mp[head]       



        