class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        res =0
        prev_nonequal = nums[0]
        for i in range(len(nums)):
            if i==0:
                continue
            if i==len(nums)-1:
                continue
            
            if nums[i+1]==nums[i]:
                continue
            
            if (prev_nonequal<nums[i] and nums[i+1]<nums[i]) or (prev_nonequal>nums[i] and nums[i+1]>nums[i]):
                res+=1
                prev_nonequal = nums[i]
            
        print(res)
        return res