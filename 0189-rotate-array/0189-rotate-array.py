class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums[:]=(nums[k+1:]+nums[0:k])
        k = k % len(nums)  # In case k is greater than the length of the array
        nums[:] = nums[-k:] + nums[:-k]  #
    
                


        