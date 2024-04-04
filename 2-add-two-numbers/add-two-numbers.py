# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ptr = ListNode()
        curr1=l1
        curr2= l2
        carry = 0
        while curr1 or curr2 or carry:
            val1 = val2=0
            if curr1:
                val1= curr1.val
                curr1= curr1.next
            if curr2:
                val2 = curr2.val
                curr2= curr2.next
            summ = val1+val2+carry
            carry= summ//10
            ptr.next = ListNode(summ%10)
            ptr = ptr.next
        return dummy.next            

        