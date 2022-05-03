# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0;
        mid = head;
        while (head != None):
        
            if count & 1:
                mid = mid.next;

            count+=1
            head = head.next;

        return mid