#!/usr/bin/python

import random
import sys
import csv
import datetime

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
                #init
                results={}
                flist=[]
                fkey=0
                
                #Take in what user input for dice type and converts the number of sides to an 'int'
                diceTypeStr = self.verifyDiceType()
                diceTypeInt = int(diceTypeStr[1:len(diceTypeStr)])
                
                diceTotal = 0
                diceTypeFace=0
                diceTypeFace=diceTypeStr[1:]

                # Takes in number of dice tosses
                numTosses = self.askNumTosses()
                print self.roll_n_dice(diceTypeInt, numTosses)


                while numTosses != 0 :
                    fkey += 1
                    e =random.randint(1,int(diceTypeFace))
                    timestamp=datetime.datetime.now()
                    flist=[diceTypeStr,e,str(timestamp)]
                    results[fkey]=flist

                    numTosses -= 1

                print results
                saveToFile= csv.writer(open("RollResults.csv","w"))
                for key,val in results.items():
                    saveToFile.writerow([key,val])

if __name__ == '__main__':

    quickroll = DiceRoller()
    print quickroll.roll_n_dice(int(sys.argv[1]),int(sys.argv[2]))
