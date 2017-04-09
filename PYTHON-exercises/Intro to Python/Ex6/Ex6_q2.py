# ============================= #
# EX 6, Q2: infinite Fibonacci  #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

# Notation: result = p + q, where p is pre-previous member of sequence, q is
# previous one, and result is the current one.
def fibonacci_generator():
	p = 0
	q = 1
	while True:
		res = p + q
		p = q
		q = res
		yield res

for item in fibonacci_generator():
	print(item)
	
	# Uncomment to stop at specific value:
	#if item > 11000:
	#	break
