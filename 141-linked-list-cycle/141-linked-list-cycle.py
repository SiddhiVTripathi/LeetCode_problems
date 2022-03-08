# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        else:
            visited = set()
            while (head.next != None):
                if (head.next in visited):
                    return True
                visited.add(head)
                head = head.next

            return False
            