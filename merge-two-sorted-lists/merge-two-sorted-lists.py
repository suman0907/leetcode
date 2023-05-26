# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ptr = ListNode(0)
        l1 = list1
        l2= list2
        while l1 and l2:
            if l1.val<l2.val:
                ptr.next=l1
                ptr=ptr.next
                l1= l1.next
            else:
                ptr.next= l2
                ptr= ptr.next
                l2= l2.next
        if l1:
            ptr.next=l1
        if l2:
            ptr.next=l2
        return dummy.next                   
            
        