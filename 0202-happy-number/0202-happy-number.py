class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # Use a set to track previously seen sums
        
        while n != 1:
            current_sum = 0
            while n > 0:
                current_sum += (n % 10) ** 2  # Sum of the squares of digits
                n //= 10  # Move to the next digit
            
            # If the sum is 1, return True as it's a happy number
            if current_sum == 1:
                return True
            
            # If we've seen this sum before, we are in a cycle (not a happy number)
            if current_sum in seen:
                return False
            
            # Otherwise, add the sum to the set and update n to the current sum
            seen.add(current_sum)
            n = current_sum
        
        return True  # In case we directly reach 1
