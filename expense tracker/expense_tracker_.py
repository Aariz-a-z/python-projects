def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{category}\n")

    print("Expense added!")


def view_expenses():
    total = 0
    print("\n--- Expense List ---")
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category = line.strip().split(",")
                amount = float(amount)
                total += amount
                print(f"{category}: ₹{amount}")
        print("Total Expense: ₹", total)
    except FileNotFoundError:
        print("No expenses found.")


while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
