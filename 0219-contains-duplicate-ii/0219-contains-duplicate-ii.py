class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}  # Dictionary to store the most recent index of each element
        
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True  # Duplicate found within distance k
            
            index_map[num] = i  # Update the most recent index of the current element
        
        return False
