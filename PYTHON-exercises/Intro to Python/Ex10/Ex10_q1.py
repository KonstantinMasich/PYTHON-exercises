# ============================= #
# EX 10, Q1: Exceptions         #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

# EXCEPTIONS
# I added an new exception (SeatException) and processed built-in exceptions AttributeError
# and KeyError. AttributeError is raised when Flight object was not instantiated properly
# and thus has not all of the attributes.

# Data about amount of seats was taken from Internet. Since every plane has Business
# and Economy type seats and various seats schemes, I simplified it to have only
# one seat type:
# 	A319 has 28 rows and 6 seats in each row (168 seats total)
#   777-200 has 4o rows and 10 seats in each row (400 seats total)

class SeatException(Exception):
	"Should be thrown when seat is already taken"
	pass

class Flight(object):
	"Describes a particular flight"
	# Class attributes:
	# number      - Flight number like BA758
	# aircraft    - Plane type like AirbusA319 or Boeing777
	# seats       - A dictionary that stores "seat-passenger" pairs
	# total_seats - Total amount of seats
	# taken_seats - Amount of taken seats
		
	def __init__(self, flight_num, flight_type):
		self.number = flight_num
		# CHECK: Empty string
		if not self.number:
			print("Error: illegal flight number!")
			return
		self.aircraft = flight_type
		# CHECK: Illegal aircraft type
		if self.aircraft!="AirbusA319" and self.aircraft!="Boeing777":
			print("Error: illegal aircraft type!")
			return	
		self.taken_seats = 0
		self.seats = {}
		# Setting number of seats and seats dictionary
		if (self.aircraft == "AirbusA319"):
			self.total_seats = 168
		else:
			self.total_seats = 400
			
	def add_passenger(self, place, name):
		# CHECK: empty passanger place or name
		if not name or not place:
			print("Error: passanger place and place must not be empty!")
			return
		try:
			# CHECK: seat is already taken
			if place in self.seats:
				print("Error: seat", place, "is already taken!")
				raise SeatException
		except SeatException:
			print ("EXCEPITON: add_passenger --> SeatException raised")
			return
		except AttributeError:
			print("EXCEPITON: add_passenger --> AttributeError raised")
			return
		try:
			self.seats[place] = name
			self.taken_seats += 1
		except KeyError:
			print("EXCEPITON: add_passenger --> KeyError raised")
			
	def replace_passenger(self, old_place, new_place):
		# CHECK: empty places
		if not old_place or not new_place:
			print("Error: old and new place must not be empty!")
			return
		try:
			if (new_place in self.seats):
				print("Error: seat", new_place, "is already taken by another passenger!")
				raise SeatException
		except SeatException:
			print ("EXCEPITON: replace_passenger --> SeatException raised")
			return
		except AttributeError:
			print("EXCEPITON: replace_passenger --> AttributeError raised")
			return
		name = self.seats[old_place]
		del self.seats[old_place]
		self.seats[new_place] = name
		
	def print_free_seats_number(self):
		try:
			print("Free places: ", self.total_seats - self.taken_seats)
		except AttributeError:
			print("EXCEPITON: print_free_seats_number --> AttributeError raised")
		
	def print_tickets(self):
		try:
			print("\n================= ALL TICKETS: =================")
			print(" == NAME == FLIGHT NUMBER == SEAT == AIRCRAFT ==")
			temp = [(k, self.seats[k]) for k in sorted(self.seats, key=self.seats.get)]
			for key, val in temp:
				print(" ", val, "    ", self.number, "       ", key, "  ", self.aircraft)
		except AttributeError:
			print("EXCEPITON: print_tickets --> AttributeError raised")

# Uncomment if needed: sample test
"""
# Bad object instantiation
f2 = Flight("", "Boeing777")

# Errors:
f2.add_passenger("1A", "John") # Should raise ATTRIBUTE ERROR
f2.print_free_seats_number()   # Should raise ATTRIBUTE ERROR
print("\n")

# Errors:
f1 = Flight("AB345", "AirbusA319")
f1.add_passenger("3F", "Zack Koe")
f1.add_passenger("1A", "John Doe")
f1.add_passenger("1A", "Dave Moe") # Should raise SEAT EXCEPTION because 1A is a taken seat
f1.replace_passenger("1A", "3F")   # Should raise SEAT EXCEPTION because 3F is a taken seat
"""
