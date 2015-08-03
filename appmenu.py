#!/usr/bin/python

import os
import diceroller
import showtotals

class AppMenu(object) :
    def start(self) :

        os.system('clear')

        menuOption = -1
        diceRoller = diceroller.DiceRoller()
        showTotals = showtotals.ShowTotals()
        while menuOption != 0 :
            print '\n' + '=' * 29
            print "Welcome to Super Awesome Dice"
            print '=' * 29
            print """
            Please make your selection:\n
            1.) Roll Dice
            2.) Show Totals
            0.) Exit Program
            """
            menuOption = raw_input("> ")
            menuOption = int(menuOption)

            if menuOption == 1 :
                diceRoller.rollDice()
            elif menuOption == 2 :
                showTotals.getResults()
            elif menuOption == 0 :
                print "Exiting program...\n"
                break
            else :
                print "Please make a valid selection"

