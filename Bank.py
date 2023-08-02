import random 

class Validation():
    def d_amount(self, amount):
        if amount.isdigit():
            return int(amount)
        else:
            return 
    
    def w_amount(self, amount):
        if amount.isdigit():
            return int(amount)
        else:
            return
    
    def check_pin(self, pin):
        if 4<=len(pin)<9:
            return int(pin)
        
    def acc_id_check(self, id):
        if id.isdigit():
            return int(id)
        else:
            return

class Login_page(Validation):
    def deposit(self):
        self.amount = input('Enter amount to deposit: ')
        amt = self.d_amount(self.amount) 
        if amt == None:
            print('Invalid input\nEnter numeric value')
            return 
        else:
            self.balance += amt
        # self.balance += self.amount
        print(f'Rs.{self.amount} has been deposited to this account\nYour current balance is {self.balance} ')
    def withdraw(self):
        self.amount = input('Enter amount to withdraw: ')
        amt = self.w_amount(self.amount)
        if amt == None:
            print('Invalid input\nEnter numeric value')
            return 
        else:
            self.balance -= amt
        print(f'Rs.{self.amount} has been deposited to this account\nYour current balance is {self.balance} ')

class Bank(Login_page, Validation):
    def __init__(self):
        self.balance = 0
        self.pin = 0
        self.account_holder_id = 0
        choice = input('1.Enter 1 to Create new account\n2.Enter 2 to login existing account\n')
        if choice == '1':
            self.create()
        elif choice == '2':
            self.login()
        else:
            print('Invalid input')
            return

    def create(self):
        self.name = input('Enter name: ')
        self.address = input("Enter address: ")
        self.account_holder_id = random.randint(10000,1000000)
        pin = input('Create new pin: ')
        temp_pin = self.check_pin(pin)
        if temp_pin == None:
            print('Pin must be numeric and should contain atleast 4 value.')
            return
        else:
            self.pin = temp_pin
        print(f"Your account bank has been created\nyour new account id is {self.account_holder_id}")

    def login(self):
        account_id = input("Enter your bank id: ")
        account_id = self.acc_id_check(account_id)
        passcode = input('Enter Pin: ')
        if account_id == self.account_holder_id and passcode == self.pin:
            choice = input('1.Enter 1 to deposite amount\n2.Enter 2 to withdraw amount\n')
            if choice == '1':
                self.deposite()
            elif choice == '2':
                self.withdraw()
            else:
                print('Invalid input')
                return 
        else:
            print('Invalid pin or id')
            return
       
    
            
sanima = Bank()
sanima.login()
