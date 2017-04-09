# ============================= #
# EX 6, Q3: sum of primes       #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

# ========================================== #
# Both options need about 8-12 sec to work.. #
# ========================================== #

from math import sqrt
import time

# Prime checker from lection
def is_prime(x):
	if x<2:
		return False
	for i in range(2, int(sqrt(x))+1):
		if x%i==0:
			return False
	return True

# Option 1:
million_squares = (x*x for x in range(1,1000001) if is_prime(x))
start = time.time() # start measure
#---------------------------
sigma = 0
for x in million_squares:
	sigma += x
print(sigma)
#---------------------------
end = time.time() # stop measure
print(end - start)

# Option 2:
"""
million_squares = (x*x for x in range(1,1000001) if is_prime(x))
start = time.time() # start measure
#---------------------------
print(sum(list(million_squares)))
#---------------------------
end = time.time()   # stop measure
print(end - start)
"""
