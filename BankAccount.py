class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, add_amount):

        print(self.balance)
        self.balance = self.balance + add_amount
        return self.balance

    def withdraw(self, withdraw_amount):

        if withdraw_amount <= self.balance:
            self.balance = self.balance - withdraw_amount
            return self.balance

        else:
            print('insufficient funds please check once')


owner_name = input('Enter user Name')
balance_amount = int(input('Enter Amount: '))


acc1 = Account(owner_name, balance_amount)

balance_amount = acc1.deposit(int(input('Enter deposit amount: ')))
print(balance_amount)
balance = acc1.withdraw(int(input('Enter the withdraw amount: ')))
print(balance)

