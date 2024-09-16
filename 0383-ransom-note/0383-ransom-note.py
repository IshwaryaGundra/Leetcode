from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d=Counter(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in d and  d[ransomNote[i]]>0:
                d[ransomNote[i]] -= 1
            else:
                return False
        return True

        
        