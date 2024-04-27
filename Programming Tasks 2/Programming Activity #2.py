def calculate_unit_type_and_price(area):
    if 28.5 <= area < 52.0:
        unit_type = "Studio Type"
        price_per_sqm = 65892.00
    elif 52.0 <= area < 86.5:
        unit_type = "2 Bedroom"
        price_per_sqm = 58807.00
    elif area >= 86.5:
        unit_type = "3 Bedroom"
        price_per_sqm = 53380.00
    else:
        unit_type = "Invalid Area"
        price_per_sqm = 0
    
    total_price = area * price_per_sqm
    return unit_type, price_per_sqm, total_price

def calculate_discount(down_payment, total_price, balance):
    if down_payment < 0.2 * total_price:
        discount_percentage = 0
    elif 0.2 * total_price <= down_payment < 0.3 * total_price:
        discount_percentage = 0.03
    elif 0.3 * total_price <= down_payment < 0.4 * total_price:
        discount_percentage = 0.04
    elif 0.4 * total_price <= down_payment:
        discount_percentage = 0.05
    else:
        discount_percentage = 000000000.000
    
    
    discount_amount = balance * discount_percentage
    return discount_percentage, discount_amount

def calculate_interest(years_to_pay, balance, discount_amount):
    if years_to_pay == 5:
        interest_rate = 0.04
    elif years_to_pay == 10:
        interest_rate = 0.06
    elif years_to_pay == 15:
        interest_rate = 0.08
    elif years_to_pay == 20:
        interest_rate = 0.1
    else:
        interest_rate == 0
    
    interest_amount = (balance - discount_amount) * interest_rate
    return interest_rate, interest_amount

def calculate_loan_details(area, down_payment, years_to_pay):
    unit_type, price_per_sqm, total_price = calculate_unit_type_and_price(area)
    balance = total_price - down_payment
    discount_percentage, discount_amount = calculate_discount(down_payment, total_price, balance)
    interest_rate, interest_amount = calculate_interest(years_to_pay, balance, discount_amount)
    contract_price = (balance - discount_amount) + interest_amount
    
    
    return unit_type, price_per_sqm, total_price, discount_percentage, discount_amount, balance, interest_rate, interest_amount, contract_price

def main():
    area = float(input("Area (in square meters): "))
    down_payment = float(input("Downpayment Amount: "))
    years_to_pay = int(input("Years to pay: "))

    unit_type, price_per_sqm, total_price, discount_percentage, discount_amount, balance, interest_rate, interest_amount, contract_price = calculate_loan_details(area, down_payment, years_to_pay)

    print("===================================================================")
    print("Area (in square meters):     |    ", "{:.2f}".format(area))
    print("Unit Type:                   |    ", unit_type)
    print("Price per Square Meter:      |    ", "{:.2f}".format(price_per_sqm))
    print("Total Unit Price:            |    ", "{:.2f}".format(total_price))
    print("===================================================================")
    print("===================================================================")
    print("Downpayment Amount:          |    ", "{:.2f}".format(down_payment))
    print("Down Payment in Percentage:  |    ", "{:.2%}".format(down_payment / total_price))
    print("Balance:                     |    ", "{:.2f}".format(balance))
    print("Discount:                    |    ", "{:.0%}".format(discount_percentage))
    print("Less: Discount Amount:       |    ", "{:.2f}".format(discount_amount))
    print("===================================================================")
    print("===================================================================")
    print("Years to Pay:                |    ", years_to_pay)
    print("Interest:                    |    ", "{:.0%}".format(interest_rate))
    print("Interest Amount:             |    ", "{:.2f}".format(interest_amount))
    print("Contract Price:              |    ", "{:.2f}".format(contract_price))
    print("===================================================================")
    

if __name__ == "__main__":
    main()