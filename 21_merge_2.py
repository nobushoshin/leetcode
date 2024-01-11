# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/solutions/1826693/python3-merging-explained/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head_node = ListNode()
        current_node = head_node
        
        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = list1
                current_node = list1
                list1 = list1.next
            else:
                current_node.next = list2
                current_node = list2
                list2 = list2.next

        if list1 or list2:
            current_node.next = list1 if list1 else list2

        return head_node.next