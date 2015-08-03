#!/usr/bin/python


import sys
import csv
import datetime

class ShowTotals(object) :
    #get rolls from results file
    #show results
    #clear the screen???

    def getResults(self):
        dict = {}
        numTosses=0
        fkey=0
        rolled=0
        dt=""
        for key, val in csv.reader(open("RollResults.csv")):
            dict[key] = val
            print val
        #numTosses=len(dict)    
        #while numTosses != 0 :
        #    fkey += 1
        #    values=dict[fkey].values()
        #    numTosses -= 1
        #    print val