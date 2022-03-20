class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        s = reduce(set.__and__, (set(d) for d in zip(tops, bottoms)))
        if not s: return -1
        x = s.pop()
        return min(len(tops) - tops.count(x), len(bottoms) - bottoms.count(x))