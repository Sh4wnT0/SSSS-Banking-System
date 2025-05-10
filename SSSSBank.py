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
            self.save_accounts()  # Save changes
            print(f"Account created successfully for {username}.")
    
    def sign_in_user(self, username):
        if username in self.accounts:
            print(f"Welcome back, {username}.")
            return True
        else:
            print("Account not found. Please register.")
            return False
    
    def deposit(self, username, amount):
        if username in self.accounts:
            self.accounts[username] += amount
            self.save_accounts()  # Save after deposit
            print(f"Deposited {amount}. New balance: {self.accounts[username]}")
        else:
            print("Account not found.")
    
    def withdraw(self, username, amount, category):
     if username in self.accounts:
        balance = self.accounts[username]
        
        # Define withdrawal limits based on category
        limits = {
            "a" or "wants": 0.5 * balance,  # Maximum 50% of balance
            "b" or "needs": 0.75 * balance,  # Maximum 75% of balance
            "c" or "emergencies": balance    # Maximum 100% of balance
        }
        
        # Check if category is valid
        if category not in limits:
            print("Invalid category. Choose Wants, Needs, or Emergencies.")
            return

        # Ensure withdrawal does not exceed category limit
        if amount <= limits[category]:
            self.accounts[username] -= amount
            self.save_accounts()  # Save changes
            print(f"Withdrew {amount} for {category}. Remaining balance: {self.accounts[username]}")
        elif category == 'a':
            print(f"Withdrawal exceeds limit! Max allowed for wants: {limits[category]}")
        elif category == 'b':
            print(f"Withdrawal exceeds limit! Max allowed for needs: {limits[category]}")
     else:
        print("Account not found.")

    def check_balance(self, username):
        if username in self.accounts:
            print(f"Your current balance is: {self.accounts[username]}")
        else:
            print("Account not found.")

def main():
    while True:
        bank = BankSystem()
        print("\nWelcome to SSSS Banking System!") 
        print("a. Login")
        print("b. Exit")
        choice = input("Choose an option a or b: ").lower()


        if choice == "a":
                username = input("Enter your username: ")
                
                if username not in bank.accounts:
                    register = input("No existing account found. Would you like to register? (yes/no): ").lower()
                    if register == "yes":
                        bank.register_user(username, initial_balance=float(input("Enter initial balance: ")))
                    else:
                        print("Registration skipped.")
                
                if bank.sign_in_user(username):
                    while True:
                        print("\nChoose transaction: a.Deposit, b.Withdraw, c.Check Balance, d.Exit")
                        choice = input("Enter choice: ").lower()
                        
                        if choice == "deposit" or choice == "a":
                            amount = float(input("Enter deposit amount: "))
                            bank.deposit(username, amount)
                        elif choice == "withdraw" or choice == "b":
                            amount = float(input("Enter withdrawal amount: "))
                            category = input("Is this for a.Wants, b.Needs, or c.Emergencies? ").lower()
                            bank.withdraw(username, amount, category)
                        elif choice == "check balance" or choice == "c":
                            bank.check_balance(username)
                        elif choice == "exit" or choice == "d":
                            print("\nThank you for using our banking system.")
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