# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        
        n = 0
        cur = head
        while cur!=None:
            cur=cur.next
            n+=1
        
        k = k%n
        if k>0:
            count=1
            prev = None
            cur = head
            while count!=n-k+1:
                prev = cur
                cur = cur.next
                count+=1
            
            prev.next=None
            tempHead = head
            head = cur
            while cur.next!=None:
                cur = cur.next
            print(cur.val)
            cur.next = tempHead
        return head
                