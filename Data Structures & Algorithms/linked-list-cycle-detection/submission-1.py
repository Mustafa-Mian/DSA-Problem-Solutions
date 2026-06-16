# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) space -  can be optimized
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return True
            else:
                visited.add(cur)
                cur = cur.next
        return False