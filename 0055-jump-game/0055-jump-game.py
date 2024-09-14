class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        for i in range(len(nums)):
            if i>maxi:
                return 0
            maxi=max(maxi,i+nums[i])
        return 1