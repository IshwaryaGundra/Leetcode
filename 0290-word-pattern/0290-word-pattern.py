class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l1=[]
        l2=[]
        s=s.split()
        for i in s:
            l1.append(s.index(i))
        for i in pattern:
            l2.append(pattern.index(i))
        if l1==l2:
            return True
        return False
        