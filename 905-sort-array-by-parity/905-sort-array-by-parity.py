class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odds=[]
        evens=[]
        
        for i in nums:
            if i%2==0:
                evens.append(i)
            else:
                odds.append(i)
        
        return evens+odds