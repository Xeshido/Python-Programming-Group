### Put your code here

def writeToFile (fAccNo, fName, fPin, balance, filename):
    with open(filename, "a") as f:
        line = f"{fAccNo}{fName}{fPin}{balance}"
        f.write(f"{line}\n")

def checkDuplicate (fAccNo, filename):
    with open(filename, "r") as f:
        while(True):
            line = f.readline()
            if not line:
                break
            accNo = line[:5].strip()  # Retrieve account number
            if (accNo == fAccNo):
                return True
            
def inputInfo(filename):
    accNo = input("\nEnter account number: ")
    if (checkDuplicate(accNo, filename)):
        print("Account already exists. Please try again")
        inputInfo(filename)
        return

    name = input("Enter account name: ")
    pin = input("Enter account pin: ")
    balance = float(input("Enter balance: "))

    #Set field length for each string variable
    fAccNo = f"{accNo[:5]:<{5}}"   
    fName = f"{name[:30]:<{30}}"
    fPin = f"{pin[:4]:<{4}}"
    
    writeToFile(fAccNo, fName, fPin, balance, filename)

# main
f = open("Accounts.txt", "a")

while True:
    inputInfo("Accounts.txt")

    choice = input("\nEnter another [Y/N]? ").lower()

    while choice!= 'y' and choice!='n':
        print("Invalid")
        choice = input("\nEnter another [Y/N]? ").lower()
    if choice == 'n':
        print("End of Program")
        break





"""Write a program that will simulate the opening of account in a bank. You are to 
create first a structure with 4 members -- (1) an array of characters with 5 
elements for the ACCOUNT NUMBER, (2) an array of characters with 30 
elements for the ACCOUNT NAME, (3) an array of characters with 4 elements 
for the PIN, and (4) floating value for the initial BALANCE (Initial Deposit).

The program will allow the user (Teller) to input the depositor’s unique record 
for the structure, and will store it to a text file named “Accounts.txt”. Unique 
record means that the program should check if the inputted Account Number 
already exists. The program should not allow the user to input the same account 
number. 

Sample Run:
Enter Account Number: 14344
Enter Account Name: Rachel A. Nayre
Enter PIN: 9546
Enter Initial Balance: 50000

Create another account [Y/N]: Y

Enter Account Number: 14344
“Account Already Exist! “ Please try again…

Enter Account Number: 14355
Enter Account Name: Marlon B. Nayre
Enter PIN: 9546
Enter Initial Balance: 50000

Create another account [Y/N]: N 
“End of Program”


"""