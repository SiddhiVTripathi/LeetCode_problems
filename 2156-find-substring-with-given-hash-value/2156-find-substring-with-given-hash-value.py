class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n,hashSum,mul = len(s),0,1
        
        for i in range(k):
            hashSum+=((ord(s[i])-ord('a')+1)*mul)
            mul*=power
            
        f = hashSum%modulo
        j = 0
        mul//=power
        
        for i in range(k,n):
            if f==hashValue:
                return s[j:j+k]
            hashSum-=(ord(s[j])-ord('a')+1)
            hashSum1 = hashSum
            hashSum=hashSum//power
            hashSum+=((ord(s[i])-ord('a')+1)*mul)
            f = hashSum%modulo
            j+=1
        return s[j:j+k]