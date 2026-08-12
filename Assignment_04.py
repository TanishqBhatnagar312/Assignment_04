import csv
import os

FILE = "expenses.csv"

def init_file():
    """Check if the CSV file exists; if not, create it with the required schema header."""
    if not os.path.exists(FILE):  
        try:
            with open(FILE, "w", newline="") as f:  
                writer = csv.writer(f)  
                writer.writerow(["date", "category", "amount", "note"])  
        except Exception as e:
            print(f"Error initializing file: {e}")  


def get_amount():
    """Handles invalid numeric input gracefully by re-prompting the user."""
    while True:  
        raw = input("Amount: ")  
        try:
            amount = float(raw)  
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount  
        except ValueError:  
            print("Please enter a valid number, e.g., 199.50")  


def add_expense(date, category, amount, note=""):
    try:
        with open(FILE, "a", newline="") as f:  
            writer = csv.writer(f)  
            writer.writerow([date, category, amount, note])  
        print("Expense added successfully.")  
    except Exception as e:
        print(f"Failed to record expense: {e}")  


def view_expenses():
    """Reads all expense entries, displays them formatted, and shows total spent."""
    total = 0.0  
    try:
        with open(FILE, "r", newline="") as f:  
            reader = csv.reader(f)  
            header = next(reader, None)  

            count = 0
            print("\n" + "=" * 50)
            print(f"{'Date':12} | {'Category':10} | {'Amount (₹)':10} | Note")
            print("-" * 50)

            for date, category, amount, note in reader:  
                amt_val = float(amount)  
                total += amt_val  
                count += 1
                print(f"{date:12} | {category:10} | ₹{amt_val:<9.2f} | {note}")  

            print("-" * 50)
            if count == 0:
                print("No expenses recorded yet.")
            else:
                print(f"Total spent: ₹{total:.2f}")  
            print("=" * 50 + "\n")

    except FileNotFoundError:  
        print(f"The file {FILE} was not found. Starting fresh.")  
    except Exception as e:
        print(f"Error reading expenses: {e}")  


def category_summary():
    totals = {}  
    try:
        with open(FILE, "r", newline="") as f:  
            reader = csv.reader(f)  
            next(reader, None)  

            for _, category, amount, _ in reader:  
                totals[category] = totals.get(category, 0) + float(amount)  

        if not totals:
            print("\nNo expense records available to summarize.\n")
            return

        print("\n" + "=" * 30)
        print("Category Wise Summary")
        print("-" * 30)
        
        for cat, amt in sorted(totals.items(), key=lambda x: -x[1]):  
            print(f"{cat:12}: ₹{amt:.2f}")  
        print("=" * 30 + "\n")

    except FileNotFoundError:  
        print(f"The file {FILE} was not found.")
    except Exception as e:
        print(f"Error generating summary: {e}")  


def main():
    init_file()  

    while True:  
        print("\nExpense Tracker\n")  
        print("1. Add Expense")  
        print("2. View All Expenses")  
        print("3. Category Summary")  
        print("4. Exit")  

        choice = input("Enter choice: ").strip()  

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ").strip()  
            category = input("Category: ").strip()  
            amount = get_amount()  
            note = input("Note (optional): ").strip()  
            add_expense(date, category, amount, note)  
        elif choice == "2":
            view_expenses()  
        elif choice == "3":
            category_summary()  
        elif choice == "4":
            print("Goodbye!")  
            break  
        else:
            print("Invalid choice! Please select an option from 1 to 4.\n")


if __name__ == "__main__":
    main()  