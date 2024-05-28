### Put your code here

"""
Modify #1 in which the program will simulate the ATM.

The program will ask the depositor to input an ACCOUNT NUMBER, the 
program will then searches the account number from the “Accounts.txt” file, if the 
account number exists, then the program will then ask for the depositor’s PIN; 
otherwise, the program will inform the user that the account does not exist. Note: 
The user will only allowed to input up to 3 incorrect account number, otherwise, 
the program will exit automatically.

The screen should look like this:

Enter Account Number: 14345
“Sorry the Account doesn’t exist!”

Enter Account Number: 14344
Enter PIN: 9546

After the depositor’s PIN has been inputted, the program will verify if the PIN 
inputted by the depositor is correct; otherwise, the program will exit 
automatically. 

If the depositor’s PIN was verified correctly, the screen will look like the 
following:

Welcome to PUP On-Line Banking Systems
1. Balance Inquiry
2. Deposit
3. Withdraw
4. Cancel

Press the desired transaction: 1

* If (1) was chosen, the latest balance from the file will be displayed: 

Output:
 Your Balance is P50000 

Note: Display again the option and input the desired transaction.
* If (2) was chosen, the program will ask the depositor how much he is going to 
deposit:

Output:
 Enter Amount: 50000

Note: The amount entered by the depositor will be added to his balance in the file.
 Display again the option and input the desired transaction.
* If (3) was chosen, the program will ask the depositor how much he is going to 
withdraw:

Output:
 Enter Amount: 50000

Note: The amount entered by the depositor will be subtracted from his balance in 
the file. Display again the option and input the desired transaction.

* If (4) was chosen, the program will terminate.

*Note: Please include try… except statemen

"""