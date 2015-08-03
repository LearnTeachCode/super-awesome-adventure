#!/usr/bin/python

import random
import sys


class DiceRoller(object) :

    def verifyDiceType(self):
                diceTypes=["d2","d4","d6","d8","d10","d20"]
                diceType=""
                while diceType not in diceTypes:
                    print " Enter the type of die you would like to roll: [ d2, d4, d6, d8, d10, d20] "
                    diceType = raw_input("> ")
                    diceType = str.lower(diceType)
                return diceType

    def askNumTosses(self):
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

    # def roll_n_dice(self, numSides, numTosses):
    def roll_n_dice(self, numSides, numTosses):
                '''
                If numTosses is equal to 1, return a single number
                Else returns a list of size = numTosses

                singleToss = {
                date: "7/15/15 "
                type: "d20"
                value: ""
                }

                '''

                resultList = [random.randint(1, numSides) for i in range(0,numTosses)]

                return resultList

    def rollDice(self):
                #Take in what user input for dice type and converts the number of sides to an 'int'
                diceTypeStr = self.verifyDiceType()
                diceTypeInt = int(diceTypeStr[1:len(diceTypeStr)])
                # Takes in number of dice tosses
                numTosses = self.askNumTosses()
                print self.roll_n_dice(diceTypeInt, numTosses)

if __name__ == '__main__':

    quickroll = DiceRoller()
    print quickroll.roll_n_dice(int(sys.argv[1]),int(sys.argv[2]))
