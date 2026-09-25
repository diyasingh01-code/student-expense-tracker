import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([date, category, description, amount])

    print("\nExpense added successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    print("\n----- All Expenses -----")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(
                f"{row['Date']} | "
                f"{row['Category']} | "
                f"{row['Description']} | "
                f"₹{row['Amount']}"
            )


def calculate_total():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expense: ₹{total:.2f}")


def category_summary():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\n----- Category Summary -----")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    while True:
        print("\n==============================")
        print("     STUDENT EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()