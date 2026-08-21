# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        ret_list = None
        tail = ret_list
        heap = []
        for i, list in enumerate(lists):
            if list:
                heapq.heappush(heap, (list.val, i, lists[i]))
                lists[i] = lists[i].next
        
        while heap:
            smallest = heapq.heappop(heap)
            if not ret_list:
                ret_list = ListNode(smallest[0], None)
                tail = ret_list
            else:
                tail.next = ListNode(smallest[0], None)
                tail = tail.next
            if smallest[2].next:
                heapq.heappush(heap, (lists[smallest[1]].val, smallest[1], lists[smallest[1]]))
                lists[smallest[1]] = lists[smallest[1]].next
            
        return ret_list
            
