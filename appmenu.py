#!/usr/bin/python
# imported miscellaneous operating system for open and reading files
import os
# imported dice roll functions
import diceroller
# imported save totals function
import showtotals

class AppMenu(object) :
    def start(self) :

        # clears python window
        os.system('clear')

        menuOption = -1
        diceRoller = diceroller.DiceRoller()

        showTotals = showtotals.ShowTotals()
        while menuOption != 0 :
            print '\n' + '=' * 29 #this creates a border
            print "Welcome to Super Awesome Dice"
            print '=' * 29  #creates second border
            print """
            Please make your selection:\n
            1.) Roll Dice
            2.) Show Totals
            0.) Exit Program
            """
            menuOption = raw_input("> ")
            menuOption = int(menuOption) # connects user input with menu options

            #if user selects 1, the module diceRoller will begin
            if menuOption == 1 :
                diceRoller.rollDice()
            # if user selects 2, the showTotals module will begin, and save on the RollResults.csv
            elif menuOption == 2 :
                showTotals.getResults()
            # program will exit
            elif menuOption == 0 :
                print "Exiting program...\n"
                break
            # if the user input's neither 1, 2 or 0, the program will ask again for user's input
            else :
                print "Please make a valid selection"
