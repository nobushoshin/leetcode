# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current_node = head
        while current_node != None:
            tmp_node = current_node.next
            current_node.next = dummy_head.next
            dummy_head.next = current_node
            current_node = tmp_node
        
        return dummy_head.next


