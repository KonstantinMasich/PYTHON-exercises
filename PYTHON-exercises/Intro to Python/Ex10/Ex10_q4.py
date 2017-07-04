def sqrt(x):
	'''
	Compute square roots using the method of Heron of Alexandria.
	Args:
		x: The number for which the square root is to be computed.
	Returns:
		The square root of x.
	Raises:
		ZeroDivisionError: in case of x=-1.
	'''
	
	guess = x
	i = 0
	try:
		while guess * guess != x and i < 20:
			guess = (guess + x / guess) / 2.0
			i += 1
	except ZeroDivisionError:
		print("EXCEPTION: sqrt(x) --> ZeroDivisionError raised")
		print("Argument provided:", x)
	return x


def main():
	print(sqrt(9))
	print(sqrt(2))
	print(sqrt(-1))
	
	# As I see, error is raised only if x=-1.
	print("\n Test: \n")
	for i in range(10000,-10000,-1):
		sqrt(i) # Error is raised only when i=-1

if __name__ == '__main__':
	main()
