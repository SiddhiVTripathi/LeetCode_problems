class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def process(string):
            
            dif=0
            for x in reversed(string):
                if x=="#":
                    dif+=1
                elif dif:
                    dif-=1
                else:
                    yield x
        return all(x==y for x,y in itertools.zip_longest(process(s),process(t)))