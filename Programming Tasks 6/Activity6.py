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

def calculate_denominations(amount):
    denominations = [1000, 500, 100, 50, 20, 10, 5, 1]
    counts = []
    for denom in denominations:
        count = amount // denom
        counts.append(count)
        amount -= count * denom
    return counts

def display_denominations(amount, counts):
    print("Denominations:")
    denominations = [1000, 500, 100, 50, 20, 10, 5, 1]
    for i in range(len(denominations)):
        print(f"\t{denominations[i]:5} - {counts[i]:2}")
    print()

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
