# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur = head = None
        while l1!=None and l2!=None:
            if cur==None:
                head = cur = ListNode()
            else:
                cur.next = ListNode()
                cur=cur.next
                
            cur.val,carry = (l1.val+l2.val+carry)%10,(l1.val+l2.val+carry)//10
            l1,l2= l1.next,l2.next
            
        while l1!=None:
            if cur==None:
                head = cur = ListNode()
            else:
                cur.next = ListNode()
                cur=cur.next
                
            cur.val,carry = (l1.val+carry)%10,(l1.val+carry)//10
            l1 = l1.next
            
        while l2!=None:
            if cur==None:
                head = cur = ListNode()
            else:
                cur.next = ListNode()
                cur=cur.next
                
            cur.val,carry = (l2.val+carry)%10,(l2.val+carry)//10
            l2 = l2.next
            
        if carry>0:
            cur.next = ListNode(carry)
        
        return head