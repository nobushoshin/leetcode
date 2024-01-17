# https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_int = self.get_number(l1)        
        l2_int = self.get_number(l2)
        str_sum = str(l1_int + l2_int)

        dummy = ListNode()
        current = dummy
        for c in str_sum:
            node = ListNode(val=int(c))
            current.next = node
            current = node
        
        return dummy.next


    def get_number(self, l):
        numbers = []
        while l != None:
            numbers.append(str(l.val))
            l = l.next
        return int(''.join(numbers))
