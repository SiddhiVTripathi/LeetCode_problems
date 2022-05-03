# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        temp2 = temp
        m=0
        
        while(temp != None):
            temp = temp.next
            m+=1
    
        if(m == n):
            return head.next
        
        temp = head
        m-=n
        
        for i in range(m):
            temp2 = temp
            temp = temp.next
        temp2.next = temp.next
        return head