# ============================= #
# EX 10, Q2: String to Int      #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

def strToInt(number):
	try:
		num = int(number)
		return num
	except ValueError:
		print("Error: specified value is not numeric!")
		return None
		
def logarithm(number):
	num = strToInt(number)
	if num:
		import math
		return math.log(num, 10)
	else:
		return None
	
# Uncomment if needed: sample test
"""
print(logarithm("100")) # Should print 2.0
print(logarithm(10))    # Should print 1.0
print(logarithm('ABC')) # Should print error message and return None
print(logarithm(""))    # Should print error message and return None
"""
