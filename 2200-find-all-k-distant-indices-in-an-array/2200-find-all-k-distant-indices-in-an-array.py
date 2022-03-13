class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        key_indices = [i for (i, e) in enumerate(nums) if e == key]
        N = len(nums)
        
        for i in range(len(nums)):
            
            dist = float('inf')
            idx = bisect_left(key_indices, i)
            if idx > 0:
                dist = min(dist, abs(i - key_indices[idx - 1]))
            if idx < len(key_indices):
                dist = min(dist, abs(key_indices[idx] - i))

            if dist <= k:
                ans.append(i)
        return ans
                