class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # move both pointers
        while fast:
            fast = fast.next
            slow = slow.next

        # delete node
        slow.next = slow.next.next

        return dummy.next