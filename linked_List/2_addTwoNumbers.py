# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
class Solution:
    def addTwoNumbers(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        medium
        """
        dummy= ListNode(0)
        head=dummy
        while l1 or l2 or add:
            if l1:
                add+=l1.val
                l1=l1.next
            if l2:
                add+=l2.val
                l2=l2.val
            dummy.next,add=ListNode(add%10),add//10#注意空节点的实例化
            dummy=dummy.next
        return head.next




