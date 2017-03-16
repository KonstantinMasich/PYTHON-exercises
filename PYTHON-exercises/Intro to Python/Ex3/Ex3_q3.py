# ============================= #
# EX 3, Q3: lists common elems. #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #
import random

# Change these constants as you want:
MIN_LIST_SIZE = 1
MAX_LIST_SIZE = 20
MIN_ELEMENT_VALUE = 1
MAX_ELEMENT_VALUE = 100

# Generating 2 lists of various lenghts
l1_len = random.randint(MIN_LIST_SIZE, MAX_LIST_SIZE)
l2_len = l1_len
while l1_len == l2_len:
	l2_len = random.randint(MIN_LIST_SIZE, MAX_LIST_SIZE)
	
# Populating lists
l1 = random.sample(range(MIN_ELEMENT_VALUE, MAX_ELEMENT_VALUE), l1_len)
l2 = random.sample(range(MIN_ELEMENT_VALUE, MAX_ELEMENT_VALUE), l2_len)
print("List 1: ", sorted(l1)) # Displaying sorted lists for easier
print("List 2: ", sorted(l2)) # reading and comprehension

# Making sets out of lists
s1 = set(l1) # Read: set 1 = set from list1
s2 = set(l2)

# Result:
print("Common elements are: ", s1.intersection(s2))
