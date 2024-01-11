# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val <= list2.val:
            smaller = list1
            larger = list2
        else:
            smaller = list2
            larger = list1

        merged_linked_list_head = smaller

        while True:
            next_smaller = smaller.next
            if next_smaller == None:
                smaller.next = larger
                break

            if larger.val <= next_smaller.val:
                smaller.next = larger
                smaller = larger
                larger = next_smaller
            else:
                smaller = next_smaller
        
        return merged_linked_list_head
