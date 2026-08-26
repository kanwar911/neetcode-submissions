# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
# Put the head of every non-empty linked list into a min-heap.
# Pop the smallest node.
# Append that node to your result list.
# If that node has a next, push node.next into the heap.
# Repeat until the heap is empty.
        minHeap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(minHeap, (head.val, i, head))

        dummy = ListNode()
        curr = dummy

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next

