# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,h=0,n
        
        while h-l>1:
            mid = l+(h-l)//2
            if isBadVersion(mid):
                h=mid
            else:
                l=mid+1
                
        if isBadVersion(l):
            return l
        else:
            return h