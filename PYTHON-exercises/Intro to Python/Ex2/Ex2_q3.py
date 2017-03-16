# ============================= #
# EX 2, Q2: lists common elems. #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #
from operator import itemgetter

# Please enter data in following format:
# [name] [age] [height]
# Example:
#   Samuel 22 167
#   David  18 178
#   ... etc ...

res = [] # result list that holds all data
while True:
	usr_input = input("Enter data: ")
	if not usr_input:
		break
	formatted_input = usr_input.split()
	# Checking input validity:
	if (len(formatted_input) != 3):
		print("Error: please provide exactly 3 attributes - name, age, height!")
		continue
	if not (formatted_input[1].isdigit() and formatted_input[2].isdigit()):
		print("Error: age and height must be numeric!")
		continue
	# Appending entry to list:
	if formatted_input:
		res.append([ formatted_input[0],     \
			         int(formatted_input[1]),\
                     int(formatted_input[2]) \
			       ])
# Sorting and printing results:
print("Sorted list is:")
print(sorted(res, key=itemgetter(0, 1, 2)))


"""
# Uncomment if needed: sample test
res = [("Dave",12,130),("Dave",12,121),("Dave",12,114),("Dave", 11, 130),("Zara",56,117),("Zara",45,117),("Matt",36,117)]
print(sorted(res, key=itemgetter(0, 1, 2)))
"""

"""
# Uncomment if needed, and move upper: distincive sorting
print ("Tuples are sorted according to NAME:")
print (sorted(res, key=itemgetter(0)))
print ("Tuples are sorted according to AGE:")
print (sorted(res, key=itemgetter(1)))
print ("Tuples are sorted according to HEIGHT:")
print (sorted(res, key=itemgetter(2)))
print (res)
"""
