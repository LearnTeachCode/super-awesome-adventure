#!/usr/bin/python

import random
import os

class DiceRoller(object) :


    def rollDice(self):
                print """
                Enter the type of die you would like to roll:\n* d2\n* d4\n* d6\n* d8\n* d10\n* d20
                """
                diceType = raw_input("> ")
                print "How many times would you like to roll?\n"

                diceRoll = raw_input("> ")

                diceType = str.lower(diceType)
                diceRoll = int(diceRoll)
                diceTotal = 0

                while diceRoll != 0 :
                    if diceType == 'd2' :
                        coin = random.randint(1, 2)
                        if coin == 1 :
                            print "Heads"
                        else :
                            print "Tails"

                    elif diceType == 'd4' :
                        print random.randint(1, 4)

                    elif diceType == 'd6' :
                        print random.randint(1, 6)

                    elif diceType == 'd8' :
                        print random.randint(1, 8)

                    elif diceType == 'd10' :
                        print random.randint(1, 10)

                    elif diceType == 'd20' :
                        print random.randint(1, 20)

                    else :
                        print "Your dice type was invalid. Please try again."

                    diceRoll = diceRoll - 1

    def startMenu(self) :

            os.system('clear')

            menuOption = -1

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
                    self.rollDice()
                elif menuOption == 2 :
                    pass
                elif menuOption == 0 :
                    print "Exiting program...\n"
                    break
                else :
                    print "Please make a valid selection"

runProg = DiceRoller()
runProg.startMenu()
