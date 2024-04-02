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
            fast = fast.next.next
        curr = next_p = slow
        prev = None
        while curr:
            next_p = curr.next
            curr.next = prev
            prev = curr
            curr = next_p
        ptr1 = head
        ptr2 = prev
        while ptr1 and ptr2:
            if ptr1.val!=ptr2.val:
                return False
            ptr1= ptr1.next
            ptr2 = ptr2.next    
        return True        


        