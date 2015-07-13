#!/usr/bin/python

import random

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
