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
            slow =  slow.next
            fast = fast.next.next
        curr = slow
        next_p = slow
        prev = None
        while curr:
            next_p = curr.next
            curr.next = prev
            prev = curr
            curr = next_p

        head1 = prev
        head2 = head
        while head1 and head2:
            if head1.val!=head2.val:
                return False
            head1= head1.next
            head2= head2.next
        
        return True            



        