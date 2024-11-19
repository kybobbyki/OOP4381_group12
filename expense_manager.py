import json
import os
from datetime import datetime

# Can configure a db here as well instead we are saving to a file for each of use
TRANSACTION_FILE = "transactions.json"

# Load all transactions from the file
def load_transactions():
    """Loads transaction data from a JSON file."""
    if not os.path.exists(TRANSACTION_FILE):
        return []
    with open(TRANSACTION_FILE, "r") as file:
        return json.load(file)

# This method is invoked when adding transaction as well... used as a common write method
def save_transactions(transactions):
    """Saves transaction data to a JSON file."""
    with open(TRANSACTION_FILE, "w") as file:
        json.dump(transactions, file, indent=4)

# Add a new transaction
def add_transaction():
    """Prompts the user to add a new transaction and saves it."""
    transactions = load_transactions()  # Load existing transactions
    transaction_id = len(transactions) + 1  # Generate a unique ID

    # Gather transaction details from the user
    name = input("Enter the transaction name: ")
    try:
        amount = float(input("Enter the transaction amount: "))
    except ValueError:
        print("Invalid amount! Please enter a numeric value.")
        return
    date = input("Enter the transaction date (YYYY-MM-DD): ")
    category = input("Enter the transaction category (e.g., Food, Transport, etc.): ")

    # Append the new transaction
    transactions.append({
        "id": transaction_id,
        "name": name,
        "amount": amount,
        "date": date,
        "category": category
    })

    # Save the updated transactions to the file
    save_transactions(transactions)
    print("Transaction added successfully!")

# Main menu loop
def main():
    """Main menu for the Expense Manager application."""
    while True:
        print("\nExpense Manager")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Modify Transaction")
        print("4. Display Statistics")
        print("5. Exit")

        # Get user input for menu choice
        choice = input("Enter your choice: ").strip()

        # Process menu choice
        if choice == "1":
            add_transaction()
        elif choice == "2":
            print("Feature not implemented yet: View Transactions")
        elif choice == "3":
            print("Feature not implemented yet: Modify Transaction")
        elif choice == "4":
            print("Feature not implemented yet: Display Statistics")
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
