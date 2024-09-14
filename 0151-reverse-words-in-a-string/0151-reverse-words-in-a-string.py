class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        print(l)
        str=''
        for i in range(len(l)-1,0,-1):
            str=str+l[i]+' '
        str+=l[0]
        return str
            