class Bank:
    def __init__(self):
        pass
        

    def main(self):
        choice = input("Start Banking(d/w/s/x): ")
        balance = 1000
        while True:
            
            if choice == 'x':
                break

            if choice == 'd':
                amount = float(input("Amount to deposit $"))
                balance += amount # balance = balance + amount
                print(f"Amount deposited ${amount:.2f}")

            elif choice == 'w':
                amount = float(input("Amount to withdraw $"))
                if balance >= amount:
                    balance -= amount # balance = balance - amount
                    print(f"Amount withdrawn ${amount:.2f}")
                else:
                    print("Insufficient funds")

            elif choice == 's':
                print(f"Starting balance ${balance:.2f}")

            else:
                print("Unknown choice!")

            choice = input("Continue Banking(d/w/s/x): ")


if __name__ == "__main__":
    bank = Bank()
    bank.main()
