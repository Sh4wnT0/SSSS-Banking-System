import json

class BankSystem:
    def __init__(self, filename="accounts.json"):
        self.filename = filename
        self.accounts = self.load_accounts()

    def load_accounts(self):
        """Load account data from a JSON file."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  # Return empty dictionary if file doesn't exist or is invalid

    def save_accounts(self):
        """Save account data to a JSON file."""
        with open(self.filename, "w") as file:
            json.dump(self.accounts, file, indent=4)

    def register_user(self, username, initial_balance=0):
        if username in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[username] = initial_balance
            self.save_accounts()
            print(f"Account created successfully for {username}.")

    def sign_in_user(self, username):
        if username in self.accounts:
            print(f"Welcome back, {username}.")
            return True
        else:
            print("Account not found. Please register.")
            return False

    def deposit(self, username, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a valid amount.")
            return
        
        if username in self.accounts:
            self.accounts[username] += amount
            self.save_accounts()
            print(f"Deposited ₱{amount}. New balance: ₱{self.accounts[username]}")
        else:
            print("Account not found.")

    def withdraw(self, username, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a valid amount.")
            return
        
        if username in self.accounts:
            balance = self.accounts[username]
            
            # Define withdrawal limits
            limits = {
                "a": 0.25 * balance,  # Wants: max 50% of balance
                "b": 0.75 * balance,  # Needs: max 75% of balance
                "c": balance          # Emergencies: max 100% of balance
            }
            
            # Loop until a valid category is chosen
            while True:
                category = input("Choose category: 'a' for Wants, 'b' for Needs, 'c' for Emergencies: ").strip().lower()
                if category in limits:
                    break
                print("Invalid category. Please try again.")

            if amount <= limits[category]:
                self.accounts[username] -= amount
                self.save_accounts()
                print(f"Withdrew ₱{amount} for {category}. Remaining balance: ₱{self.accounts[username]}")
            else:
                print(f"Withdrawal exceeds limit! Max allowed for ₱{category}: ₱{limits[category]}")
        else:
            print("Account not found.")

    def check_balance(self, username):
        if username in self.accounts:
            print(f"Your current balance is: ₱{self.accounts[username]}")
        else:
            print("Account not found.")

def main():
    bank = BankSystem()

    while True:
        print("\nWelcome to SSSS Banking System!") 
        print("a. Login")
        print("b. Exit")
        choice = input("Choose an option (a/b): ").strip().lower()

        if choice == "a":
            username = input("Enter your username: ").strip()

            if username not in bank.accounts:
                register = input("No existing account found. Would you like to register? (yes/no): ").strip().lower()
                if register == "yes":
                    initial_balance = float(input("Enter initial balance: "))
                    bank.register_user(username, initial_balance)
                else:
                    print("Registration skipped.")

            if bank.sign_in_user(username):
                while True:
                    print("\nChoose transaction:")
                    print("a. Deposit")
                    print("b. Withdraw")
                    print("c. Check Balance")
                    print("d. Exit")
                    choice = input("Enter choice: ").strip().lower()

                    if choice in ["a", "deposit"]:
                        amount = float(input("Enter deposit amount: "))
                        bank.deposit(username, amount)
                    elif choice in ["b", "withdraw"]:
                        amount = float(input("Enter withdrawal amount: "))
                        bank.withdraw(username, amount)
                    elif choice in ["c", "check balance"]:
                        bank.check_balance(username)
                    elif choice in ["d", "exit"]:
                        print("\nThank you for transacting with us!.")
                        break
                    else:
                        print("Invalid choice, please try again.")
        elif choice == "b":
            print("Thank you for using SSSS banking system!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()