
def display_menu():
    print("A – ADD\tD - DELETE\tE – EDIT\tT - TRANSACT\tX - EXIT")

def get_product_data():
    product_code = input("PRODUCT CODE: ")
    product_name = input("PRODUCT NAME: ")
    quantity = input("QUANTITY: ")
    return f"{product_code},{product_name},{quantity}\n"

def add_product():
    with open("Products.txt", "a") as file:
        while True:
            product_data = get_product_data()
            file.write(product_data)
            more = input("Enter more? [Y/N]: ").upper()
            if more != 'Y':
                break

def delete_product():
    product_code = input("Enter PRODUCT CODE to delete: ")
    found = False
    with open("Products.txt", "r") as file:
        lines = file.readlines()
    with open("Products.txt", "w") as file:
        for line in lines:
            if line.startswith(product_code + ", "):
                found = True
                print(f"Record found: {line.strip()}")
                confirm = input("Do you want to delete this record? [Y/N]: ").upper()
                if confirm != 'Y':
                    file.write(line)
            else:
                file.write(line)
    if not found:
        print("Record not found")

def edit_product():
    product_code = input("Enter PRODUCT CODE to edit: ")
    found = False
    with open("Products.txt", "r") as file:
        lines = file.readlines()
    with open("Products.txt", "w") as file:
        for line in lines:
            if line.startswith(product_code + ", "):
                found = True
                print(f"Record found: {line.strip()}")
                new_data = get_product_data()
                file.write(new_data)
            else:
                file.write(line)
    if not found:
        print("Record not found")

def transact_product():
    product_code = input("Enter PRODUCT CODE to transact: ")
    found = False
    with open("Products.txt", "r") as file:
        lines = file.readlines()
    with open("Products.txt", "w") as file:
        for line in lines:
            if line.startswith(product_code + ", "):
                found = True
                parts = line.strip().split(", ")
                print(f"Record found: {line.strip()}")
                transaction_code = input("TRANSACTION CODE [P/S]: ").upper()
                quantity = int(input("QUANTITY: "))
                if transaction_code == 'P':
                    parts[2] = str(int(parts[2]) + quantity)
                elif transaction_code == 'S':
                    parts[2] = str(int(parts[2]) - quantity)
                file.write(",".join(parts) + "\n")
            else:
                file.write(line)
    if not found:
        print("Record not found")

def main():
    try:
        while True:
            display_menu()
            choice = input("WHAT DO YOU WANT TO DO? ").upper()
            if choice == 'A':
                add_product()
            elif choice == 'D':
                delete_product()
            elif choice == 'E':
                edit_product()
            elif choice == 'T':
                transact_product()
            elif choice == 'X':
                print("Updated file contents:")
                with open("Products.txt", "r") as file:
                    print(file.read())
                print("End of program")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
