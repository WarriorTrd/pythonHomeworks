from random import randint

class account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}'s account number is {self.account_number} and it has a balance of {self.balance}"

class bank(account):
    def __init__(self, account_number, name, balance):
        super().__init__(account_number, name, balance)

    def create_account(self):
        self.name = input("Enter the name of the account holder: ")
        self.account_number = randint(1000000000, 9999999999)
        self.balance = int(input("Enter the initial balance: "))
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"{self.name} has withdrawn {amount} and the balance is {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"{self.name} has deposited {amount} and the balance is {self.balance}"

    def transfer(self, amount, recipient):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            recipient.balance += amount
            return f"{self.name} has transferred {amount} to {recipient.name} and the balance is {self.balance}"

    def save_to_file(self):
        with open("bankinfos.txt", "a") as file:
            file.write(f"{self.name},{self.account_number},{self.balance}\n")

    @staticmethod
    def load_from_file():
        try:
            with open("bankinfos.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            return "No saved accounts found"

accounts = {}  
menu = int(input("Enter 1 to create an account, 2 to withdraw, 3 to deposit, 4 to transfer, 5 to save to file, 6 to load from file, 0 to exit: "))

while menu != 0:
    if menu == 1:
        new_account = bank(0, "", 0).create_account()
        accounts[new_account.account_number] = new_account
        print(new_account)

    elif menu in [2, 3, 4, 5]:
        acc_num = int(input("Enter your account number: "))
        if acc_num not in accounts:
            print("Account not found. Create an account first.")
        else:
            account1 = accounts[acc_num]

            if menu == 2:
                amount = int(input("Enter the amount to withdraw: "))
                print(account1.withdraw(amount))
            
            elif menu == 3:
                amount = int(input("Enter the amount to deposit: "))
                print(account1.deposit(amount))
            
            elif menu == 4:
                recipient_acc = int(input("Enter recipient account number: "))
                if recipient_acc in accounts:
                    amount = int(input("Enter the amount to transfer: "))
                    print(account1.transfer(amount, accounts[recipient_acc]))
                else:
                    print("Recipient account not found.")
            
            elif menu == 5:
                account1.save_to_file()
                print("Account saved.")

    elif menu == 6:
        print(bank.load_from_file())

    menu = int(input("\nEnter 1 to create an account, 2 to withdraw, 3 to deposit, 4 to transfer, 5 to save to file, 6 to load from file, 0 to exit: "))
