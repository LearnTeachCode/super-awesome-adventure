#!/usr/bin/python

# the sys module provides access to some variable and functions
import sys
# The csv module implements classes to read and write tabular data in CSV format.
import csv
# The datetime module supplies classes for manipulating dates and times
import datetime

class ShowTotals(object) :
    #get rolls from results file
    #show results
    #clear the screen???

    def getResults(self):
        dict = {}
        numTosses=0 #how many tosses
        fkey=0  # user input to what type of die they want to roll
        rolled=0 # result of your roll
        dt="" # date and time
        for key, val in csv.reader(open("RollResults.csv")):
            dict[key] = val
            print val
        #numTosses=len(dict)
        #while numTosses != 0 :
        #    fkey += 1
        #    values=dict[fkey].values()
        #    numTosses -= 1
        #    print val
