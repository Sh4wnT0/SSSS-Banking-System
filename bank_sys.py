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
                "a": 0.5 * balance,  # Wants: max 50% of balance
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
