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

# Transaction class which stores attributes related to the transaction and has methods which enable information modification
class Transaction:
    def __init__(self, transaction_id, name, amount, date, category):
        self.transaction_id = transaction_id
        self.name = name
        self.amount = amount 
        self.date = date
        self.category = category
    def display(self):
        #returns a string with all the transaction details 
        return f"ID: {self.transaction_id}, Name: {self.name}, Amount: {self.amount}, Date: {self.date}, Category: {self.category}"

# Food transaction inherites attributes from the Transaction class and adds attributes specific to food transactions 
class FoodTransaction(Transaction):
    def __init__(self, transaction_id, name, amount, date, category, meal_type, location):
        super().__init(transaction_id, name, amount, date, category)
        self.meal_type = meal_type
        self.location = location
    def display(self):
        #returns a string with all the transaction details 
        return f"ID: {self.transaction_id}, Name: {self.name}, Amount: {self.amount}, Date: {self.date}, Category: {self.category}, Meal Type: {self.meal_type}, Location: {self.location}"

# Utility transaction inherites attributes from the Transaction class and adds attributes specific to utility transactions 
class UtilityTransaction(Transaction):
    def __init__(self, transaction_id, name, amount, date, category, utility_type, provider):
        super().__init__(transaction_id, name, amount, date, category)
        self.utility_type = utility_type
        self.provider = provider 
    def display(self):
        #returns a string with all the transaction details
        return f"ID: {self.transaction_id}, Name: {self.name}, Amount: {self.amount}, Date: {self.date}, Category: {self.category}, Utility Type: {self.utility_type}, Provider: {self.provider}"




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


# View transaction function allowing the user to filter transactions with given date range and category
def view_transactions():

    # Load existing transactions
    transactions = load_transactions() 

    # Print if no transaction is found
    if not transactions:
        print("No transactions found.")
        return

    # get user input 
    filtered_start_date = input("Enter the starting date range (YYYY-MM-DD): ") 
    filtered_end_date = input("Enter the ending date range (YYYY-MM-DD): ")
    filtered_category = input("Enter the category to filter (leave blank to skip): ")

    #converting given date range to datetime so it can be compared to the transaction date
    try:
        filtered_start_date = datetime.strptime(filtered_start_date, "%Y-%m-%d")
        filtered_end_date = datetime.strptime(filtered_end_date, "%Y-%m-%d")
    except ValueError:
        print("Please enter Data using the format YYYY-MM-DD")
        return

    filtered_transactions = []  # List to store filtered transactions
    for transaction in transactions:

        #converting transaction date to datetime so it can be compared to the given date range
        try: 
            transaction_date = datetime.strptime(transaction["date"], "%Y-%m-%d")
        except ValueError:
            print("Invalid date format in transaction data.")
            return
        
        #applying the filter
        if filtered_start_date <= transaction_date <= filtered_end_date: # Check if the transaction date is in the user input range
            if not filtered_category or transaction["category"].strip().lower() == filtered_category.lower(): # Check if the category matches the user input
                filtered_transactions.append(transaction) # Add the transaction to the filtered list 

    # print if the filter doesn't return any matches
    if not filtered_transactions:
        print("No transacitons found in the given filter.")
        return
    
    # print "table"
    print("\nFiltered Transactions")
    print("ID | Name | Amount | Date | Category")
    print("-" * 50) # hard coded break

    for transaction in filtered_transactions:
        print(f"{transaction['id']} | {transaction['name']} | {transaction['amount']} | {transaction['date']} | {transaction['category']}")

# Allows the user to modify transaction
def modify_transaction(): 
     # Load existing transactions
    transactions = load_transactions() 

    # Print if no transaction is found
    if not transactions:
        print("No transactions found.")
        return
    #get user input
    date = input("Enter the transaction date to modify (YYYY-MM-D): ")
    category = input("Enter the category of the transaction to modify: ")

    filtered_transactions = [ t for t in transactions if t["date"] == date and t["category"].strip().lower() == category.lower()]
                             
    # print if the filter doesn't return any matches
    if not filtered_transactions:
        print("No transacitons found in the given filter.")
        return    
    # print "table"
    print("\nMatching Transactions")
    print("ID | Name | Amount | Date | Category")
    print("-" * 50) # hard coded break

    for transaction in filtered_transactions:
        print(f"{transaction['id']} | {transaction['name']} | {transaction['amount']} | {transaction['date']} | {transaction['category']}")
   
    try:
        transaction_id = int(input("Enter the ID of the transaction you would like to modify: "))
    except ValueError:
        print("Invalid ID entered.")

    
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            new_name = input(f"Enter new name ({transaction['name']}): ") or transaction['name']
            try:
                new_amount = input(f"Enter new amount ({transaction['amount']}): ")
                new_amount = float(new_amount) if new_amount else transaction['amount']
            except ValueError:
                print("Invalid amount entered.")
                return
            new_date = input(f"Enter new date ({transaction['date']}): ") or transaction['date']
            new_category = input(f"Enter new category ({transaction['category']}): ") or transaction['category']
    
            transaction.update({
                "name": new_name,
                "amount": new_amount,
                "date": new_date,
                "category": new_category
            })
            save_transactions(transactions)
            print("Transaction updated")
            return
        
# View Statistics function

def display_statistics():

    transactions = load_transactions()

    if not transactions:
        print("No transactions found.")
        return 
    
# Filter transactions by date range
    start_date = input("Enter the starting date range (YYYY-MM-DD): ")
    end_date = input("Enter the ending date range (YYYY-MM-DD): ")
    
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Please enter date using the format YYYY-MM-DD")
        return

# filter transactions by date
    filtered_transactions = [t for t in transactions if start_date <= datetime.strptime(t["date"], "%Y-%m-%d") <= end_date]

    if not filtered_transactions:
        print("No transactions found in the given date range.")
        return

# group transactions by category
    category_groups = {}
    for transaction in filtered_transactions:
        category = transaction["category"].strip().lower() # normalizing catergories to lowercase
        if category not in category_groups:
            category_groups[category] = []
        category_groups[category].append(transaction)

# displaying statistics for each category 
    print("-" * 50)
    print("\nStatistics by Category:")

    # calculations fot each category
    for category, transactions in category_groups.items():
        try:
            # total amount per catergory
            total_amount = sum(t["amount"] for t in transactions)
            # average amount per category
            average_amount = total_amount / len(transactions)
            # highest cost transaction
            max_amount = max(t["amount"] for t in transactions)
            # lowest cost transaction
            min_amount = min(t["amount"] for t in transactions)

            print(f"\nCatergory: {category}")
            print(f"Total Amount: {total_amount}")
            print(f"Average Amount: {average_amount}")
            print(f"Highest Cost Transaction: {max_amount}")
            print(f"Lowest Cost Transaction: {min_amount}")

            # in case there are no transactions in the category
        except ZeroDivisionError:
            print(f"\nCatergory: {category}")
            print("No transactions found for this category.")

    # overall statistics
    print("-" * 50)
    print("\nOverall Statistics:")

    # calculations fot overall
    total_spent = sum(t["amount"] for t in filtered_transactions)
    avg_daily_spent = total_spent / ((end_date - start_date).days + 1)
    max_transaction = max(filtered_transactions, key=lambda t: t["amount"])
    min_transaction = min(filtered_transactions, key=lambda t: t["amount"])
    
    # displaying the stats, rounded to 2 decimal places for dollar amouint. 
    print(f"  Total spent: ${total_spent:.2f}")
    print(f"  Average daily spent: ${avg_daily_spent:.2f}")
    print(f"  Highest cost transaction: {max_transaction['name']} (${max_transaction['amount']:.2f})")
    print(f"  Lowest cost transaction: {min_transaction['name']} (${min_transaction['amount']:.2f})")

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
            view_transactions()
        elif choice == "3":
            modify_transaction()
        elif choice == "4":
            display_statistics()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
