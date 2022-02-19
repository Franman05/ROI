#We will continue practicing Object Oriented Programming in this assignment to become more fluent in Python. 
#Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.
#Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.

class  investment():
    def __init__(self,down_payments, closing_cost,fixes):
        self.down_payments = down_payments
        self.closing_cost = closing_cost
        self.fixes = fixes

    def mutiply(self):
        print("Income:",self.down_payments * self.closing_cost * self.fixes)

number = investment(10*10,2*10,1*10)
    
number.mutiply()

    
