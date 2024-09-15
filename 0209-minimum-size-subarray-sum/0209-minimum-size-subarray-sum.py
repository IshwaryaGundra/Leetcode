class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        mini=float('inf')
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while(current_sum >= target):
                mini = min(mini,right-left+1)
                current_sum -= nums[left]
                left += 1
        return mini if mini!=float('inf') else 0

            
        