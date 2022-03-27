import functools
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        strength = [(sum(ls),i) for i,ls in enumerate(mat)]
        def compare(key1,key2):
            if key1[0]<key2[0]:
                return -1
            elif key1[0]==key2[0]:
                if key1[1]<key2[1]:
                    return -1
                return 1
            else:
                return 1
        return [i[1] for i in sorted(strength,key=functools.cmp_to_key(compare))[:k]]