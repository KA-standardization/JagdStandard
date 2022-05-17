'''
https://leetcode-cn.com/problems/linked-list-cycle/
'''


class Solution:
    fast = None
    slow = None

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None: return False
        self.slow = head
        self.fast = head.next
        while self.fast != self.slow:
            # if head is None: return False
            if self.slow is None or self.fast is None: return False
            if self.fast.next is None: return False
            self.slow = self.slow.next
            self.fast = self.fast.next.next
        return True
