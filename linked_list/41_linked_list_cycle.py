from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()

    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
    print(sol.hasCycle(n1))

    a1, a2 = ListNode(1), ListNode(2)
    a1.next = a2; a2.next = a1
    print(sol.hasCycle(a1))

    b1 = ListNode(1)
    print(sol.hasCycle(b1))
