def main():
    # Define prices per unit for each item
    prices = {
        "Paper": 1.00,
        "Pencil": 5.00,
        "Scissors": 25.00,
        "Eraser": 2.50
    }

    print("MATERIALS")
    print("-------------")
    print("Enter the Cost of the following:")
    for item, price in prices.items():
        print(f"{item} : P{price:.2f}")

    print("\nPURCHASE")
    print("--------")
    # Accept quantities bought per item
    quantities = {}
    for item, _ in prices.items():
        quantity = int(input(f"{item} : "))
        quantities[item] = quantity

    # Calculate total amount due
    total_amount_due = sum(prices[item] * quantities[item] for item in prices)

    # Display total price
    print(f"\nTHE TOTAL PRICE IS: P {total_amount_due:.2f}")

    # Accept cash amount given by customer
    cash_given = float(input("Enter Cash : P "))

    # Calculate change
    change = cash_given - total_amount_due

    print("\nOFFICIAL RECEIPT")
    print("--------------------")
    print("Paper : P {:.2f}".format(prices["Paper"] * quantities["Paper"]))
    print("Pencil : P {:.2f}".format(prices["Pencil"] * quantities["Pencil"]))
    print("Scissors : P {:.2f}".format(prices["Scissors"] * quantities["Scissors"]))
    print("Eraser : P {:.2f}".format(prices["Eraser"] * quantities["Eraser"]))
    print("--------------------")

    # Display total, cash given, and change
    print("Total : P {:.2f}".format(total_amount_due))
    print("Cash : P {:.2f}".format(cash_given))
    print("Change : P {:.2f}".format(change))

    # Calculate total number of items
    total_items = sum(quantities.values())
    print("No of Items : {}".format(total_items))

    # Calculate price before VAT and VAT amount
    price_before_vat = total_amount_due / 1.12
    vat_amount = total_amount_due - price_before_vat
    print("Price before VAT : P {:.2f} VAT : P {:.2f}".format(price_before_vat, vat_amount))

if __name__ == "__main__":
    main()
