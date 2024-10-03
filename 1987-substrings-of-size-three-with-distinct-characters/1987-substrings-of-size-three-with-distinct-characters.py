class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=0
        r=0
        i=0
        n=len(s)
        c=0
        while i<n:
            if r-l+1<3:
                r+=1
            else:
                #print(sorted(set(s[l:r+1])))
                #print(sorted(s[l:r+1]))
                if len(s[l:r+1])==3:
                    if len(set(s[l:r+1]))==3:
                        c=c+1
                l=l+1
                r=r+1
            i=i+1
        return c
        