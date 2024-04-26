def amountConversion (conversions, amount, bill = 1000):  # Function that process the amount to 
    if bill < 1: # base
        return 
    
    if amount >= bill: 
        conversions[bill] = amount//bill  #Adds the conversion for 1000(key) as its value in the dictionary
        amount -= (amount//bill) * bill # Updates amount

        # Calls the function recursively with the updated bill value
        if bill == 500 or bill == 5: amountConversion(conversions, amount, bill-4*(bill//5))   
        elif bill == 50: amountConversion(conversions, amount, bill-30)
        else: amountConversion(conversions, amount, bill//2)  
    else:
        setBill(conversions, amount, bill)
        
def setBill (conversions, amount, bill): # Function that ensures bill is less than the amount given by user
    # Calls the function recursively with the updated bill value
    if bill == 500 or bill == 5: amountConversion(conversions, amount, bill-4*(bill//5))
    elif bill == 50: amountConversion(conversions, amount, bill-30)
    else:amountConversion(conversions, amount, bill//2)


while True: 
    try:       
        amount = int(input("\nInput Amount: "))
        conversions = {} # Dictionary to store the conversions
        amountConversion(conversions, amount) # Function call

        print("Denominations: ")
        for x,y in conversions.items():  # Displays the conversions
            print("\t", x, "-", y)

        choice = input("\nEnter More [Y/N]? ").upper()
        while choice != 'Y' and choice != 'N':
            print("Invalid input!")
            choice = input("Enter more? [Y/N]: ") # Aks user repeatedly until user enters valid input
        if choice == 'Y': # Continues loop
            continue
        elif choice== 'N': # Exits loop
            break
    except Exception as e:
        print(e)






