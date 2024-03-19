class Bank:
    def __init__(self):
        self.balance = 1000

    def deposit(self):
        amount = float(input("Amount to deposit $"))
        self.balance += amount
        print(f"Amount deposited ${amount:.2f}")

    def withdraw(self):
        amount = float(input("Amount to withdraw $"))
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount withdrawn ${amount:.2f}")
        else:
            print("Insufficient funds")

    def show_balance(self):
        print(f"Current balance ${self.balance:.2f}")

    def main(self):
        while True:
            choice = input("Start Banking(d/w/s/x): ")
            
            if choice == 'x':
                break

            elif choice == 'd':
                self.deposit()

            elif choice == 'w':
                self.withdraw()

            elif choice == 's':
                self.show_balance()

            else:
                print("Unknown choice!")

            choice = input("Continue Banking(d/w/s/x): ")


if __name__ == "__main__":
    bank = Bank()
    bank.main()
