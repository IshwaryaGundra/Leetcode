class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        for i in nums:
            k=nums.count(i)
            s=0
            while(k>2):
                s=s+1
                nums.remove(i)
                k=k-1
        return len(nums)-s
        