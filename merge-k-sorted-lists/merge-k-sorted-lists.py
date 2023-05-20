# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap_list = []
        for i in range(len(lists)):
            curr = lists[i]
            if curr:
                heapq.heappush(heap_list,(curr.val,i, curr))
                curr = curr.next
        head = ptr = ListNode(0)
        while heap_list:
            node = heapq.heappop(heap_list)[2]
            ptr.next = node
            ptr = ptr.next
            if node.next:
                i +=1
                heapq.heappush(heap_list,(node.next.val,i,node.next)) 
        return head.next               
        