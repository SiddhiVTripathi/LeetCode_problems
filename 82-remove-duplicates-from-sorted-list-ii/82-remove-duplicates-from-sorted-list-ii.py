# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        prev = cur = head
        
        while cur!=None and cur.next!=None:
            flag = False
            while cur!=None and cur.next!=None and  cur.val==cur.next.val :
                flag =True
                cur=cur.next
                
            if flag:
                if cur.val==prev.val:
                    head =cur = prev = cur.next
                else:
                    prev.next=cur.next
                    cur = prev.next
            else:
                prev = cur
                cur=cur.next
                
        return head