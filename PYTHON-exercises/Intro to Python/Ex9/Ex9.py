# ============================= #
# EX 9: Classes                 #
# Konstantin Masich 326893955   #
# VM: Ubuntu 16.10 x64 Python 3 #
# ============================= #

# Data about amount of seats was taken from Internet. Since every plane has Business
# and Economy type seats and various seats schemes, I simplified it to have only
# one seat type:
# 	A319 has 28 rows and 6 seats in each row (168 seats total)
#   777-200 has 4o rows and 10 seats in each row (400 seats total)

class Flight(object):
	"Describes a particular flight"
	# Class attributes:
	# number      - Flight number like BA758
	# aircraft    - Plane type like AirbusA319 or Boeing777
	# seats       - A dictionary that stores "seat-passenger" pairs
	# total_seats - Total amount of seats
	# taken_seats - Amount of taken seats
		
	def __init__(self, flight_num, flight_type):
		self.number   = flight_num
		self.aircraft = flight_type
		self.taken_seats = 0
		self.seats = {}
		# Setting number of seats and seats dictionary
		if (self.aircraft == "AirbusA319"):
			self.total_seats = 168
		else:
			self.total_seats = 400
			
	def add_passenger(self, place, name):
		self.seats[place] = name
		self.taken_seats += 1
		
	def replace_passenger(self, old_place, new_place):
		name = self.seats[old_place]
		del self.seats[old_place]
		self.seats[new_place] = name
		
	def print_free_seats_number(self):
		print("Free places: ", self.total_seats - self.taken_seats)
		
	def print_tickets(self):
		print("\n================= ALL TICKETS: =================")
		print(" == NAME == FLIGHT NUMBER == SEAT == AIRCRAFT ==")
		temp = [(k, self.seats[k]) for k in sorted(self.seats, key=self.seats.get)]
		for key, val in temp:
			print(" ", val, "    ", self.number, "       ", key, "  ", self.aircraft)


# Uncomment if needed: sample test

"""
# Creating a flight
f1 = Flight("AB564", "AirbusA319")
# Adding passengers
f1.add_passenger("3F", "Zack Koe")
f1.add_passenger("1A", "John Doe")
f1.add_passenger("2A", "Dave Moe")
f1.add_passenger("4C", "Matt Zoe")
f1.add_passenger("3B", "Abby Boe")
print("Before replacing passengers:\n", f1.seats)
# Replacing passengers
f1.replace_passenger("2A", "14D")
f1.replace_passenger("4C", "16E")
print("After replacing passengers:\n", f1.seats)
# Printing tickets
f1.print_tickets()
# Printing amount of avaliable seats
print()
f1.print_free_seats_number() # Should be 168-5=163
"""
