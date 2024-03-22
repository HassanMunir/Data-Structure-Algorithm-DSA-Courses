## Explanation

### A function that two_sum that takes an array 'nums' and a target integer 'target'

### I create a hashmap called "prevMap". This will store the difference of each number encountered so far, along with its index in the array

### Then iterate through the array 'nums' using 'enumerate()' to simultaneously get the index 'i' and the value 'num'

### For each number 'num', I calculate the difference needed to achieve the target sum (difference = target - n)

### Check if this difference exists in the "prevMap". If it does, it means we have found the pair that adds up to the target sum, so we return the indices of the current number 'i' and the index of its difference stored in "prevMap"[diff]

### If the difference does not exist in the hashmap, we add the current number and its index to the hashmap

### If no such pair is found after iterating through the entire array, we return an empty list
