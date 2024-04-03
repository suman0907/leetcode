# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        st = set()
        curr = headA
        while curr:
            st.add(curr)
            curr= curr.next
        curr= headB
        while curr:
            if curr in st:
                return curr
            curr = curr.next
        return None            