class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=nums.count(val)

        while k!=0:
            if val  in nums:
                nums.remove(val)
                k=k-1
        return len(nums)-k