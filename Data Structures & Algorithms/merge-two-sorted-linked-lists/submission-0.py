# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        one = list1
        two = list2
        dummy = ListNode()
        merged = dummy

        while one and two:
            if one.val <= two.val:
                merged.next = one
                one = one.next
            else:
                merged.next = two
                two = two.next

            merged = merged.next

        if one:
            merged.next = one

        if two:
            merged.next = two

        return dummy.next