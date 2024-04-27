# Constants
DEMAND_CHG = 35.00  # basic water demand charge
PER_1000_CHG = 1.10  # charge per thousand gallons used
LATE_CHG = 2.00  # surcharge on an unpaid balance

# Inputs
print(" =================================")
print("||       WATER BILL PROGRAM       ||")
print(" =================================")
unpaid = float(input("Enter unpaid balance> Php"))
previous = int(input("Enter previous meter reading> "))
current = int(input("Enter current meter reading> "))
print(" =================================")

# Calculations
use_charge = (current - previous) * PER_1000_CHG
late_charge = LATE_CHG if unpaid > 0 else 0
bill = DEMAND_CHG + use_charge + unpaid + late_charge

# Output
print(" =================================")
print("||             BILL              ||")
print(" =================================")
print(f"Bill includes Php{late_charge:.2f} late charge on unpaid balance of Php{unpaid:.2f}")
print(f"Total Due = Php{bill:.2f}")
print(" =================================")

