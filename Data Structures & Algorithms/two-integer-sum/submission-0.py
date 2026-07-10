class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store {number: index}
        seen = {} 
        
        # enumerate gives us both the index and the number at the same time
        for i, num in enumerate(nums):
            temp = target - num
            
            # If the difference is in our dictionary, we found our pair!
            if temp in seen:
                return [seen[temp], i]
            
            # Otherwise, add the current number and its index to the dictionary
            seen[num] = i
            
        return []