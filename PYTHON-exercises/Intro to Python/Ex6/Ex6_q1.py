# ============================= #
# EX 6, Q1: distinct generator  #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

# Change these as you see fit
items = [3,6,6,2,1,1]
NUM_OF_VALUES = 4


def take(count, iterable):
    "Take first count elements"
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item
		
# I did not quite understand the task so I tried to make it in 2
# options, I hope one of them was what you meant...

# Please notice that order is not preserved: for 3,6,6,2,1,1 and
# num=3 it will return 1,2,3 and not 3,6,2. For num=1 the result
# will be 1, and for num=4 it will be 1,2,3,6.
# But that is not important, right? The task was just to get
# distinct values, the order was not important as I understand.
# This allows me to simply use set().
		
# Option 1
def dist_vals(count, iterable):
	dist = set(iterable)
	counter = 0
	for item in dist:
		if counter == count:
			return
		counter += 1
		yield item

def run_take():
	for item in take(NUM_OF_VALUES, dist_vals(NUM_OF_VALUES,items)):
		print(item)
		
# Option 2 - simply use run_take2() instead of run_take() at line 57

# This returns a generator object!
def dist_vals2(iterable):
	yield set(iterable)
		
def run_take2():
	for gen in dist_vals2(items):
		for item in take(NUM_OF_VALUES, gen):
			print(item)
	
if __name__== '__main__':
    run_take()
