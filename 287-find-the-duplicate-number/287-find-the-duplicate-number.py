class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            cur = abs(i)
            if nums[cur]<0:
                duplicate = cur
                break
            nums[cur]=-nums[cur]
            
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
            
        return duplicate