class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i=0
        
        while i<len(s):
            
            if len(stack)==0:
                if s[i] in ('(','[','{'):
                    stack.append(s[i])
                    i+=1
                    continue
                else:
                    return False
            
            if s[i] in (')','}',']'):
                top = stack.pop(-1)
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == '}' and top != '{':
                    return False
                if s[i] == ']' and top != '[':
                    return False
            else:
                stack.append(s[i])
            
            i+=1
        

        return not len(stack)
            
        