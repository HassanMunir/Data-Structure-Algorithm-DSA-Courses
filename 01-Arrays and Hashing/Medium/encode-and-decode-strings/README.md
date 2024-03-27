## Explanation

### Encode Function (encode method):

#### This method takes a list of strings strs as input

#### It initializes an empty string res to store the encoded result

#### It iterates through each string s in the input list strs

#### For each string s, it appends the length of the string followed by "#" and the string itself to the res string

#### Finally, it returns the encoded result res

### Decode Function (decode method):

#### This method takes an encoded string str as input

#### It initializes an empty list res to store the decoded strings

#### It initializes an index i to 0 for traversing the input string

#### It enters a while loop that runs until i reaches the end of the input string

#### Within the loop, it initializes another index j to i

#### It increments j until it finds "#" in the input string

#### It extracts the length of the encoded string from the substring starting from i to j

#### It converts the length to an integer and stores it in the variable length

#### It extracts the encoded string from the substring starting from j+1 to j+1+length and appends it to the res list

#### It updates the index i to j+1+length to move to the next encoded string in the input

#### Finally, it returns the decoded list res
