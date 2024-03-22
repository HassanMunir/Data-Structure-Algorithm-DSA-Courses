# Question

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set to store unique elements
        hashset = set()

        # Iterate through the array
        for n in nums:
            # If the current element is already in the set, return True (duplicate found)
            if n in hashset:
                return True
            # Otherwise, add the element to the set
            hashset.add(n)
        # If no duplicates found, return False
        return False
