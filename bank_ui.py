from bank_sys import BankSystem

def handle_user_session(bank, username):
    while True:
        print("\nChoose transaction:")
        print("a. Deposit")
        print("b. Withdraw")
        print("c. Check Balance")
        print("d. Exit")

        choice = input("Enter choice: ").strip().lower()

        if choice in ["a", "deposit"]:
            amount = float(input("Enter deposit amount: "))
            print(bank.deposit(username, amount))
        elif choice in ["b", "withdraw"]:
            amount = float(input("Enter withdrawal amount: "))
            print(bank.withdraw(username, amount))
        elif choice in ["c", "check balance"]:
            print(bank.check_balance(username))
        elif choice in ["d", "exit"]:
            print("\nThank you for transacting with SSSS!.")
            break
        else:
            print("Invalid choice, please try again.")

def SSSS():
    bank = BankSystem()

    while True:
        print("\nWelcome to SSSS Banking System!")
        print("a. Login")
        print("b. Exit")
        choice = input("Choose an option (a/b): ").strip().lower()

        if choice == "a":
            username = input("Enter your username: ").strip()

            if not bank.sign_in_user(username):
                register = input("No account found. Register? (yes/no): ").strip().lower()
                if register == "yes":
                    initial_balance = float(input("Enter initial balance: "))
                    print(bank.register_user(username, initial_balance))
                else:
                    print("Registration skipped.")

            handle_user_session(bank, username)
        elif choice == "b":
            print("Thank you for using SSSS banking system!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    SSSS()
