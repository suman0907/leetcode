# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k ==0 :
            return head
        k = k%self.getSize(head)
        if k == 0:
            return head
        slow = head
        fast = head
        while fast and k>=0:
            fast = fast.next
            k -=1
        while fast:
            slow= slow.next
            fast = fast.next
        dummy=ptr =  slow.next
        slow.next = None
        while ptr and ptr.next:
            ptr = ptr.next  
        ptr.next = head
        return dummy  
    def getSize(self,head):
        ptr = head
        count = 0
        while ptr:
            count +=1
            ptr = ptr.next
        return count               
        