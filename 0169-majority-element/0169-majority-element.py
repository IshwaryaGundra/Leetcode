from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''d=Counter(nums)
        for i in (d):
            print(d[i])
            if d[i]>len(nums)/2:
                return i
        return -1'''
        nums.sort()
        return nums[len(nums)//2]

        