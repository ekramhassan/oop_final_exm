import random

class User:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Account not enough money.")
        else:
            self.balance -= amount

    def check_balance(self):
        print("Your balance is: $", self.balance)

    def transfer(self, to_user, amount):
        if amount > self.balance:
            print("Account not enough money.")
        else:
            self.balance -= amount
            to_user.balance += amount

    def get_transaction_history(self):
        print("Your transaction history is:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount):
        if amount > 2 * self.balance:
            print("You can't take a loan.")
        else:
            self.balance += amount

class Admin:
    def __init__(self, name):
        self.name = name

    def create_account(self, name, account_number, balance):
        new_user = User(name, account_number, balance)
        return new_user

    def check_total_available_balance(self):
        total_balance = 0
        for user in users:
            total_balance += user.balance
        return total_balance

    def check_total_loan_amount(self):
        total_loan_amount = 0
        for user in users:
            total_loan_amount += user.loan_amount
        return total_loan_amount

    def on_off_loan_feature(self, status):
        loan_feature = status
        return loan_feature

#  the users and admin
users = []
admin = Admin("Admin")
while True:

    user_input = input("PLEASE CHOICE ONE (create, deposit, withdraw, transfer, check, loan, history, quit): ")

    
    if user_input == "create":
        name = input("Enter your name: ")
        account_number = random.randint(10000, 99999)
        balance = 1000
        new_user = admin.create_account(name, account_number, balance)
        users.append(new_user)
        print("Account created successfully!")
    elif user_input == "deposit":
        user_name = input("Enter your name: ")
        account_number = input("Enter your account number: ")
        amount = int(input("Enter the amount you want to deposit: "))
        for user in users:
            if user.name == user_name and user.account_number == account_number:
                user.deposit(amount)
                print("Deposit successful!")
                break
        else:
            print("Your account does not exit.")
    elif user_input == "withdraw":
        user_name = input("Enter your name: ")
        account_number = input("Enter your account number: ")
        amount = int(input("Enter the amount you want to withdraw: "))
        for user in users:
            if user.name == user_name and user.account_number == account_number:
                user.withdraw(amount)
                print("Withdrawal successful!")
                break
        else:
            print("Your account does not exit.")
    elif user_input == "transfer":
        from_user_name = input("Enter your name: ")
        from_account_number = input("Enter your account number: ")
        to_user_name = input("Enter the recipient's name: ")
        to_account_number = input("Enter the recipient's account number: ")
        amount = int(input("Enter the amount transfer: "))
        from_user_found = False
        to_user_found = False
        for from_user in users:
            if from_user.name == from_user_name and from_user.account_number == from_account_number:
                from_user_found = True
                for to_user in users:
                    if to_user.name == to_user_name and to_user.account_number == to_account_number:
                        to_user_found = True
                        from_user.transfer(to_user, amount)
                        print("Transfer successful!")
                        break
                break
        if not from_user_found:
            print("Invalid sender name or account number.")
        if not to_user_found:
            print("Invalid recipient name or account number.")
    elif user_input == "check":
        user_name = input("Enter your name: ")
        account_number = input("Enter your account number: ")
        for user in users:
            if user.name == user_name and user.account_number == account_number:
                user.check_balance()
                break
        else:
            print("Invalid user name or account number.")
    elif user_input == "loan":
        user_name = input("Enter your name: ")
        account_number = input("Enter your account number: ")
        amount = int(input("Enter the loan amount: "))
        for user in users:
            if user.name == user_name and user.account_number == account_number:
                user.take_loan(amount)
                print("Loan taken successfully!")
                break
        else:
            print("Invalid user name or account number.")
    elif user_input == "history":
        user_name = input("Enter your name: ")
        account_number = input("Enter your account number: ")
        for user in users:
            if user.name == user_name and user.account_number == account_number:
                user.get_transaction_history()
                break
        else:
            print("Invalid user name or account number.")
    elif user_input == "exit":
        print("Goodbye!")
        break
    else:
        print(" Please try again.")
