## Explanation

### hashset = set(): Initializes an empty set called hashset. A set is a data structure that stores unique elements, so duplicates are automatically eliminated when adding elements to it

### for n in nums: Iterates over each element n in the input list nums

### if n in hashset: Checks if the current element n is already in the hashset. If it is, it means that n is a duplicate, so the method returns True, indicating that the list contains duplicates

### hashset.add(n): If the current element n is not in the hashset, it adds n to the set using the add method

### return False: If the loop completes without finding any duplicates (i.e., no duplicate elements are found during iteration), the method returns False, indicating that the list does not contain any duplicates
