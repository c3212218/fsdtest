from customer import Customer
from config import DTF,NOW

class Bank:
    def __init__(self):
        self.admin = Manager()
        self.customers = []
        self.add_customers()
    
    def main(self):
        self.menu()
    
    def add_customers(self):
        for _ in range(3):
            self.customers.append(Customer())
    
    def read_choice(self):
        print("Bank menu (L/A/X): ", end="")
        return input().strip().upper()
    
    def check_customer(self, name):
        for c in self.customers:
            if c.match(name):
                return c
        return None
    
    def read_name(self):
        print("Enter Customer Login Name: ", end="")
        return input().strip()
    
    def customer_login(self):
        c = self.check_customer(self.read_name())
        if c:
            c.use()
        else:
            print("Customer does not exist")
    
    def admin_login(self,bank):
        self.admin.use(bank)

    def show(self):
        customer = self.check_customer(self.read_name())
        if (customer != None):
            print(customer)
        else:
            print("Customer does not exist")

    def add(self):   
        newCustomer = Customer()
        customer = self.check_customer(newCustomer.name)
        if (customer == None): 
            self.customers.append(newCustomer)
        else:
            print("Customer already exists")
    
    def remove(self):
        customer = self.check_customer(self.read_name())
        if (customer != None):
            self.customers.remove(customer)
        else:
            print("Customer does not exist")
    
    def view(self):
        for customer in self.customers:
            print(customer)
    
    def menu(self):
        print("Bank menu: " + NOW.strftime(DTF))
        while True:
            choice = self.read_choice()
            if choice == 'X':
                break
            elif choice == 'L':
                self.customer_login()
            elif choice == 'A':
                self.admin_login(bank)
            else:
                self.help()
        print("Done")

    def help(self):
        print("Menu options")
        print("L = Login into customer menu")
        print("A = Login to admin menu")
        print("X = exit")

class Manager:
    def __init__(self):
        self.name = "John Smith"

    def view(self,bank):
        bank.view()

    def show(self,bank):
        bank.show()

    def remove(self,bank):
        bank.remove()

    def add(self,bank):
        bank.add()

    def read_choice(self):
        print("Manager menu (a/r/v/s/x): ", end="")
        return input().strip().lower()
    
    def use(self,bank):
        print(f"{self.name} admin menu: {NOW.strftime(DTF)}")
        c = ''
        while True:
            c = self.read_choice()
            if c == 'x':
                break
            elif c == 'a':
                self.add(bank)
            elif c == 'r':
                self.remove(bank)
            elif c == 's':
                self.show(bank)
            elif c == 'v':
                self.view(bank)
            else:
                self.help()
        print("Back to Bank menu")

    def help(self):
        print("Menu options")
        print("a = add a customer")
        print("r = remove a customer")
        print("v = view all customers")
        print("s = show the selected customer")
        print("x = exit")

# Running the main function
bank = Bank()
bank.main()