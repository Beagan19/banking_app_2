class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, withdraw):
        self.balance -= withdraw
        print(self.name, "has an account balance of:", self.balance)

    def deposit(self, deposit):
        self.balance += deposit
        print(self.name, "has an account balance of:", self.balance)

    def transfer_money(self, bank_user, transfer):
        print("You are transferring $" + str(transfer) + " to " + bank_user.name)
        print("Authentication required.")
        pin = input("Enter your PIN: ")
        if pin == str(self.pin):
            print("Transfer authorized.")
            self.balance -= transfer
            bank_user.balance += transfer
            print(self.name, "has an account balance of $" + str(self.balance))
            return True

        else:
            print("Invalid PIN. Transaction cancelled.")
            return False

    def request_money(self, bank_user, request):
        print(self.name, "is requesting $" +
              str(request), "from", bank_user.name)
        print("User authentication is required...")
        pin = input("Enter " + bank_user.name + "'s PIN: ")

        if pin != str(bank_user.pin):
            print("Invalid PIN. Transaction cancelled.")
            return False

        password = input("Enter your password: ")
        if password != self.password:
            print("Invalid password. Transaction cancelled.")
            return False

        print("Request authorized.")
        self.balance += request
        bank_user.balance -= request
        print(bank_user.name, "tranferring $",
              str(request), "to", self.name)


""" Driver Code for Task 1 
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)"""

""" Driver Code for Task 2 
user1.change_name("Bobby")
user1.change_pin(4321)
user1.change_password("newpassword")
print(user1.name, user1.pin, user1.password)"""

""" Driver Code for Task 3
bank_user1 = BankUser("Bob", 1234, "password",)
print(bank_user1.name, bank_user1.pin, bank_user1.password, bank_user1.balance)"""

""" Driver Code for Task 4
bank_user1 = BankUser("Bob", 1234, "password")
bank_user1.show_balance()
bank_user1.deposit(1000)
bank_user1.withdraw(500)"""

""" Driver Code for Task 5"""
bob = BankUser("Bob", 1234, "password")
alice = BankUser("Alice", 5678, "alicepassword")
alice.deposit(5000)
bob.show_balance()
print("\n")

alice.transfer_money(bob, 500)
bob.show_balance()
alice.show_balance()
print("\n")

alice.request_money(bob, 250)

bob.show_balance()
alice.show_balance()
