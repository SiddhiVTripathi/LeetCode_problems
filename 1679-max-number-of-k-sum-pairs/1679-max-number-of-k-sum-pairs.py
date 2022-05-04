class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=0
        l,h=0,len(nums)-1
        
        while l<h:
            sum_ = nums[l]+nums[h]
            if sum_==k:
                res+=1
                l+=1
                h-=1
            elif sum_<k:
                l+=1
            else:
                h-=1
        return res