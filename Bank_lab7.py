import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Account:
    def __init__(self, type):
        self.type = type
        self.balance = 0.0

    def read_balance(self):
        self.balance = float(input(f"Enter {self.type} account balance: $"))

    def match(self, type):
        return self.type == type

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f} into {self.type} account.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount:.2f} from {self.type} account.")
        else:
            print("Insufficient funds.")

    def show_balance(self):
        print(f"{self.type} account balance: ${self.balance:.2f}")

    def transfer(self, amount, other_account):
        if self.type == "Savings" and other_account.type == "Loan":
            if amount <= self.balance:
                self.balance -= amount
                other_account.balance += amount
                print(f"Transferred ${amount:.2f} from Savings to Loan account.")
            else:
                print("Insufficient funds.")
        else:
            print("Transfer can only be made from Savings to Loan account.")

    def __str__(self):
        return f"{self.type} balance $:{self.balance:.2f}"


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = [Account("Savings"), Account("Loan")]

    def read_amount(self):
        return float(input(f"Enter amount for {self.name}: $"))

    def verify_name(self, name):
        return self.name == name

    def lookup(self, type):
        for account in self.accounts:
            if account.match(type):
                return account
        return None

    def withdraw(self, type):
        account = self.lookup(type)
        if account:
            amount = self.read_amount()
            account.withdraw(amount)
        else:
            print(f"{type} account not found for {self.name}.")

    def show_accounts_info(self):
        print(f"{self.name} accounts:")
        for account in self.accounts:
            print(account)

    def transfer(self):
        savings = self.lookup("Savings")
        loan = self.lookup("Loan")
        if savings and loan:
            amount = self.read_amount()
            savings.transfer(amount, loan)
        else:
            print(f"Savings or Loan account not found for {self.name}.")

    def get_name(self):
        return self.name


class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer(self, name):
        for customer in self.customers:
            if customer.verify_name(name):
                return customer
        return None

    def show_customer_info(self):
        for customer in self.customers:
            print(f"\nCustomer: {customer.get_name()}")
            for account in customer.accounts:
                print(f"{account.type} account balance: ${account.balance:.2f}")

    def main(self):
        
    # Initialize customers
        num_customers = int(input("Enter the number of customers: "))
        for i in range(num_customers):
            name = input(f"Enter customer {i+1} name: ")
            savings_balance = float(input(f"Enter savings account balance for {name}: "))
            loan_balance = float(input(f"Enter loan account balance for {name}: "))

            customer = Customer(name)
            customer.accounts[0].balance = savings_balance
            customer.accounts[1].balance = loan_balance
            bank.add_customer(customer)
            
        while True:
            print(f"\nCustomer Menu: (Current date and time: {now})")
            print("(L) Login")
            print("(V) View all customers")
            print("(X) Exit")

            choice = input().upper()

            if choice == 'L':
                name = input("Enter your name: ")
                customer = self.find_customer(name)
                if customer:
                    self.customer_menu(customer)
                else:
                    print("Customer not found.")
            elif choice == 'V':
                self.show_customer_info()
            elif choice == 'X':
                print("Exiting the system")
                break
            else:
                print("Invalid choice, please try again.")

    def customer_menu(self, customer):
        while True:
            print(f"\nCustomer Menu for {customer.get_name()}:")
            print("(D) Deposit")
            print("(W) Withdraw")
            print("(T) Transfer")
            print("(S) Show balance")
            print("(B) Back to main menu")

            choice = input().upper()

            if choice == 'D':
                customer.accounts[0].deposit(customer.read_amount())
            elif choice == 'W':
                customer.withdraw("Savings")
            elif choice == 'T':
                customer.transfer()
            elif choice == 'S':
                customer.show_accounts_info()
            elif choice == 'B':
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    bank = Bank()
    bank.main()
