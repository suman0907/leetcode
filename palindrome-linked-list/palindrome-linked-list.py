# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        curr = slow
        next_p = slow
        prev = None
        while curr:
            next_p = curr.next
            curr.next = prev
            prev = curr
            curr= next_p
        l1 = prev
        l2= head
        while l1 and l2:
            if l1.val!=l2.val:
                return False
            l1= l1.next
            l2= l2.next    
        return True        

        