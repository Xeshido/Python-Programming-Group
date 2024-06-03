# Aldas, Dominic Syd
# Caldejon, Christian Angelo
# Llovit, Jhanna
# Okol, Arcangel

import os

# Function to write account information to the file
def writeToFile(fAccNo, fName, fPin, balance, filename):
    with open(filename, "a") as f:
        line = f"{fAccNo:<5}{fName:<30}{fPin:<4}{balance:.2f}"
        f.write(f"{line}\n")

# Function to check for duplicate account numbers
def checkDuplicate(fAccNo, filename):
    if not os.path.exists(filename):
        return False
    with open(filename, "r") as f:
        while (True):
            line = f.readline()
            if not line:
                break
            accNo = line[:5].strip()  # Retrieve account number
            if (accNo == fAccNo):
                return True
    return False

# Function to input new account information
def inputInfo(filename):
    accNo = input("\nEnter account number: ")
    if (checkDuplicate(accNo, filename)):
        print("Account already exists. Please try again")
        return

    name = input("Enter account name: ")
    pin = input("Enter account pin: ")
    balance = float(input("Enter balance: "))

    # Set field length for each string variable
    fAccNo = f"{accNo[:5]:<{5}}"
    fName = f"{name[:30]:<{30}}"
    fPin = f"{pin[:4]:<{4}}"

    writeToFile(fAccNo, fName, fPin, balance, filename)

# Function to read accounts from file
def read_accounts(filename):
    if not os.path.exists(filename):
        # Create the file if it does not exist
        with open(filename, "w") as f:
            pass  # Just create an empty file
        return {}

    accounts = {}
    with open(filename, "r") as f:
        for line in f:
            accNo = line[:5].strip()
            name = line[5:35].strip()
            pin = line[35:39].strip()
            balance = float(line[39:].strip())
            accounts[accNo] = {'name': name, 'pin': pin, 'balance': balance}
    return accounts

# Function to write accounts to file
def write_accounts(accounts, filename):
    with open(filename, "w") as f:
        for accNo, info in accounts.items():
            line = f"{accNo:<5}{info['name']:<30}{info['pin']:<4}{info['balance']:.2f}\n"
            f.write(line)

# Function to simulate ATM operations
def atm_simulation(filename):
    attempts = 0
    accounts = read_accounts(filename)

    while attempts < 3:
        accNo = input("Enter Account Number: ").strip()
        if accNo in accounts:
            pin_attempts = 0
            while pin_attempts < 3:
                pin = input("Enter PIN: ").strip()
                if pin == accounts[accNo]['pin']:
                    print("Welcome to PUP On-Line Banking Systems")
                    while True:
                        print("\n1. Balance Inquiry\n2. Deposit\n3. Withdraw\n4. Cancel")
                        try:
                            choice = int(input("Press the desired transaction: "))
                            if choice == 1:
                                print(f"Your Balance is P{accounts[accNo]['balance']}")
                            elif choice == 2:
                                try:
                                    amount = float(input("Enter Amount to Deposit: "))
                                    accounts[accNo]['balance'] += amount
                                    write_accounts(accounts, filename)
                                    print(f"New Balance is P{accounts[accNo]['balance']}")
                                except ValueError:
                                    print("Invalid amount. Please enter a valid number.")
                            elif choice == 3:
                                try:
                                    amount = float(input("Enter Amount to Withdraw: "))
                                    if amount > accounts[accNo]['balance']:
                                        print("Insufficient funds.")
                                    else:
                                        accounts[accNo]['balance'] -= amount
                                        write_accounts(accounts, filename)
                                        print(f"New Balance is P{accounts[accNo]['balance']}")
                                except ValueError:
                                    print("Invalid amount. Please enter a valid number.")
                            elif choice == 4:
                                print("Transaction Cancelled. Thank you for using PUP On-Line Banking Systems.")
                                break
                            else:
                                print("Invalid choice. Please select a valid transaction.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    break
                else:
                    pin_attempts += 1
                    if pin_attempts < 3:
                        print("Incorrect PIN. Please try again.")
                    else:
                        print("Too many incorrect PIN attempts. Exiting.")
                        return
            break
        else:
            attempts += 1
            if attempts < 3:
                print("Sorry, the Account doesn't exist!")
            else:
                print("Too many incorrect account number attempts. Exiting.")
                return

# Main function to integrate account creation and ATM simulation
def main():
    filename = "Accounts.txt"

    while True:
        print("\n1. Create Account\n2. Use ATM\n3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            inputInfo(filename)
        elif choice == '2':
            atm_simulation(filename)
        elif choice == '3':
            print("End of Program")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
