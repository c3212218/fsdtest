class Account:
    def __init__(self, type):
        self.type = type
        self.balance = float(input(f"Enter initial balance for {self.type}: "))

    def read_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposited ${amount} to {self.type} account.")
        else:
            print("Invalid input: Please enter a non-negative amount.")

    def withdraw(self, amount):
        if amount >= 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn ${amount} from {self.type} account.")
            else:
                print("Insufficient funds")
        else:
            print("Invalid input: Please enter a non-negative amount.")

    def show_balance(self):
        print(f"{self.type} account balance: ${self.balance}")

    def transfer(self, amount, target_account):
        if amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            print(f"Transferred ${amount} from {self.type} account to {target_account.type} account.")
        else:
            print("Insufficient funds for transfer.")


class Customer:
    def __init__(self, name):
        self.name = name
        self.savings = Account("Savings")
        self.loan = Account("Loan")

    def read_amount(self):
        return float(input("Enter amount: "))

    def withdraw(self):
        amount = self.read_amount()
        self.savings.withdraw(amount)

    def show_status(self):
        print(f"{self.name} accounts:")
        self.savings.show_balance()
        self.loan.show_balance()

    def transfer(self):
        amount = self.read_amount()
        self.savings.transfer(amount, self.loan)
 #       self.loan.transfer(amount, self.savings)


class Bank:
    def __init__(self):
        self.customer = Customer("John Smith")

    def main(self):
        while True:
            print("\nCustomer menu:")
            print("(d) Deposit")
            print("(w) Withdraw")
            print("(t) Transfer")
            print("(s) Show balance")
            print("(x) Exit")

            option = input()

            if option == 'd':
                amount = float(input("Enter deposit amount: "))
                self.customer.savings.deposit(amount)

            elif option == 'w':
                self.customer.withdraw()

            elif option == 't':
                self.customer.transfer()

            elif option == 's':
                self.customer.show_status()

            elif option == 'x':
                print("Exiting the system")
                break

            else:
                print("Invalid option, please try again")


if __name__ == "__main__":
    bank = Bank()
    bank.main()
