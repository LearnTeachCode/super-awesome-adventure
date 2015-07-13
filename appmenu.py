#!/usr/bin/python

import os
import diceroller

class AppMenu(object) :
    def start(self) :

        os.system('clear')

        print '\n' + '=' * 29
        print "Welcome to Super Awesome Dice"
        print '=' * 29

        menuOption = -1
        diceRoller = diceroller.DiceRoller()

        while menuOption != 0 :
                print """
                Menu:\n
                1.) Roll Dice
                2.) Show Results
                0.) Exit
                """
                try:
                    menuOption = raw_input("> ")
                    menuOption = int(menuOption)

                    if menuOption == 1 :
                        diceRoller.rollDice()
                    elif menuOption == 2 :
                        pass
                    elif menuOption == 0 :
                        print "Exiting...\n"
                        break
                    else:
                        os.system('clear')
                        print "Please enter a valid selection"
                except ValueError:
                    os.system('clear')
                    print "Please enter a valid selection"
                    pass
