class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l,h=0,len(nums)-1
        while(l<=h):
            
            val1=nums[l]**2
            val2=nums[h]**2
            
            if val1<val2:
                ans = [val2]+ans
                h-=1
            else:
                ans = [val1]+ans
                l+=1
        return ans