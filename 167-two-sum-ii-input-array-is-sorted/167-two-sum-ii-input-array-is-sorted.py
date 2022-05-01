class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low,top=0,len(numbers)-1
        
        while top>low:
            res = numbers[top]+numbers[low]
            
            if res<target:
                low+=1
            elif res>target:
                top-=1
            else:
                return[low+1,top+1]