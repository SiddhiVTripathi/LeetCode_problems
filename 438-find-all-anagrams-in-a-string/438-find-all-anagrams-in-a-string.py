class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        
        p_counter = {}
        for x in range(m):
            if p[x] in p_counter:
                p_counter[p[x]] +=1
            else:
                p_counter[p[x]] =1
                
        window = {}
        v = []
        for i in range(0, n-m+1):
            if i == 0:
                window_str = s[i:i+m]
                for x in range(m):
                    if window_str[x] in window:
                        window[window_str[x]] +=1
                    else:
                        window[window_str[x]] = 1
            else:
                b = s[i-1]
                if b in window:
                    window[s[i-1]] -=1
                    if window[s[i-1]] == 0:
                        del window[s[i-1]]
                    
                x = s[i+m-1]
                if x in window:
                    window[s[i+m-1]] +=1
                else:
                    window[s[i+m-1]] =1
                    
            if window == p_counter:
                v.append(i)
            
            
        return v