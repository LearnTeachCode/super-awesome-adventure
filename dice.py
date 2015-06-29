leave_program = 0

while leave_program != "q":
    import random
    print "This is a dice rolling program"
    # will update this to allow user to roll multiple dice using a function, yayy!
	print "Press enter to roll"
    raw_input()
    number = random.randint(1, 6)
    if number == 1:
        print "[--------------------]"
        print "[--------------------]"
        print "[---------O---------]"
        print "[--------------------]"
        print "[--------------------]"
        print "Type 'q' to quit"
        leave_program = raw_input()
    if number == 2:
        print "[--------------------]"
        print "[--------------------]"
        print "[-----O-------O----]"
        print "[--------------------]"
        print "[--------------------]"
        print "Type 'q' to quit"
        leave_program = raw_input()
    if number == 3:
        print "[--------------------]"
        print "[---------O---------]"
        print "[--------------------]"
        print "[----O--------O----]"
        print "[--------------------]"
        print "Type 'q' to quit"
        leave_program = raw_input()
    if number == 4:
        print "[--------------------]"
        print "[-----O--------O---]"
        print "[---------------------]"
        print "[-----O-------O----]"
        print "[--------------------]"
        print "Type 'q' to quit"
        leave_program = raw_input()
    if number == 5:
        print "[--------------------]"
        print "[-----O--------O---]"
        print "[----------O--------]"
        print "[-----O-------O----]"
        print "[--------------------]"
        print "Type 'q' to quit"
        leave_program = raw_input()
    if number == 6:
        print "[--------------------]"
        print "[---O--------O-----]"
        print "[---O--------O-----]"
        print "[---O--------O-----]"
        print "[--------------------]"
        print "Type 'q' to quit"
        leave_program = raw_input()
