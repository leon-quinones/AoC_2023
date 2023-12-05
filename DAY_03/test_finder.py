import re
from functools import reduce

# initializing string
test_str = "GeeksforGeeks is best for Geeks"

# initializing substring
test_sub = "Geeks"

# using re.finditer() to find all occurrences of substring in string
occurrences = re.finditer(test_sub, test_str)
print(occurrences)
# using reduce() to get start indices of all occurrences
res = reduce(lambda x, y: (x + [y.span()] ) , occurrences, [])

# printing result
print("The start indices of the substrings are : " + str(res))
# This code is contributed by Jyothi pinjala
