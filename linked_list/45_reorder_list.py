from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

def make_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

if __name__ == "__main__":
    sol = Solution()
    h1 = make_list([1,2,3,4])
    sol.reorderList(h1)
    print_list(h1)

    h2 = make_list([1,2,3,4,5])
    sol.reorderList(h2)
    print_list(h2)
