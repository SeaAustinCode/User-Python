
class User:
    
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance

    def make_deposits(self, amnt):
        self.balance += amnt

    def make_withdrawal(self, amnt):
        self.balance -= amnt

    def user_account_balance(self): # what is self a key representing the instance
        print(self.name)
        print(self.balance)

    def transfer_money(self, amnt,recipient):
        self.make_withdrawal(amnt)
        recipient.make_deposits(amnt)
        self.user_account_balance()
        recipient.user_account_balance()

#make withdrawal from user1 [x]
#make deposit to recipient
#print user1 and recipient account balance


jeff = User("jeff", 2000)
eric = User("eric", 5000)
bruce = User("bruce", 7500)
# print(jeff)
# jeff.make_deposits(500)
# print(jeff.balance)
jeff.make_deposits(200)
jeff.make_deposits(500)
jeff.make_deposits(1000)
jeff.make_withdrawal(700)
jeff.user_account_balance()

eric.make_deposits(500)
eric.make_deposits(500)
eric.make_withdrawal(250)
eric.make_withdrawal(250)
eric.user_account_balance()

bruce.make_deposits(1000)
bruce.make_withdrawal(50)
bruce.make_withdrawal(50)
bruce.make_withdrawal(250)
bruce.user_account_balance()

print(                )
jeff.transfer_money(500,eric)


