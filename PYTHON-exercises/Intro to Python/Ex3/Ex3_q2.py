# ============================= #
# EX 3, Q2: frequent words      #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #
from collections import Counter

# 1. Getting input from user:
# Please enter words separated by a space, for example:
# "to be or not to be"
usr_input = input("Enter a sequence of words: ")
while not usr_input:
    print("Error: empty sequence. Please enter again!")
    usr_input = input("Enter a sequence of words: ")

# For Moti: a test, uncomment to use:
"""
usr_input = "zoo zoo dog zoo cat cat zoo hawk animal hawk"
# Output: animal x1, cat x2, dog x1, hawk x2, zoo x4
# or:
#usr_input = "z z      a z  b   z  a a z   k a   k k z   k  z a"
# Output: a x5, b x1, k x4 , z x7
"""

# 2. Counting frequencies:
usr_input = usr_input.lower() # lowercase to count more precisely
words = usr_input.split()
counter_dict = Counter(words)

# 3. Now counter_dict has a dictionary where words are keys
#    and their frequencies are values. We sort keys and print
#    every key with its respective value in the dictionary:
sorted_keys = sorted(counter_dict.keys())
for key in sorted_keys:
    print (key, counter_dict[key]) # Prints key + value

# This solution does not sort the dictionary itself, because it is not
# really needed as the output is sorted as requested. If necessary,
# the dictionary could be presented using OrderedDict, or using other methods.
