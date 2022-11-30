from datetime import datetime

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

from tkinter import *

# Ticketing Program Homework practice 

# Introduction 

# Create a program in python that can simulate a ticketing system for Adventure Theme Park, the python application will ask the user the list of questions below before calculating their total charge. 
# Provide a welcome message 
print("Welcome to Adventure Theme Park! How can I help?")

# Display the entrance ticket prices 
price = {"adult":20, "children":12, "senior":11}
print(f"Entry ticket prices cost: {price}, respectively.")

# Ask how many adult tickets are required 
# Ask how many child tickets are required 
# Ask how many senior citizen tickets are required 
print(f"Which type of ticket would you like to purchase?")


for i in range(3):
    typeOfTicket = input("Enter type of ticket: ")
    if typeOfTicket == "adult" or typeOfTicket == "children" or typeOfTicket == "senior":
        print(f"You want {typeOfTicket} tickets.")
    
        while True:
            try:
                print("How many would you like?")
                amountOfTickets = int(input("Number of Tickets: "))
            except ValueError:
                print("Please say an integer.")
                continue
            else:
                break
        if amountOfTickets > 0:
            print(f"You want {amountOfTickets} tickets.")
        else:
            print("Please say an integer.")

        # Ask for the lead booker surname (for the ticket)
        print("Who is the lead booker?")
        fname = input("Input lead booker first name: ")
        lname = input("Input lead booker last name: ")
        leadBooker = fname + " " + lname
        print(f"Lead Booker: {leadBooker}.")

        # Ask if they require a parking pass for the car park
        # Print a car parking pass (if requested) 
        print("Do you require a parking pass for your car?")
        parkingPass = input("Yes = Parking Pass No = Parking Pass: ").lower()
        if parkingPass == "yes":
            print("You need a parking pass.")
        else:
            print("You do not need a parking pass.")
            
        # Add the total number of tickets to display the total cost 
        totalAdultPrice = amountOfTickets*price["adult"]
        totalChildrenPrice = amountOfTickets * price['children']
        totalSeniorPrice = amountOfTickets * price['senior']
        if typeOfTicket == "adult" and amountOfTickets > 0:
            print(f"As the price of an adult ticket is {price['adult']} and you want {amountOfTickets} tickets, the total cost of your ticket(s) are £{totalAdultPrice}.")
        elif typeOfTicket == "children" and amountOfTickets > 0:
            print(f"As the price of an children ticket is {price['children']} and you want {amountOfTickets} tickets, the total cost of your ticket(s) are £{totalChildrenPrice}.")
        elif typeOfTicket == "senior" and amountOfTickets > 0:
            print(f"As the price of an children ticket is {price['senior']} and you want {amountOfTickets} tickets, the total cost of your ticket(s) are £{totalSeniorPrice}.")
        else:
            print("Sorry, let me try to recalculate your total cost.")
            break

        # Print a ticket (display lead booker surname, tickets purchased, today’s date*)
        # Print a car parking pass (if requested)  
        today = datetime.today()
        print("----------------------------------------------------------------------------------------")
        print("                                Adventure Theme Park Ticket")
        print("----------------------------------------------------------------------------------------")
        print(f"Ticket Purchased By:{Fore.RED}{Back.WHITE}{leadBooker}")
        print("----------------------------------------------------------------------------------------")
        print(f"Type of Ticket(s) Purchased: {Fore.RED}{Back.WHITE}{typeOfTicket}{Back.BLACK}")
        print("----------------------------------------------------------------------------------------")
        print(f"Date Purchased On:{Fore.RED}{Back.WHITE}{today}{Back.BLACK}")
        print("----------------------------------------------------------------------------------------")
        print(f"Parking Request: {Fore.RED}{Back.WHITE}{parkingPass}{Back.BLACK}")
        print("----------------------------------------------------------------------------------------")
        while True:
            if parkingPass == "yes":
                print(f"{Back.WHITE}Parking request granted. This is your parking pass ticket.{Back.BLACK}")
                print("----------------------------------------------------------------------------------------")
                break
            else:
                print(f"You did not ask for a parking request. Please ask for help if you need one.")
                print("----------------------------------------------------------------------------------------")
                break
        print(f"{Back.WHITE}Thank you for purchasing with Adventure Theme Park. Please come again!")
        print("----------------------------------------------------------------------------------------")    
        break

    else:
        print("Sorry, what type of tickets did you want? The options are adult, children or senior tickets.")
        continue
        


# Use data validation techniques to avoid runtime errors through incorrect data entry  

# Thank the customer for their purchase 

# *You will need to investigate how to add today's date to the ticket.  

 

# Entrance ticket type example 

# Adult			£20 

# Child			£12 

# Senior citizen		£11 

 

# Parking 

# Free (car pass must be displayed/printed if yes is selected) 

# Design 

# Use pseudocode to design your program 

# Think carefully about what will be needed in the main program and in each subroutine/function. 

 

 

# *You will need to research how to add today's date to the ticket (Hint: import datetime or date).  