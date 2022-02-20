from functools import cmp_to_key
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def cmp(a,b):
            if a[0]>b[0]:
                return 1
            elif a[0]==b[0]:
                if a[1]>b[1]:
                    return -1
                else:
                    return 1
            else:
                return -1
        
        intervals.sort(key = cmp_to_key(cmp))
        
        i=1
        for interval in intervals[1:]:
            if interval[0]>=intervals[i-1][0] and interval[1]<=intervals[i-1][1]:
                intervals.remove(interval)
                continue
            i+=1
        return len(intervals)
            