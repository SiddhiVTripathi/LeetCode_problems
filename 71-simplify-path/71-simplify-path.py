class Solution:
    def simplifyPath(self, path: str) -> str:
        ls = path.replace('//','/').split('/')
        stack = []
        for i,op in enumerate(ls):
            if op not in ('.','..',''):
                stack.append(op)
                continue
            if op=='..':
                if len(stack)!=0:
                    _ = stack.pop(-1)
            if op=='.':
                continue    
        st = '/'.join([x for x in stack])
        return '/'+st