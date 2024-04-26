# Aldas, Dominic Syd
# Caldejon, Christian Angelo
# Llovit, Jhanna
# Okol, Arcangel

def checkAvailability (day, month, daysMonths): # Function that checks date availability
    if day in daysMonths[month-1][1]:
        daysMonths[month-1][1].remove(day) # If date is available, it is removed from the list
        return True
    
    return False

# List to store days and months
days_months = [["January", list(range(1, 32))],  
               ["February",list(range(1, 30))], 
               ["March",list(range(1, 32))], 
               ["April",list(range(1, 31))], 
               ["May",list(range(1, 32))], 
               ["June",list(range(1, 31))],
               ["July",tuple(range(1, 32))], 
               ["August",list(range(1, 32))], 
               ["September",list(range(1, 31))], 
               ["October",list(range(1, 32))], 
               ["November",list(range(1, 31))], 
               ["December",list(range(1, 32))]]

#User input
while True: 
    monthIn = int(input("\nInput Month Code: "))
    dayIn = int(input("Input Day: "))
    


    print(f"\nYou have chosen: {days_months[monthIn-1][0]} {dayIn}, 2023 for your reservation") # Displays formatted date

    if (checkAvailability(dayIn, monthIn, days_months)): # Calls method checkAvailability 
        print("The chosen date is Available!")   # Executes when method returns true
    else:
        print("The chosen date is NOT Available!")

    choice = input("\nEnter another? [Y/N]: ").upper() # User input

    while choice != 'Y' and choice != 'N':
        print("Invalid input!")
        choice = input("Enter more? [Y/N]: ") # Aks user repeatedly until user enters valid input

    if choice == 'Y': # Continues loop
        continue
    elif choice== 'N': # Exits loop
        break


