# Question

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        # Create a dictionary to store the complement of each number and its index


        for i,n in enumerate (nums):
            # Calculate the complement needed to achieve the target
            diff = target - n

            # Check if the complement exists in the dictionary
            if diff in prevMap:
            # If yes, return the indices of the current number and its complement
                return [prevMap [diff], i]
            # Otherwise, add the current number and its index to the dictionary
            prevMap [n] = i
        
        #If no such pair is found, return an empty list
        return