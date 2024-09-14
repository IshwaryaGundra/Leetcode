class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize two arrays to store prefix and suffix products
        output = [1] * n
        prefix = 1
        
        # Calculate prefix products and store them in the output array
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products and multiply them with prefix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
