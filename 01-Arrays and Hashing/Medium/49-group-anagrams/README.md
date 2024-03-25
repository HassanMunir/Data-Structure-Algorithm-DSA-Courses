## Explanation

### Define the function groupAnagrams that takes the input array of strings strs

### Inside the function, we initialize a defaultdict with the default value as an empty list. This dictionary will hold the grouped anagrams

### We iterate through each string s in the input array strs

### For each string s, we sort its characters and join them back into a string. This sorted string will serve as the key for grouping anagrams

### Append the original string s to the list associated with the sorted string key in the anagrams dictionary

### After iterating through all strings, return the values of the anagrams dictionary as a list of lists, containing grouped anagrams

### Finally, demonstrate the usage of the function with an example input array input_strs and print the result
