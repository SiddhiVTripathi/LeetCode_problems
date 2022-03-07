# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h3 = None
        
        while list1!=None and list2!=None:
            if h3==None:
                cur = ListNode()
                h3=cur
            else:
                cur.next = ListNode()
                cur = cur.next
                
            if list1.val<=list2.val:
                cur.val = list1.val
                list1 = list1.next
            else:
                cur.val = list2.val
                list2 = list2.next
            
        while list1!=None:
            if h3==None:
                cur = ListNode()
                h3=cur
            else:
                cur.next = ListNode()
                cur = cur.next
            cur.val = list1.val
            list1 = list1.next
            
        while list2!=None:
            if h3==None:
                cur = ListNode()
                h3=cur
            else:
                cur.next = ListNode()
                cur = cur.next
            cur.val = list2.val
            list2 = list2.next
            
        return h3