class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s,len_t = len(s),len(t)
        i,j=0,0
        while j<len_t and i<len_s:
            if s[i]==t[j]:
                i+=1
            j+=1
        if i==len_s:
            return True
        return False