# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy=ListNode(0)
        cur = dummy
        carry =0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1=0
            if l2:
                val2 = l2.val
            else:
                val2=0
            total = val1+val2+carry

            num = total %10
            carry = total//10

            cur.next = ListNode(num)
            cur = cur.next
            if l1:
                l1=l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next