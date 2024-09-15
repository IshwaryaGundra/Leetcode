class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #l = s
        if len(s)==0:
            return 0
        maxi=0
        hashset = set()
        '''for i in range(len(l)):
            string = l[i]
            for j in range(i+1,len(l)):
                string += l[j]
                print(string)
                if sorted(string) == sorted(set(string)):
                    print(string)
                    maxi = max(maxi,len(string))
        return maxi'''
        left = 0
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            maxi = max(maxi,right-left+1)
        return maxi


        