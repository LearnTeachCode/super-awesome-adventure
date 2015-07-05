import random

# Function to roll default six-sided die and print the result
def roll_die():
	number = random.randint(1, 6)
	if number == 1:
		print "[--------------------]"
		print "[--------------------]"
		print "[---------O---------]"
		print "[--------------------]"
		print "[--------------------]"
	if number == 2:
		print "[--------------------]"
		print "[--------------------]"
		print "[-----O-------O----]"
		print "[--------------------]"
		print "[--------------------]"
	if number == 3:
		print "[--------------------]"
		print "[---------O---------]"
		print "[--------------------]"
		print "[----O--------O----]"
		print "[--------------------]"			
	if number == 4:
		print "[--------------------]"
		print "[-----O--------O---]"
		print "[---------------------]"
		print "[-----O-------O----]"
		print "[--------------------]"
	if number == 5:
		print "[--------------------]"
		print "[-----O--------O---]"
		print "[----------O--------]"
		print "[-----O-------O----]"
		print "[--------------------]"
	if number == 6:
		print "[--------------------]"
		print "[---O--------O-----]"
		print "[---O--------O-----]"
		print "[---O--------O-----]"
		print "[--------------------]"

# MAIN PROGRAM:
leave_program = 0
print "\nWelcome to the super awesome dice rolling program."
while leave_program != "q":	    
	numdice = raw_input("How many dice do you want to roll? Enter a number (Must be at least 1):\n>> ")
	numdice = int(numdice)	
	while numdice < 1:
		# TODO: catch errors if user didn't enter a number!	
		numdice = raw_input("Sorry, you can only roll 1 or more dice. Please re-enter the number of dice you want to roll:\n>> ")
		numdice = int(numdice)	
	rollcount = 1
	while rollcount <= numdice:
		print "\nRolling die #%d:" % rollcount
		roll_die()				
		rollcount += 1
	leave_program = raw_input("Type 'q' to quit, or press enter to start again.\n>> ")