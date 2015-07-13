#!/usr/bin/python

import random
import numbers

class DiceRoller(object) :

    def verifyDiceType(self):
                diceTypes=["d2","d4","d6","d8","d10","d20"]
                diceType=""
                while diceType not in diceTypes:
                    print " Enter the type of die you would like to roll: [ d2, d4, d6, d8, d10, d20] "
                    diceType = raw_input("> ")
                    diceType = str.lower(diceType)
                return diceType

    def numberOfRolls(self):
        while True:
            try:
                print "How many times would you like to roll?\n"
                diceRoll = int(raw_input("> "))
            except ValueError:
                print "Error!"
                continue
            else:
                print diceRoll
                return diceRoll
                break
                    
    def rollDice(self):                
                diceType=self.verifyDiceType()
                diceRoll=self.numberOfRolls()
                
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

                    diceRoll = diceRoll - 1
