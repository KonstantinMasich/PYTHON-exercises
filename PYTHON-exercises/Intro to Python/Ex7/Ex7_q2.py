# ============================= #
# EX 7, Q2: binary search func  #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #
import random # for testing
from bisect import bisect_left # for binary search

def bin_search(a, e):
    "Runs binary search of element 'e' on list 'a'."
    # Here I use built-in bisect_left function that finds
    # an insertion point for 'e' to maintain sorted order
    # of 'a'.
    index = bisect_left(a, e)
    if (index >= len(a)): # Index out of bounds
        return -1
    if (a[index] == e):   # Element at insertion point equals to 'e'
        return index
    else:
        return -1         # Element not found in list

# 1. Getting user input and checking validity:
# a. Getting a list of numbers
try:
    print("Please enter numbers separated by Space, and hit Enter:")
    usr_list = [int(num) for num in input().split()]
except ValueError:
    print("Error: illegal characters in the list!")
    exit()
if (len(usr_list) == 0):
    print("Error: the list is empty!")
    exit()
# b. Making sure user's list is sorted:
srt_list = sorted(usr_list)
# c. Getting a to-be-found element
try:
    usr_elem = int(input("Please enter the element you want to find: "))
except ValueError:
    print("Error: illegal characters in the element / empty element!")
    exit()

# 2. Searching for specified element
print(bin_search(srt_list, usr_elem))



# Uncomment to test:
"""
test_list = sorted(random.sample(range(1, 30), 10))
print("Test list: \n", test_list)
for i in range(10):
    val = random.randint(-1,31)
    print(val, " is at place: ", bin_search(test_list, val))
"""
