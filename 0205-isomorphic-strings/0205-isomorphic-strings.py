class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps=[]
        mapt=[]
        if len(s)!=len(t):
            return False
        for i in s:
            maps.append(s.index(i))
        for i in t:
            mapt.append(t.index(i))
        if maps==mapt:
            return True
        
        
        