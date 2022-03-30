from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0]>target:
                return False
            res = bisect_left(row,target)
            if res<len(row) and row[res]==target:
                return True
        return False
            