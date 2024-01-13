class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_flag = True
        l2_flag = True
        dummy = ListNode()
        current_node = dummy
        next_n = 0
        while l1_flag or l2_flag:
            if l1_flag == False:
                n = l2.val
            elif l2_flag == False:
                n = l1.val
            else:
                n = l1.val + l2.val
            
            number = (n + next_n) % 10
            next_n = (n + next_n) // 10
            current_node = self.add_node(number, current_node)

            if l1.next == None:
                l1_flag = False
            else:
                l1 = l1.next
            
            if l2.next == None:
                l2_flag = False
            else:
                l2 = l2.next

        if next_n > 0:
            current_node = self.add_node(next_n, current_node)
        
        return dummy.next
    

    def add_node(self, num, current_node):
        node = ListNode()
        node.val = num
        current_node.next = node
        return node      