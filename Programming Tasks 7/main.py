from denominations import calculate_denominations, display_denominations

def get_amount():
    while True:
        try:
            amount = int(input("Input Amount: "))
            if amount < 0:
                print("Amount must be a positive integer.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def repeat_program():
    while True:
        try:
            repeat = input("Enter More [Y/N]? ").strip().upper()
            if repeat != 'Y' and repeat != 'N':
                raise ValueError
            else:
                return repeat
        except ValueError:
            print("Invalid input. Please enter 'Y' or 'N'.")

def main():
    while True:
        try:
            amount = get_amount()
            counts = calculate_denominations(amount)
            display_denominations(amount, counts)
            repeat = repeat_program()
            if repeat == 'N':
                break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()