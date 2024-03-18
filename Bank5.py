class Bank:
    def __init__(self):
        self.balance = 1000

    def read_amount(self, action):
        return float(input(f"Amount to {action} $"))

    def deposit(self):
        amount = self.read_amount("deposit")
        self.balance += amount
        print(f"Amount {amount:.2f} deposited")

    def withdraw(self):
        amount = self.read_amount("withdraw")
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount {amount:.2f} withdrawn")
        else:
            print("Insufficient funds!")

    def show(self):
        print(f"Starting balance ${self.balance:.2f}")

    def read_choice(self):
        return input("Start Banking (d/w/s/x): ")[0].lower()

    def help(self):
        print("d - deposit")
        print("w - withdraw")
        print("s - show")
        print("x - exit")

    def menu(self):
        while True:
            c = self.read_choice()
            if c == 'x':
                break
            elif c == 'd':
                self.deposit()
            elif c == 'w':
                self.withdraw()
            elif c == 's':
                self.show()
            else:
                self.help()


if __name__ == "__main__":
    Bank().menu()
