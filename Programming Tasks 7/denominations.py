
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

