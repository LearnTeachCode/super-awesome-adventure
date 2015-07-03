from tkinter import *
import random

class diceRoll:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton1 = Button(frame, text="Roll Die of 2", command=self.rollDice2)
        self.printButton2 = Button(frame, text="Roll Die of 4", command=self.rollDice4)
        self.printButton3 = Button(frame, text="Roll Die of 6", command=self.rollDice6)
        self.printButton4 = Button(frame, text="Roll Die of 8", command=self.rollDice8)
        self.printButton5 = Button(frame, text="Roll Die of 10", command=self.rollDice10)
        self.printButton6 = Button(frame, text="Roll Die of 12", command=self.rollDice12)
        self.printButton7 = Button(frame, text="Roll Die of 20", command=self.rollDice20)
        self.printButton8 = Button(frame, text="Roll Die of 100", command=self.rollDice100)

        self.printButton1.pack(side=LEFT)
        self.printButton2.pack(side=LEFT)
        self.printButton3.pack(side=LEFT)
        self.printButton4.pack(side=LEFT)
        self.printButton5.pack(side=LEFT)
        self.printButton6.pack(side=LEFT)
        self.printButton7.pack(side=LEFT)
        self.printButton8.pack(side=LEFT)

        bottomframe = Frame(root)
        bottomframe.pack(side = BOTTOM)

        self.quitButton = Button(bottomframe, text="Quit", command=frame.quit)
        self.quitButton.pack(side=BOTTOM)

        canvas = Canvas(bottomframe, width = 200, height = 100)
        canvas.pack(side=LEFT)

        greenBox = canvas.create_rectangle(30, 30, 120, 120, fill="darkgreen")
        blackdot = canvas.create_oval(60, 60, 60, 60, fill="black", width=20)
        roll = 1
        textRoll = canvas.create_text(100, 50, text="2")

    def rollDice2(self):
        roll = random.randint(1,2)
        print("You rolled a", roll, "congrats!")
    def rollDice4(self):
        roll = random.randint(1,4)
        print("You rolled a", roll, "congrats!")
    def rollDice6(self):
        roll = random.randint(1,6)
        print("You rolled a", roll, "congrats!")
    def rollDice8(self):
        roll = random.randint(1,8)
        print("You rolled a", roll, "congrats!")
    def rollDice10(self):
        roll = random.randint(1,10)
        print("You rolled a", roll, "congrats!")
    def rollDice12(self):
        roll = random.randint(1,12)
        print("You rolled a", roll, "congrats!")
    def rollDice20(self):
        roll = random.randint(1,20)
        print("You rolled a", roll, "congrats!")
    def rollDice100(self):
        roll = random.randint(1,100)
        print("You rolled a", roll, "congrats!")




root = Tk()
dice = diceRoll(root)
root.mainloop()